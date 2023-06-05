from collections import namedtuple
from typing import Any

from bson.objectid import ObjectId
from flask_restx import Resource, abort
from marshmallow_mongoengine import ModelSchema as ModelSerializer
from mongoengine import Document
from mongoengine.errors import InvalidQueryError, ValidationError
from mongoengine.queryset.queryset import QuerySet
from pymongo.command_cursor import CommandCursor
from werkzeug.exceptions import BadRequest, HTTPException

from starwars_api.extensions.openapi import api

RelatedObjectId = namedtuple("ObjectId", "pk")


class MongoDocumentsResource(Resource):
    model_class: Document = None
    serializer_class: ModelSerializer = None
    aggregations: list[object] = []

    ###
    ### Basic REST operations
    ###
    def list_all_documents(self) -> list[Document]:
        """Get all mongo documents"""
        try:
            return self.get_documents()
        except Exception:
            raise self.abort_on_error("get")

    def retrive_document_by_object_id(self, object_id: str) -> Document:
        """Get mongo document by objectId or raise if not exists"""
        try:
            return self.get_documents(id=object_id)
        except Exception:
            raise self.abort_on_error("retrieve")

    def create_new_document(self, mongo_document) -> None:
        """ "Create document in mongo saving new instance"""
        try:
            mongo_document.save()
        except ValidationError as exc:
            exc_message = exc.message.replace("None", "null")
            raise self.abort_on_validation_error({exc.field_name: exc_message})
        except Exception:
            raise self.abort_on_error("create")

    def update_document(self, mongo_document, api_payload) -> Document:
        """Update mongo document in mongo with new data"""
        try:
            errors = self.serializer_class().validate(api_payload)
        except Exception:
            raise self.abort_on_error("deserialize json payload")

        if errors:
            raise self.abort_on_validation_error(errors)

        try:
            mongo_document.update(**api.payload)
        except InvalidQueryError:
            raise self.abort_on_unprocessable_entity()
        except ValidationError as exc:
            exc_message = exc.message.replace("None", "null")
            raise self.abort_on_validation_error({exc.field_name: exc_message})
        except Exception:
            raise self.abort_on_error("update")

        try:
            mongo_document.reload()
        except Exception:
            raise self.abort_on_error("reload")
        return mongo_document

    def delete_document(self, mongo_document) -> None:
        """Delete mongo document"""
        try:
            mongo_document.delete()
        except Exception:
            raise self.abort_on_error("delete")

    ###
    ### Generic mongo documents management
    ###
    def get_documents(self, **filters) -> list[Document | dict]:
        """Get mongo documents iterating response generators for a list"""
        documents = self.model_class.objects(**filters)
        if self.aggregations:
            documents = documents.aggregate(self.aggregations)
        return documents

    ###
    ### Normalization operations
    ###
    def normalize_aggregated_results(self, mongo_result: CommandCursor) -> list[dict]:
        """Convert generator objects from mongodb normalizing to a list"""
        return [self.normalize_document_fields(document) for document in mongo_result]

    def normalize_document_fields(self, aggregated_document: dict):
        """Fix wrong association ObjectId without pk attribute in aggregated results"""
        for field_key, field_value in aggregated_document.items():
            if isinstance(field_value, list):
                normalized_objects = [self.fix_object_id_missing_pk_attribute(sub_value) for sub_value in field_value]
            else:
                normalized_objects = self.fix_object_id_missing_pk_attribute(field_value)
            aggregated_document[field_key] = normalized_objects
        return aggregated_document

    def fix_object_id_missing_pk_attribute(self, field_value):
        """Fix wrong association ObjectId without pk attribute in aggregated results"""
        if isinstance(field_value, ObjectId) and not hasattr(field_value, "pk"):
            return RelatedObjectId(pk=str(field_value))
        else:
            return field_value

    ###
    ### Serialization operations
    ###
    def serialize_documents_to_json(self, mongo_documents, many=False) -> dict[Any, Any]:
        """Serialize found mongo document to json response"""
        try:
            return self.serializer_class(many=many).dump(mongo_documents)
        except Exception as exc:
            raise self.abort_on_error("serialize to json")

    def deserialize_json_payload_to_document(self, api_payload) -> Document:
        """Deserialize json payload to a new mongo document"""
        try:
            serializer = self.serializer_class()
            errors = serializer.validate(api_payload)
            if errors:
                raise self.abort_on_validation_error(errors)
            return serializer.load(api_payload)
        except BadRequest:
            raise
        except Exception:
            raise self.abort_on_error("deserialize json payload")

    ###
    ### Known exceptions to raise on operation methods
    ###
    def abort_on_not_found(self) -> HTTPException:
        return abort(code=404, message=f"{self.model_class.__name__} resource not found.")

    def abort_on_unprocessable_entity(self) -> HTTPException:
        return abort(code=422, message="Unprocessable resource, please check your payload field definitions.")

    def abort_on_error(self, action_name: str) -> HTTPException:
        return abort(code=500, message=f"Error on {action_name} {self.model_class.__name__} resource.")

    def abort_on_validation_error(self, errors: dict | list) -> HTTPException:
        return abort(code=400, message="Input payload validation failed", errors=errors)


class ListCreateAPIResource(MongoDocumentsResource):
    """Resource base class to create and list many mongo documents"""

    def list(self) -> dict[Any, Any]:  # TODO: fix typing to list[dict[Any, Any]]
        """List all mongo documents"""
        mongo_documents = self.list_all_documents()
        if self.aggregations:
            mongo_documents = self.normalize_aggregated_results(mongo_documents)
        return self.serialize_documents_to_json(mongo_documents, many=True)

    def create(self) -> dict[Any, Any]:
        """Create a mongo document"""
        mongo_document = self.deserialize_json_payload_to_document(api.payload)
        self.create_new_document(mongo_document)
        return self.serialize_documents_to_json(mongo_document)


class DetailAPIResource(MongoDocumentsResource):
    """Resource base class to retrieve, update, partial update and delete a specific mongo document"""

    def retrieve(self, object_id: str) -> dict[Any, Any]:
        """Retrieve a mongo document"""
        mongo_documents = self.retrive_document_by_object_id(object_id)
        if self.aggregations:
            mongo_documents = self.normalize_aggregated_results(mongo_documents)
        if not mongo_documents:
            raise self.abort_on_not_found()
        return self.serialize_documents_to_json(mongo_documents[0])

    def update(self, object_id: str) -> dict[Any, Any]:
        """Update a mongo_document"""
        mongo_document = self.retrive_document_by_object_id(object_id)
        if not mongo_document:
            raise self.abort_on_not_found()
        mongo_document = self.update_document(mongo_document, api.payload)
        return self.serialize_documents_to_json(mongo_document)

    def destroy(self, object_id: str) -> tuple:
        """Delete a mongo document"""
        mongo_document = self.retrive_document_by_object_id(object_id)
        if not mongo_document:
            raise self.abort_on_not_found()
        self.delete_document(mongo_document)
        return ("", 204)

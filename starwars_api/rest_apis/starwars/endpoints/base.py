from typing import Any

from flask_restx import Resource, abort
from marshmallow_mongoengine import ModelSchema as ModelSerializer
from mongoengine import Document
from mongoengine.errors import InvalidQueryError, ValidationError
from werkzeug.exceptions import BadRequest, HTTPException

from starwars_api.extensions.openapi import api


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
            mongo_document = self.get_documents(id=object_id)
        except Exception:
            raise self.abort_on_error("retrieve")
        if not mongo_document:
            raise self.abort_on_not_found()
        return mongo_document

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
        return list(documents)

    ###
    ### Serialization operations
    ###
    def serialize_documents_to_json(self, mongo_documents, many=False) -> dict[Any, Any]:
        """Serialize found mongo document to json response"""
        try:
            # get first object from list
            if many is False and isinstance(mongo_documents, list):
                mongo_documents = mongo_documents[0]
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
        mongo_document = self.retrive_document_by_object_id(object_id)
        return self.serialize_documents_to_json(mongo_document)

    def update(self, object_id: str) -> dict[Any, Any]:
        """Update a mongo_document"""
        mongo_document = self.retrive_document_by_object_id(object_id)
        mongo_document = self.update_document(mongo_document, api.payload)
        return self.serialize_documents_to_json(mongo_document)

    def destroy(self, object_id: str) -> tuple:
        """Delete a mongo document"""
        mongo_document = self.retrive_document_by_object_id(object_id)
        self.delete_document(mongo_document)
        return ("", 204)

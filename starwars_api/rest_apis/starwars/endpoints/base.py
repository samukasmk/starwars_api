from flask import Response
from flask_restx import Resource, abort
from mongoengine.errors import InvalidQueryError, ValidationError
from werkzeug.exceptions import HTTPException

from starwars_api.extensions.openapi import api


class MongoDocumentsResource(Resource):
    model_class = None
    serializer_class = None

    ###
    ### exceptions to raise on operation methods
    ###
    def abort_on_not_found(self):
        return abort(code=404, message=f"{self.model_class.__name__} resource not found.")

    def abort_on_unprocessable_entity(self):
        return abort(code=422, message="Unprocessable resource, please check your payload field definitions.")

    def abort_on_error(self, action_name):
        return abort(code=500, message=f"Error on {action_name} {self.model_class.__name__} resource.")

    def abort_on_validation_error(self, exc):
        exc_message = exc.message.replace('"None"', "null")
        return abort(code=400, message="Input payload validation failed", errors={exc.field_name: exc_message})

    ###
    ### mongo document operations
    ###
    def get_all_documents(self):
        """Get all mongo documents"""
        try:
            return self.model_class.objects()
        except Exception:
            raise self.abort_on_error("get")

    def get_document_by_object_id(self, object_id):
        """Get mongo document by objectId or raise if not exists"""
        try:
            mongo_document = self.model_class.objects.with_id(object_id=object_id)
        except Exception:
            raise self.abort_on_error("retrieve")
        if not mongo_document:
            raise self.abort_on_not_found()
        return mongo_document

    def create_new_document(self, mongo_document):
        """ "Create document in mongo saving new instance"""
        try:
            mongo_document.save()
        except Exception:
            raise self.abort_on_error("create")

    def update_document(self, mongo_document, api_payload):
        """Update mongo document in mongo with new data"""
        try:
            mongo_document.update(**api.payload)
        except InvalidQueryError:
            raise self.abort_on_unprocessable_entity()
        except ValidationError as exc:
            raise self.abort_on_validation_error(exc)
        except Exception:
            raise self.abort_on_error("update")

        try:
            mongo_document.reload()
        except Exception:
            raise self.abort_on_error("reload")
        return mongo_document

    def delete_document(self, mongo_document):
        """Delete mongo document"""
        try:
            mongo_document.delete()
        except Exception:
            raise self.abort_on_error("delete")

    def serialize_document_to_json(self, mongo_document, many=False):
        """Serialize found mongo document to json response"""
        try:
            return self.serializer_class(many=many).dump(mongo_document)
        except Exception:
            raise self.abort_on_error("serialize to json")

    def deserialize_json_payload_to_document(self, api_payload):
        """Deserialize json payload to a new mongo document"""
        try:
            return self.serializer_class().load(api_payload)
        except Exception:
            raise self.abort_on_error("deserialize json payload")


class ListCreateAPIResource(MongoDocumentsResource):
    """Resource base class to create and list many mongo documents"""

    def list(self) -> Response | HTTPException:
        """List all mongo documents"""
        mongo_documents = self.get_all_documents()
        return self.serialize_document_to_json(mongo_documents, many=True)

    def create(self) -> Response | HTTPException:
        """Create a mongo document"""
        mongo_document = self.deserialize_json_payload_to_document(api.payload)
        self.create_new_document(mongo_document)
        return self.serialize_document_to_json(mongo_document)


class DetailAPIResource(MongoDocumentsResource):
    """Resource base class to retrieve, update, partial update and delete a specific mongo document"""

    def retrieve(self, object_id: str) -> Response | HTTPException:
        """Retrieve a mongo document"""
        mongo_document = self.get_document_by_object_id(object_id)
        return self.serialize_document_to_json(mongo_document)

    def update(self, object_id: str) -> Response | HTTPException:
        """Update a mongo_document"""
        api.payload.pop("id", None)
        mongo_document = self.get_document_by_object_id(object_id)
        mongo_document = self.update_document(mongo_document, api.payload)
        return self.serialize_document_to_json(mongo_document)

    def destroy(self, object_id: str) -> tuple:
        """Delete a mongo document"""
        mongo_document = self.get_document_by_object_id(object_id)
        self.delete_document(mongo_document)
        return ("", 204)

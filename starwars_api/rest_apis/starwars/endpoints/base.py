from flask import Response
from flask_restx import Resource, abort
from werkzeug.exceptions import HTTPException

from starwars_api.extensions.openapi import api


class ResourceBase(Resource):
    model_class = None
    serializer_class = None

    def abort_on_not_found(self):
        return abort(code=404, message=f"{self.model_class.__name__} resource not found")

    def abort_on_error(self, action):
        return abort(code=500, message=f"Error on {action} {self.model_class.__name__} resource")


class ListCreateAPIResource(ResourceBase):
    """API Endpoint to create and list many mongo documents"""

    def list(self) -> Response | HTTPException:
        """List all mongo documents"""

        # get mongo documents
        try:
            mongo_documents = self.model_class.objects()
        except Exception:
            return self.abort_on_error('get')

        # serialize found mongo documents to json response
        try:
            serializer = self.serializer_class(many=True)
            response_dict = serializer.dump(mongo_documents)
        except Exception:
            return self.abort_on_error('serialize to json')

        return response_dict

    def create(self) -> Response | HTTPException:
        """Create a mongo document"""

        # deserialize json payload to a new mongo document
        try:
            serializer = self.serializer_class()
            mongo_document = serializer.load(api.payload)
        except Exception:
            return self.abort_on_error('deserialize json payload')

        # create document in mongo
        try:
            mongo_document.save()
        except Exception:
            return self.abort_on_error('create')

        # serialize created mongo document to json response
        response_dict = serializer.dump(mongo_document)

        return response_dict


class DetailAPIResource(ResourceBase):
    """API Endpoint to retrieve, update, partial update and delete a specific mongo document"""

    def retrieve(self, mongo_document_id: str) -> Response | HTTPException:
        """Retrieve a mongo document"""

        # get mongo document by objectId
        try:
            mongo_document = self.model_class.objects.with_id(object_id=mongo_document_id)
        except Exception:
            return self.abort_on_error('get')

        # check if mongo document was found
        if not mongo_document:
            return self.abort_on_not_found()

        # serialize found mongo document to json response
        try:
            serializer = self.serializer_class()
            response_dict = serializer.dump(mongo_document)
        except Exception:
            return self.abort_on_error('serialize to json')

        return response_dict

    def update(self, mongo_document_id: str) -> Response | HTTPException:
        """Update a mongo_document"""

        # get mongo document by objectId
        try:
            mongo_document = self.model_class.objects.with_id(object_id=mongo_document_id)
        except Exception:
            return self.abort_on_error('find')

        # check if mongo document was found
        if not mongo_document:
            return self.abort_on_not_found()

        # remove id field to prevent duplicity failures
        api.payload.pop("id", None)

        # update mongo document in mongo with new data
        try:
            mongo_document.update(**api.payload)
            mongo_document.reload()
        except Exception:
            return self.abort_on_error('update')

        # serialize updated mongo document to json response
        try:
            serializer = self.serializer_class()
            response_dict = serializer.dump(mongo_document)
        except Exception:
            return self.abort_on_error('serialize to json')

        return response_dict

    def destroy(self, mongo_document_id: str) -> Response | HTTPException:
        """Delete a mongo_document"""

        # get mongo document by objectId
        try:
            mongo_document = self.model_class.objects.with_id(object_id=mongo_document_id)
        except Exception:
            return self.abort_on_error('find')

        # check if mongo document exists
        if not mongo_document:
            return self.abort_on_not_found()

        # delete mongo document
        try:
            mongo_document.delete()
        except Exception:
            return self.abort_on_error('delete')

        return Response(status=204)

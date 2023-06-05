from marshmallow_mongoengine import ModelSchema, fields


class BaseSerializer(ModelSchema):
    id = fields.String(dump_only=True)

    created_at = fields.DateTime(dump_only=True)
    updated_at = fields.DateTime(dump_only=True)

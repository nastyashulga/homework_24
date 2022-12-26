from marshmallow import fields, Schema, validates_schema, ValidationError

class RequestParamSchema(Schema):
    cmd = fields.Str(request=True)
    value = fields.Str(request=True)

    @validates_schema
    def validate_cmd_params(self, values, *args, **kwargs):
        valid_cmd_commands = {'filter', 'sort', 'map', 'limit', 'unique'}

        if values['cmd'] not in valid_cmd_commands:
            raise ValidationError({'cmd': f'containts invalid command={values["cmd"]}'})

        return values

class RequestParamsListSchema(Schema):
    queries = fields.Nested(RequestParamSchema, many=True)
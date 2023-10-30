from aenum import IntEnum

from pydantic_core import CoreSchema

from pydantic import BaseModel, GetJsonSchemaHandler


class OpenAPIEnum(IntEnum):
    @classmethod
    def __get_pydantic_json_schema__(cls, core_schema: CoreSchema, handler: GetJsonSchemaHandler):
        json_schema = BaseModel.__get_pydantic_json_schema__(core_schema, handler)
        json_schema = handler.resolve_ref_schema(json_schema)

        if 'enum' in json_schema:
            json_schema.update(
                type='integer',
                enum=[obj.value for obj in cls.__iter__()],
                additionalProperties={'enumObj': {obj.name: obj.value for obj in cls.__iter__()}}
            )
        return json_schema

from aenum import Enum


class OpenAPIEnum(Enum):
    @classmethod
    def __modify_schema__(cls, field_schema: dict):
        if 'enum' in field_schema:
            field_schema['type'] = 'integer'
            field_schema['enum'] = {obj.value for obj in cls.__iter__()}
            field_schema['additionalProperties'] = {'enumObj': {obj.name: obj.value for obj in cls.__iter__()}}

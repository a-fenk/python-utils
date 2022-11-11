from aenum import Enum


class OpenAPIEnum(Enum):
    @classmethod
    def __modify_schema__(cls, field_schema: dict):
        if 'enum' in field_schema:
            field_schema['primitive'] = [{obj.name: obj.value} for obj in cls.__iter__()]

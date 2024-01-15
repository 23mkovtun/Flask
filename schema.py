from typing import Optional, Type

import pydantic


class AbstractAd(pydantic.BaseModel):
    header: str
    description: str
    owner: str

    @pydantic.field_validator("header")
    @classmethod
    def header_length(cls, value: str) -> str:
        if len(value) > 50:
            raise ValueError('headline is too long')
        return value

    @pydantic.field_validator("description")
    @classmethod
    def description_length(cls, value: str) -> str:
        if len(value) > 200:
            raise ValueError('description is too long')
        return value

    @pydantic.field_validator("owner")
    @classmethod
    def owner_length(cls, value: str) -> str:
        if len(value) > 50:
            raise ValueError('name is too long')
        return value


class CreateAd(AbstractAd):
    header: str
    description: str
    owner: str


class UpdateAd(AbstractAd):
    header: Optional[str] = None
    description: Optional[str] = None
    # owner: Optional[str] = None


SCHEMA_CLASS = Type[CreateAd | UpdateAd]
SCHEMA = CreateAd | UpdateAd

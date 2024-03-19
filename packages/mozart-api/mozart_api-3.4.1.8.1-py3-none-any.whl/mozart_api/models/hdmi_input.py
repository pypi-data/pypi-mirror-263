# coding: utf-8

"""
    Mozart platform API

    API for interacting with the Mozart platform.

    The version of the OpenAPI document: 0.2.0
    Contact: support@bang-olufsen.dk
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json


from typing import Optional
from pydantic import BaseModel, Field, StrictStr


class HdmiInput(BaseModel):
    """
    HdmiInput
    """

    content_uri: Optional[StrictStr] = Field(
        None,
        alias="contentUri",
        description="This points to the editable content trigger for this specific hdmi input",
    )
    input: Optional[StrictStr] = None
    __properties = ["contentUri", "input"]

    class Config:
        """Pydantic configuration"""

        allow_population_by_field_name = True
        validate_assignment = True

    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.dict(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> HdmiInput:
        """Create an instance of HdmiInput from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> HdmiInput:
        """Create an instance of HdmiInput from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return HdmiInput.parse_obj(obj)

        _obj = HdmiInput.parse_obj(
            {"content_uri": obj.get("contentUri"), "input": obj.get("input")}
        )
        return _obj

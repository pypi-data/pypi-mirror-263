"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import json
import pprint
import re  # noqa: F401

from pydantic import BaseModel, Field

from span_panel.client.models.state_of_energy import StateOfEnergy


class BatteryStorage(BaseModel):
    """
    BatteryStorage
    """

    soe: StateOfEnergy = Field(...)
    __properties = ["soe"]

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
    def from_json(cls, json_str: str) -> BatteryStorage:
        """Create an instance of BatteryStorage from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of soe
        if self.soe:
            _dict["soe"] = self.soe.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> BatteryStorage:
        """Create an instance of BatteryStorage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return BatteryStorage.parse_obj(obj)

        _obj = BatteryStorage.parse_obj(
            {
                "soe": (
                    StateOfEnergy.from_dict(obj.get("soe"))
                    if obj.get("soe") is not None
                    else None
                ),
            },
        )
        return _obj

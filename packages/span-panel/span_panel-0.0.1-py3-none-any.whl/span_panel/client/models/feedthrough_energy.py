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
from typing import Union

from pydantic import BaseModel, Field, StrictFloat, StrictInt


class FeedthroughEnergy(BaseModel):
    """
    FeedthroughEnergy
    """

    produced_energy_wh: Union[StrictFloat, StrictInt] = Field(
        ...,
        alias="producedEnergyWh",
    )
    consumed_energy_wh: Union[StrictFloat, StrictInt] = Field(
        ...,
        alias="consumedEnergyWh",
    )
    __properties = ["producedEnergyWh", "consumedEnergyWh"]

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
    def from_json(cls, json_str: str) -> FeedthroughEnergy:
        """Create an instance of FeedthroughEnergy from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> FeedthroughEnergy:
        """Create an instance of FeedthroughEnergy from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return FeedthroughEnergy.parse_obj(obj)

        _obj = FeedthroughEnergy.parse_obj(
            {
                "produced_energy_wh": obj.get("producedEnergyWh"),
                "consumed_energy_wh": obj.get("consumedEnergyWh"),
            },
        )
        return _obj

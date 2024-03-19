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

from span_panel.client.models.network_status import NetworkStatus
from span_panel.client.models.software_status import SoftwareStatus
from span_panel.client.models.system_status import SystemStatus


class StatusOut(BaseModel):
    """
    StatusOut
    """

    software: SoftwareStatus = Field(...)
    system: SystemStatus = Field(...)
    network: NetworkStatus = Field(...)
    __properties = ["software", "system", "network"]

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
    def from_json(cls, json_str: str) -> StatusOut:
        """Create an instance of StatusOut from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self):
        """Returns the dictionary representation of the model using alias"""
        _dict = self.dict(by_alias=True, exclude={}, exclude_none=True)
        # override the default output from pydantic by calling `to_dict()` of software
        if self.software:
            _dict["software"] = self.software.to_dict()
        # override the default output from pydantic by calling `to_dict()` of system
        if self.system:
            _dict["system"] = self.system.to_dict()
        # override the default output from pydantic by calling `to_dict()` of network
        if self.network:
            _dict["network"] = self.network.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: dict) -> StatusOut:
        """Create an instance of StatusOut from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return StatusOut.parse_obj(obj)

        _obj = StatusOut.parse_obj(
            {
                "software": (
                    SoftwareStatus.from_dict(obj.get("software"))
                    if obj.get("software") is not None
                    else None
                ),
                "system": (
                    SystemStatus.from_dict(obj.get("system"))
                    if obj.get("system") is not None
                    else None
                ),
                "network": (
                    NetworkStatus.from_dict(obj.get("network"))
                    if obj.get("network") is not None
                    else None
                ),
            },
        )
        return _obj

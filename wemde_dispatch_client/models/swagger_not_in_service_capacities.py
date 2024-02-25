# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from wemde_dispatch_client.models.not_in_service_capacities import NotInServiceCapacities
from typing import Optional, Set
from typing_extensions import Self

class SwaggerNotInServiceCapacities(BaseModel):
    """
    SwaggerNotInServiceCapacities
    """ # noqa: E501
    dispatch_interval: Optional[datetime] = Field(default=None, alias="dispatchInterval")
    not_in_service_capacities: Optional[List[NotInServiceCapacities]] = Field(default=None, alias="notInServiceCapacities")
    __properties: ClassVar[List[str]] = ["dispatchInterval", "notInServiceCapacities"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of SwaggerNotInServiceCapacities from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in not_in_service_capacities (list)
        _items = []
        if self.not_in_service_capacities:
            for _item in self.not_in_service_capacities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['notInServiceCapacities'] = _items
        # set to None if not_in_service_capacities (nullable) is None
        # and model_fields_set contains the field
        if self.not_in_service_capacities is None and "not_in_service_capacities" in self.model_fields_set:
            _dict['notInServiceCapacities'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SwaggerNotInServiceCapacities from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dispatchInterval": obj.get("dispatchInterval"),
            "notInServiceCapacities": [NotInServiceCapacities.from_dict(_item) for _item in obj["notInServiceCapacities"]] if obj.get("notInServiceCapacities") is not None else None
        })
        return _obj


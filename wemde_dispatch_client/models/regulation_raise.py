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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Union
from wemde_dispatch_client.models.facility import Facility
from typing import Optional, Set
from typing_extensions import Self

class RegulationRaise(BaseModel):
    """
    Real-Time Market Submissions for Regulation Raise Market Service.
    """ # noqa: E501
    market_service: StrictStr = Field(description="The Market Service the Real-Time Market Submission applies to.", alias="marketService")
    base_forecast_requirement: Union[StrictFloat, StrictInt] = Field(description="The total forecast requirement for the relevant Market Service.", alias="baseForecastRequirement")
    override_forecast_requirement: Union[StrictFloat, StrictInt] = Field(description="The total override forecast requirement used in replacement to baseForecastRequirement. The baseForecastRequirement is overriden when this field has a valid and acceptable numerical value.", alias="overrideForecastRequirement")
    facilities: List[Facility] = Field(description="An array of Facilities with Real-Time Market Submissions for the relevant Market Service.")
    __properties: ClassVar[List[str]] = ["marketService", "baseForecastRequirement", "overrideForecastRequirement", "facilities"]

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
        """Create an instance of RegulationRaise from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in facilities (list)
        _items = []
        if self.facilities:
            for _item in self.facilities:
                if _item:
                    _items.append(_item.to_dict())
            _dict['facilities'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RegulationRaise from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "marketService": obj.get("marketService"),
            "baseForecastRequirement": obj.get("baseForecastRequirement"),
            "overrideForecastRequirement": obj.get("overrideForecastRequirement"),
            "facilities": [Facility.from_dict(_item) for _item in obj["facilities"]] if obj.get("facilities") is not None else None
        })
        return _obj



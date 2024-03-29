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
from typing import Any, ClassVar, Dict, List, Optional, Union
from wemde_dispatch_client.models.dispatch import Dispatch
from typing import Optional, Set
from typing_extensions import Self

class DispatchInstructionsData(BaseModel):
    """
    DispatchInstructionsData
    """ # noqa: E501
    facility_code: Optional[StrictStr] = Field(default=None, description="Participant Facility Code", alias="facilityCode")
    sent_out: Optional[Dispatch] = Field(default=None, alias="sentOut")
    as_generated: Optional[Dispatch] = Field(default=None, alias="asGenerated")
    ramp_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Ramp rate value", alias="rampRate")
    regulation_raise_enablement_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Enablement quantity for the Regulation Raise", alias="regulationRaiseEnablementQuantity")
    regulation_lower_enablement_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Enablement quantity for the Regulation Lower", alias="regulationLowerEnablementQuantity")
    contingency_raise_enablement_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Enablement quantity for the Contingency Raise", alias="contingencyRaiseEnablementQuantity")
    contingency_lower_enablement_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Enablement quantity for the Contingency Lower", alias="contingencyLowerEnablementQuantity")
    rocof_enablement_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Enablement quantity for the RoCof", alias="rocofEnablementQuantity")
    __properties: ClassVar[List[str]] = ["facilityCode", "sentOut", "asGenerated", "rampRate", "regulationRaiseEnablementQuantity", "regulationLowerEnablementQuantity", "contingencyRaiseEnablementQuantity", "contingencyLowerEnablementQuantity", "rocofEnablementQuantity"]

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
        """Create an instance of DispatchInstructionsData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of sent_out
        if self.sent_out:
            _dict['sentOut'] = self.sent_out.to_dict()
        # override the default output from pydantic by calling `to_dict()` of as_generated
        if self.as_generated:
            _dict['asGenerated'] = self.as_generated.to_dict()
        # set to None if facility_code (nullable) is None
        # and model_fields_set contains the field
        if self.facility_code is None and "facility_code" in self.model_fields_set:
            _dict['facilityCode'] = None

        # set to None if ramp_rate (nullable) is None
        # and model_fields_set contains the field
        if self.ramp_rate is None and "ramp_rate" in self.model_fields_set:
            _dict['rampRate'] = None

        # set to None if regulation_raise_enablement_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.regulation_raise_enablement_quantity is None and "regulation_raise_enablement_quantity" in self.model_fields_set:
            _dict['regulationRaiseEnablementQuantity'] = None

        # set to None if regulation_lower_enablement_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.regulation_lower_enablement_quantity is None and "regulation_lower_enablement_quantity" in self.model_fields_set:
            _dict['regulationLowerEnablementQuantity'] = None

        # set to None if contingency_raise_enablement_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.contingency_raise_enablement_quantity is None and "contingency_raise_enablement_quantity" in self.model_fields_set:
            _dict['contingencyRaiseEnablementQuantity'] = None

        # set to None if contingency_lower_enablement_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.contingency_lower_enablement_quantity is None and "contingency_lower_enablement_quantity" in self.model_fields_set:
            _dict['contingencyLowerEnablementQuantity'] = None

        # set to None if rocof_enablement_quantity (nullable) is None
        # and model_fields_set contains the field
        if self.rocof_enablement_quantity is None and "rocof_enablement_quantity" in self.model_fields_set:
            _dict['rocofEnablementQuantity'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DispatchInstructionsData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "facilityCode": obj.get("facilityCode"),
            "sentOut": Dispatch.from_dict(obj["sentOut"]) if obj.get("sentOut") is not None else None,
            "asGenerated": Dispatch.from_dict(obj["asGenerated"]) if obj.get("asGenerated") is not None else None,
            "rampRate": obj.get("rampRate"),
            "regulationRaiseEnablementQuantity": obj.get("regulationRaiseEnablementQuantity"),
            "regulationLowerEnablementQuantity": obj.get("regulationLowerEnablementQuantity"),
            "contingencyRaiseEnablementQuantity": obj.get("contingencyRaiseEnablementQuantity"),
            "contingencyLowerEnablementQuantity": obj.get("contingencyLowerEnablementQuantity"),
            "rocofEnablementQuantity": obj.get("rocofEnablementQuantity")
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class FacilityScheduleDetail(BaseModel):
    """
    FacilityScheduleDetail
    """ # noqa: E501
    facility_code: Optional[StrictStr] = Field(default=None, description="Facility Code to which the associated values Facility Schedule Details applies to", alias="facilityCode")
    contingency_raise_pf: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The Contingency Raise Performance Factor of the Facility", alias="contingencyRaisePF")
    contingency_lower_pf: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The Contingency Lower Performance Factor of the Facility", alias="contingencyLowerPF")
    regulation_raise_pf: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The Regulation Raise Performance Factor of the Facility", alias="regulationRaisePF")
    regulation_lower_pf: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The Regulation Lower Performance Factor of the Facility", alias="regulationLowerPF")
    rocof_pf: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The RoCoF Performance Factor of the Facility", alias="rocofPF")
    dispatch_binding_flag: Optional[StrictBool] = Field(default=None, description="Determines if the Semi-Scheduled Facility's Dispatch Cap is Binding due to a constraint.", alias="dispatchBindingFlag")
    contingency: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Solved Contingency level associated with the Facility")
    initial_mw: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Initial MW of the Facility based from the SCADA", alias="initialMw")
    fast_start_flag: Optional[StrictBool] = Field(default=None, alias="fastStartFlag")
    fast_start_initial_mode_time: Optional[StrictInt] = Field(default=None, description="Gets or sets the Initial Fast Start Mode", alias="fastStartInitialModeTime")
    fast_start_initial_mode: Optional[StrictInt] = Field(default=None, description="Gets or sets the Initial Fast Start Mode", alias="fastStartInitialMode")
    what_if_initial_mw: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="WhatIf Initial MW of the Facility if an Intervention Constraint is present. If none, the value is the same with the Initial MW.", alias="whatIfInitialMw")
    fast_start_target_mode: Optional[StrictInt] = Field(default=None, description="Fast-Start Current Mode of the Facility in the current Solution", alias="fastStartTargetMode")
    fast_start_target_mode_time: Optional[StrictInt] = Field(default=None, description="Fast-Start Current Mode Time of the Facility in the current Solution", alias="fastStartTargetModeTime")
    estimated_fcess_uplift_payment: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="estimatedFcessUpliftPayment")
    nol_demand: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="nolDemand")
    congestion_rental: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="congestionRental")
    facility_risk: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="facilityRisk")
    __properties: ClassVar[List[str]] = ["facilityCode", "contingencyRaisePF", "contingencyLowerPF", "regulationRaisePF", "regulationLowerPF", "rocofPF", "dispatchBindingFlag", "contingency", "initialMw", "fastStartFlag", "fastStartInitialModeTime", "fastStartInitialMode", "whatIfInitialMw", "fastStartTargetMode", "fastStartTargetModeTime", "estimatedFcessUpliftPayment", "nolDemand", "congestionRental", "facilityRisk"]

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
        """Create an instance of FacilityScheduleDetail from a JSON string"""
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
        # set to None if facility_code (nullable) is None
        # and model_fields_set contains the field
        if self.facility_code is None and "facility_code" in self.model_fields_set:
            _dict['facilityCode'] = None

        # set to None if contingency_raise_pf (nullable) is None
        # and model_fields_set contains the field
        if self.contingency_raise_pf is None and "contingency_raise_pf" in self.model_fields_set:
            _dict['contingencyRaisePF'] = None

        # set to None if contingency_lower_pf (nullable) is None
        # and model_fields_set contains the field
        if self.contingency_lower_pf is None and "contingency_lower_pf" in self.model_fields_set:
            _dict['contingencyLowerPF'] = None

        # set to None if regulation_raise_pf (nullable) is None
        # and model_fields_set contains the field
        if self.regulation_raise_pf is None and "regulation_raise_pf" in self.model_fields_set:
            _dict['regulationRaisePF'] = None

        # set to None if regulation_lower_pf (nullable) is None
        # and model_fields_set contains the field
        if self.regulation_lower_pf is None and "regulation_lower_pf" in self.model_fields_set:
            _dict['regulationLowerPF'] = None

        # set to None if rocof_pf (nullable) is None
        # and model_fields_set contains the field
        if self.rocof_pf is None and "rocof_pf" in self.model_fields_set:
            _dict['rocofPF'] = None

        # set to None if dispatch_binding_flag (nullable) is None
        # and model_fields_set contains the field
        if self.dispatch_binding_flag is None and "dispatch_binding_flag" in self.model_fields_set:
            _dict['dispatchBindingFlag'] = None

        # set to None if contingency (nullable) is None
        # and model_fields_set contains the field
        if self.contingency is None and "contingency" in self.model_fields_set:
            _dict['contingency'] = None

        # set to None if initial_mw (nullable) is None
        # and model_fields_set contains the field
        if self.initial_mw is None and "initial_mw" in self.model_fields_set:
            _dict['initialMw'] = None

        # set to None if fast_start_flag (nullable) is None
        # and model_fields_set contains the field
        if self.fast_start_flag is None and "fast_start_flag" in self.model_fields_set:
            _dict['fastStartFlag'] = None

        # set to None if fast_start_initial_mode_time (nullable) is None
        # and model_fields_set contains the field
        if self.fast_start_initial_mode_time is None and "fast_start_initial_mode_time" in self.model_fields_set:
            _dict['fastStartInitialModeTime'] = None

        # set to None if fast_start_initial_mode (nullable) is None
        # and model_fields_set contains the field
        if self.fast_start_initial_mode is None and "fast_start_initial_mode" in self.model_fields_set:
            _dict['fastStartInitialMode'] = None

        # set to None if what_if_initial_mw (nullable) is None
        # and model_fields_set contains the field
        if self.what_if_initial_mw is None and "what_if_initial_mw" in self.model_fields_set:
            _dict['whatIfInitialMw'] = None

        # set to None if fast_start_target_mode (nullable) is None
        # and model_fields_set contains the field
        if self.fast_start_target_mode is None and "fast_start_target_mode" in self.model_fields_set:
            _dict['fastStartTargetMode'] = None

        # set to None if fast_start_target_mode_time (nullable) is None
        # and model_fields_set contains the field
        if self.fast_start_target_mode_time is None and "fast_start_target_mode_time" in self.model_fields_set:
            _dict['fastStartTargetModeTime'] = None

        # set to None if estimated_fcess_uplift_payment (nullable) is None
        # and model_fields_set contains the field
        if self.estimated_fcess_uplift_payment is None and "estimated_fcess_uplift_payment" in self.model_fields_set:
            _dict['estimatedFcessUpliftPayment'] = None

        # set to None if nol_demand (nullable) is None
        # and model_fields_set contains the field
        if self.nol_demand is None and "nol_demand" in self.model_fields_set:
            _dict['nolDemand'] = None

        # set to None if congestion_rental (nullable) is None
        # and model_fields_set contains the field
        if self.congestion_rental is None and "congestion_rental" in self.model_fields_set:
            _dict['congestionRental'] = None

        # set to None if facility_risk (nullable) is None
        # and model_fields_set contains the field
        if self.facility_risk is None and "facility_risk" in self.model_fields_set:
            _dict['facilityRisk'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of FacilityScheduleDetail from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "facilityCode": obj.get("facilityCode"),
            "contingencyRaisePF": obj.get("contingencyRaisePF"),
            "contingencyLowerPF": obj.get("contingencyLowerPF"),
            "regulationRaisePF": obj.get("regulationRaisePF"),
            "regulationLowerPF": obj.get("regulationLowerPF"),
            "rocofPF": obj.get("rocofPF"),
            "dispatchBindingFlag": obj.get("dispatchBindingFlag"),
            "contingency": obj.get("contingency"),
            "initialMw": obj.get("initialMw"),
            "fastStartFlag": obj.get("fastStartFlag"),
            "fastStartInitialModeTime": obj.get("fastStartInitialModeTime"),
            "fastStartInitialMode": obj.get("fastStartInitialMode"),
            "whatIfInitialMw": obj.get("whatIfInitialMw"),
            "fastStartTargetMode": obj.get("fastStartTargetMode"),
            "fastStartTargetModeTime": obj.get("fastStartTargetModeTime"),
            "estimatedFcessUpliftPayment": obj.get("estimatedFcessUpliftPayment"),
            "nolDemand": obj.get("nolDemand"),
            "congestionRental": obj.get("congestionRental"),
            "facilityRisk": obj.get("facilityRisk")
        })
        return _obj



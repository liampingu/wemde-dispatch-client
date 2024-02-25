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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class DSPDispatchInstructionsParticipantWiseData(BaseModel):
    """
    DSPDispatchInstructionsParticipantWiseData
    """ # noqa: E501
    dispatch_instruction_id: Optional[StrictStr] = Field(default=None, description="Unique ID of the Instruction and this ID will be used for the Acknowledgement", alias="dispatchInstructionID")
    facility_code: Optional[StrictStr] = Field(default=None, description="Participant Facility Code", alias="facilityCode")
    issue_time: Optional[datetime] = Field(default=None, description="Time when the DSP Dispatch Instruction has been issued", alias="issueTime")
    dispatch_interval_from: Optional[datetime] = Field(default=None, description="Start interval", alias="dispatchIntervalFrom")
    dispatch_interval_to: Optional[datetime] = Field(default=None, description="End interval", alias="dispatchIntervalTo")
    withdrawal_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Dispatch Withdrawal quantity for the interval range", alias="withdrawalQuantity")
    ack_status: Optional[StrictBool] = Field(default=None, description="Acknowledgement Status", alias="ackStatus")
    __properties: ClassVar[List[str]] = ["dispatchInstructionID", "facilityCode", "issueTime", "dispatchIntervalFrom", "dispatchIntervalTo", "withdrawalQuantity", "ackStatus"]

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
        """Create an instance of DSPDispatchInstructionsParticipantWiseData from a JSON string"""
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

        # set to None if dispatch_interval_from (nullable) is None
        # and model_fields_set contains the field
        if self.dispatch_interval_from is None and "dispatch_interval_from" in self.model_fields_set:
            _dict['dispatchIntervalFrom'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DSPDispatchInstructionsParticipantWiseData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dispatchInstructionID": obj.get("dispatchInstructionID"),
            "facilityCode": obj.get("facilityCode"),
            "issueTime": obj.get("issueTime"),
            "dispatchIntervalFrom": obj.get("dispatchIntervalFrom"),
            "dispatchIntervalTo": obj.get("dispatchIntervalTo"),
            "withdrawalQuantity": obj.get("withdrawalQuantity"),
            "ackStatus": obj.get("ackStatus")
        })
        return _obj



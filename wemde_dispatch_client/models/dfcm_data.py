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
from wemde_dispatch_client.models.dfcm_validation_details import DfcmValidationDetails
from wemde_dispatch_client.models.frequency_limits import FrequencyLimits
from typing import Optional, Set
from typing_extensions import Self

class DfcmData(BaseModel):
    """
    Dynamic Frequency Control Model data used in the Dispatch Engine calculations.
    """ # noqa: E501
    dfcm_id: Optional[StrictStr] = Field(default=None, description="The Id of the DFCM data.", alias="dfcmId")
    dfcm_schema_version: Optional[StrictStr] = Field(default=None, description="The version of the DFCM data.", alias="dfcmSchemaVersion")
    frequency_limits: Optional[FrequencyLimits] = Field(default=None, alias="frequencyLimits")
    dfcm_validation_details: Optional[DfcmValidationDetails] = Field(default=None, alias="dfcmValidationDetails")
    tau_valuesfor_cr_performance_factors: Optional[List[Union[StrictFloat, StrictInt]]] = Field(default=None, description="An array of tau values for Contingency Raise Performance Factors.", alias="tauValuesforCRPerformanceFactors")
    __properties: ClassVar[List[str]] = ["dfcmId", "dfcmSchemaVersion", "frequencyLimits", "dfcmValidationDetails", "tauValuesforCRPerformanceFactors"]

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
        """Create an instance of DfcmData from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of frequency_limits
        if self.frequency_limits:
            _dict['frequencyLimits'] = self.frequency_limits.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dfcm_validation_details
        if self.dfcm_validation_details:
            _dict['dfcmValidationDetails'] = self.dfcm_validation_details.to_dict()
        # set to None if dfcm_id (nullable) is None
        # and model_fields_set contains the field
        if self.dfcm_id is None and "dfcm_id" in self.model_fields_set:
            _dict['dfcmId'] = None

        # set to None if dfcm_schema_version (nullable) is None
        # and model_fields_set contains the field
        if self.dfcm_schema_version is None and "dfcm_schema_version" in self.model_fields_set:
            _dict['dfcmSchemaVersion'] = None

        # set to None if tau_valuesfor_cr_performance_factors (nullable) is None
        # and model_fields_set contains the field
        if self.tau_valuesfor_cr_performance_factors is None and "tau_valuesfor_cr_performance_factors" in self.model_fields_set:
            _dict['tauValuesforCRPerformanceFactors'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DfcmData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dfcmId": obj.get("dfcmId"),
            "dfcmSchemaVersion": obj.get("dfcmSchemaVersion"),
            "frequencyLimits": FrequencyLimits.from_dict(obj["frequencyLimits"]) if obj.get("frequencyLimits") is not None else None,
            "dfcmValidationDetails": DfcmValidationDetails.from_dict(obj["dfcmValidationDetails"]) if obj.get("dfcmValidationDetails") is not None else None,
            "tauValuesforCRPerformanceFactors": obj.get("tauValuesforCRPerformanceFactors")
        })
        return _obj



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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class RocofControlRequirements(BaseModel):
    """
    RocofControlRequirements
    """ # noqa: E501
    minimum_rocof_control_requirement: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Required Minimum Rocof Control Requirements", alias="minimumRocofControlRequirement")
    additional_rocof_control_requirement: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Required Additional Rocof Control Requirements", alias="additionalRocofControlRequirement")
    rocof_control_requirement: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="rocofControlRequirement")
    __properties: ClassVar[List[str]] = ["minimumRocofControlRequirement", "additionalRocofControlRequirement", "rocofControlRequirement"]

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
        """Create an instance of RocofControlRequirements from a JSON string"""
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
        # set to None if minimum_rocof_control_requirement (nullable) is None
        # and model_fields_set contains the field
        if self.minimum_rocof_control_requirement is None and "minimum_rocof_control_requirement" in self.model_fields_set:
            _dict['minimumRocofControlRequirement'] = None

        # set to None if additional_rocof_control_requirement (nullable) is None
        # and model_fields_set contains the field
        if self.additional_rocof_control_requirement is None and "additional_rocof_control_requirement" in self.model_fields_set:
            _dict['additionalRocofControlRequirement'] = None

        # set to None if rocof_control_requirement (nullable) is None
        # and model_fields_set contains the field
        if self.rocof_control_requirement is None and "rocof_control_requirement" in self.model_fields_set:
            _dict['rocofControlRequirement'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RocofControlRequirements from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "minimumRocofControlRequirement": obj.get("minimumRocofControlRequirement"),
            "additionalRocofControlRequirement": obj.get("additionalRocofControlRequirement"),
            "rocofControlRequirement": obj.get("rocofControlRequirement")
        })
        return _obj



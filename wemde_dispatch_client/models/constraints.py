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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from wemde_dispatch_client.models.constraint_equation import ConstraintEquation
from wemde_dispatch_client.models.constraint_set import ConstraintSet
from typing import Optional, Set
from typing_extensions import Self

class Constraints(BaseModel):
    """
     Constraints that define the physical limits within the transmission network, contingency events, and any other  linear combination of solution variables used as inputs in the Dispatch Engine for the Dispatch Interval.
    """ # noqa: E501
    constraint_set: Optional[List[ConstraintSet]] = Field(default=None, description="An array of Constraint Set.", alias="constraintSet")
    constraint_equations: Optional[List[ConstraintEquation]] = Field(default=None, description="An array of Constraint Equations.", alias="constraintEquations")
    __properties: ClassVar[List[str]] = ["constraintSet", "constraintEquations"]

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
        """Create an instance of Constraints from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in constraint_set (list)
        _items = []
        if self.constraint_set:
            for _item in self.constraint_set:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constraintSet'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in constraint_equations (list)
        _items = []
        if self.constraint_equations:
            for _item in self.constraint_equations:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constraintEquations'] = _items
        # set to None if constraint_set (nullable) is None
        # and model_fields_set contains the field
        if self.constraint_set is None and "constraint_set" in self.model_fields_set:
            _dict['constraintSet'] = None

        # set to None if constraint_equations (nullable) is None
        # and model_fields_set contains the field
        if self.constraint_equations is None and "constraint_equations" in self.model_fields_set:
            _dict['constraintEquations'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Constraints from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "constraintSet": [ConstraintSet.from_dict(_item) for _item in obj["constraintSet"]] if obj.get("constraintSet") is not None else None,
            "constraintEquations": [ConstraintEquation.from_dict(_item) for _item in obj["constraintEquations"]] if obj.get("constraintEquations") is not None else None
        })
        return _obj



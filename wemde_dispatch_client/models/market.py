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
from wemde_dispatch_client.models.contingency_lower import ContingencyLower
from wemde_dispatch_client.models.contingency_raise import ContingencyRaise
from wemde_dispatch_client.models.energy import Energy
from wemde_dispatch_client.models.regulation_lower import RegulationLower
from wemde_dispatch_client.models.regulation_raise import RegulationRaise
from wemde_dispatch_client.models.rocof import Rocof
from typing import Optional, Set
from typing_extensions import Self

class Market(BaseModel):
    """
    Real-Time Market Submissions for all the Market Services.
    """ # noqa: E501
    energy: Optional[Energy] = None
    regulation_raise: Optional[RegulationRaise] = Field(default=None, alias="regulationRaise")
    regulation_lower: Optional[RegulationLower] = Field(default=None, alias="regulationLower")
    contingency_raise: Optional[ContingencyRaise] = Field(default=None, alias="contingencyRaise")
    contingency_lower: Optional[ContingencyLower] = Field(default=None, alias="contingencyLower")
    rocof: Optional[Rocof] = None
    __properties: ClassVar[List[str]] = ["energy", "regulationRaise", "regulationLower", "contingencyRaise", "contingencyLower", "rocof"]

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
        """Create an instance of Market from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of energy
        if self.energy:
            _dict['energy'] = self.energy.to_dict()
        # override the default output from pydantic by calling `to_dict()` of regulation_raise
        if self.regulation_raise:
            _dict['regulationRaise'] = self.regulation_raise.to_dict()
        # override the default output from pydantic by calling `to_dict()` of regulation_lower
        if self.regulation_lower:
            _dict['regulationLower'] = self.regulation_lower.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contingency_raise
        if self.contingency_raise:
            _dict['contingencyRaise'] = self.contingency_raise.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contingency_lower
        if self.contingency_lower:
            _dict['contingencyLower'] = self.contingency_lower.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rocof
        if self.rocof:
            _dict['rocof'] = self.rocof.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Market from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "energy": Energy.from_dict(obj["energy"]) if obj.get("energy") is not None else None,
            "regulationRaise": RegulationRaise.from_dict(obj["regulationRaise"]) if obj.get("regulationRaise") is not None else None,
            "regulationLower": RegulationLower.from_dict(obj["regulationLower"]) if obj.get("regulationLower") is not None else None,
            "contingencyRaise": ContingencyRaise.from_dict(obj["contingencyRaise"]) if obj.get("contingencyRaise") is not None else None,
            "contingencyLower": ContingencyLower.from_dict(obj["contingencyLower"]) if obj.get("contingencyLower") is not None else None,
            "rocof": Rocof.from_dict(obj["rocof"]) if obj.get("rocof") is not None else None
        })
        return _obj



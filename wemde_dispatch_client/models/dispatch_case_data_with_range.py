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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List
from wemde_dispatch_client.models.data_with_range import DataWithRange
from typing import Optional, Set
from typing_extensions import Self

class DispatchCaseDataWithRange(BaseModel):
    """
    DispatchCaseDataWithRange
    """ # noqa: E501
    dispatch_data_issue_id: StrictStr = Field(description="Dispatch Case Data Issue ID.", alias="dispatchDataIssueID")
    case_data: List[DataWithRange] = Field(description="Case Data Object.", alias="caseData")
    __properties: ClassVar[List[str]] = ["dispatchDataIssueID", "caseData"]

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
        """Create an instance of DispatchCaseDataWithRange from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in case_data (list)
        _items = []
        if self.case_data:
            for _item in self.case_data:
                if _item:
                    _items.append(_item.to_dict())
            _dict['caseData'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DispatchCaseDataWithRange from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dispatchDataIssueID": obj.get("dispatchDataIssueID"),
            "caseData": [DataWithRange.from_dict(_item) for _item in obj["caseData"]] if obj.get("caseData") is not None else None
        })
        return _obj



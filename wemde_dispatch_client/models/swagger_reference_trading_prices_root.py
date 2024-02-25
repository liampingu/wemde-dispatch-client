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
from typing import Any, ClassVar, Dict, List, Optional
from wemde_dispatch_client.models.swagger_reference_trading_prices import SwaggerReferenceTradingPrices
from typing import Optional, Set
from typing_extensions import Self

class SwaggerReferenceTradingPricesRoot(BaseModel):
    """
    SwaggerReferenceTradingPricesRoot
    """ # noqa: E501
    data: Optional[SwaggerReferenceTradingPrices] = None
    transaction_id: Optional[StrictStr] = Field(default=None, alias="transactionId")
    __properties: ClassVar[List[str]] = ["data", "transactionId"]

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
        """Create an instance of SwaggerReferenceTradingPricesRoot from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of data
        if self.data:
            _dict['data'] = self.data.to_dict()
        # set to None if transaction_id (nullable) is None
        # and model_fields_set contains the field
        if self.transaction_id is None and "transaction_id" in self.model_fields_set:
            _dict['transactionId'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SwaggerReferenceTradingPricesRoot from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "data": SwaggerReferenceTradingPrices.from_dict(obj["data"]) if obj.get("data") is not None else None,
            "transactionId": obj.get("transactionId")
        })
        return _obj



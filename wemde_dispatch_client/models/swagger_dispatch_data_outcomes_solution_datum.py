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
from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wemde_dispatch_client.models.available_quantities import AvailableQuantities
from wemde_dispatch_client.models.constraint import Constraint
from wemde_dispatch_client.models.contingency_solution import ContingencySolution
from wemde_dispatch_client.models.defined_contingency import DefinedContingency
from wemde_dispatch_client.models.dispatch_caps import DispatchCaps
from wemde_dispatch_client.models.dispatch_total import DispatchTotal
from wemde_dispatch_client.models.facility_schedule_detail import FacilityScheduleDetail
from wemde_dispatch_client.models.fcess_market_clearing_price_ceilings import FcessMarketClearingPriceCeilings
from wemde_dispatch_client.models.in_service_quantities import InServiceQuantities
from wemde_dispatch_client.models.market_service_requirements import MarketServiceRequirements
from wemde_dispatch_client.models.market_shortfalls import MarketShortfalls
from wemde_dispatch_client.models.price_setting import PriceSetting
from wemde_dispatch_client.models.prices import Prices
from wemde_dispatch_client.models.rocof_control_requirements import RocofControlRequirements
from wemde_dispatch_client.models.schedule import Schedule
from wemde_dispatch_client.models.trapezium_adjustment import TrapeziumAdjustment
from typing import Optional, Set
from typing_extensions import Self

class SwaggerDispatchDataOutcomesSolutionDatum(BaseModel):
    """
    SwaggerDispatchDataOutcomesSolutionDatum
    """ # noqa: E501
    categories: Optional[StrictStr] = None
    primary_dispatch_interval: Optional[datetime] = Field(default=None, alias="primaryDispatchInterval")
    dispatch_interval: Optional[datetime] = Field(default=None, alias="dispatchInterval")
    schedule: Optional[List[Schedule]] = None
    dispatch_caps: Optional[List[DispatchCaps]] = Field(default=None, alias="dispatchCaps")
    trapezium_adjustments: Optional[List[TrapeziumAdjustment]] = Field(default=None, alias="trapeziumAdjustments")
    facility_schedule_details: Optional[List[FacilityScheduleDetail]] = Field(default=None, alias="facilityScheduleDetails")
    defined_contingency: Optional[List[DefinedContingency]] = Field(default=None, alias="definedContingency")
    constraints: Optional[List[Constraint]] = None
    in_service_quantities: Optional[InServiceQuantities] = Field(default=None, alias="inServiceQuantities")
    available_quantities: Optional[AvailableQuantities] = Field(default=None, alias="availableQuantities")
    market_shortfalls: Optional[MarketShortfalls] = Field(default=None, alias="marketShortfalls")
    prices: Optional[Prices] = None
    dispatch_total: Optional[DispatchTotal] = Field(default=None, alias="dispatchTotal")
    rocof_control_requirements: Optional[RocofControlRequirements] = Field(default=None, alias="rocofControlRequirements")
    contingency_solution: Optional[ContingencySolution] = Field(default=None, alias="contingencySolution")
    price_setting: Optional[List[PriceSetting]] = Field(default=None, alias="priceSetting")
    fcess_market_clearing_price_ceilings: Optional[List[FcessMarketClearingPriceCeilings]] = Field(default=None, alias="fcessMarketClearingPriceCeilings")
    market_service_requirements: Optional[MarketServiceRequirements] = Field(default=None, alias="marketServiceRequirements")
    __properties: ClassVar[List[str]] = ["categories", "primaryDispatchInterval", "dispatchInterval", "schedule", "dispatchCaps", "trapeziumAdjustments", "facilityScheduleDetails", "definedContingency", "constraints", "inServiceQuantities", "availableQuantities", "marketShortfalls", "prices", "dispatchTotal", "rocofControlRequirements", "contingencySolution", "priceSetting", "fcessMarketClearingPriceCeilings", "marketServiceRequirements"]

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
        """Create an instance of SwaggerDispatchDataOutcomesSolutionDatum from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in schedule (list)
        _items = []
        if self.schedule:
            for _item in self.schedule:
                if _item:
                    _items.append(_item.to_dict())
            _dict['schedule'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dispatch_caps (list)
        _items = []
        if self.dispatch_caps:
            for _item in self.dispatch_caps:
                if _item:
                    _items.append(_item.to_dict())
            _dict['dispatchCaps'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in trapezium_adjustments (list)
        _items = []
        if self.trapezium_adjustments:
            for _item in self.trapezium_adjustments:
                if _item:
                    _items.append(_item.to_dict())
            _dict['trapeziumAdjustments'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in facility_schedule_details (list)
        _items = []
        if self.facility_schedule_details:
            for _item in self.facility_schedule_details:
                if _item:
                    _items.append(_item.to_dict())
            _dict['facilityScheduleDetails'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in defined_contingency (list)
        _items = []
        if self.defined_contingency:
            for _item in self.defined_contingency:
                if _item:
                    _items.append(_item.to_dict())
            _dict['definedContingency'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in constraints (list)
        _items = []
        if self.constraints:
            for _item in self.constraints:
                if _item:
                    _items.append(_item.to_dict())
            _dict['constraints'] = _items
        # override the default output from pydantic by calling `to_dict()` of in_service_quantities
        if self.in_service_quantities:
            _dict['inServiceQuantities'] = self.in_service_quantities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of available_quantities
        if self.available_quantities:
            _dict['availableQuantities'] = self.available_quantities.to_dict()
        # override the default output from pydantic by calling `to_dict()` of market_shortfalls
        if self.market_shortfalls:
            _dict['marketShortfalls'] = self.market_shortfalls.to_dict()
        # override the default output from pydantic by calling `to_dict()` of prices
        if self.prices:
            _dict['prices'] = self.prices.to_dict()
        # override the default output from pydantic by calling `to_dict()` of dispatch_total
        if self.dispatch_total:
            _dict['dispatchTotal'] = self.dispatch_total.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rocof_control_requirements
        if self.rocof_control_requirements:
            _dict['rocofControlRequirements'] = self.rocof_control_requirements.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contingency_solution
        if self.contingency_solution:
            _dict['contingencySolution'] = self.contingency_solution.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in price_setting (list)
        _items = []
        if self.price_setting:
            for _item in self.price_setting:
                if _item:
                    _items.append(_item.to_dict())
            _dict['priceSetting'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in fcess_market_clearing_price_ceilings (list)
        _items = []
        if self.fcess_market_clearing_price_ceilings:
            for _item in self.fcess_market_clearing_price_ceilings:
                if _item:
                    _items.append(_item.to_dict())
            _dict['fcessMarketClearingPriceCeilings'] = _items
        # override the default output from pydantic by calling `to_dict()` of market_service_requirements
        if self.market_service_requirements:
            _dict['marketServiceRequirements'] = self.market_service_requirements.to_dict()
        # set to None if categories (nullable) is None
        # and model_fields_set contains the field
        if self.categories is None and "categories" in self.model_fields_set:
            _dict['categories'] = None

        # set to None if schedule (nullable) is None
        # and model_fields_set contains the field
        if self.schedule is None and "schedule" in self.model_fields_set:
            _dict['schedule'] = None

        # set to None if dispatch_caps (nullable) is None
        # and model_fields_set contains the field
        if self.dispatch_caps is None and "dispatch_caps" in self.model_fields_set:
            _dict['dispatchCaps'] = None

        # set to None if trapezium_adjustments (nullable) is None
        # and model_fields_set contains the field
        if self.trapezium_adjustments is None and "trapezium_adjustments" in self.model_fields_set:
            _dict['trapeziumAdjustments'] = None

        # set to None if facility_schedule_details (nullable) is None
        # and model_fields_set contains the field
        if self.facility_schedule_details is None and "facility_schedule_details" in self.model_fields_set:
            _dict['facilityScheduleDetails'] = None

        # set to None if defined_contingency (nullable) is None
        # and model_fields_set contains the field
        if self.defined_contingency is None and "defined_contingency" in self.model_fields_set:
            _dict['definedContingency'] = None

        # set to None if constraints (nullable) is None
        # and model_fields_set contains the field
        if self.constraints is None and "constraints" in self.model_fields_set:
            _dict['constraints'] = None

        # set to None if price_setting (nullable) is None
        # and model_fields_set contains the field
        if self.price_setting is None and "price_setting" in self.model_fields_set:
            _dict['priceSetting'] = None

        # set to None if fcess_market_clearing_price_ceilings (nullable) is None
        # and model_fields_set contains the field
        if self.fcess_market_clearing_price_ceilings is None and "fcess_market_clearing_price_ceilings" in self.model_fields_set:
            _dict['fcessMarketClearingPriceCeilings'] = None

        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SwaggerDispatchDataOutcomesSolutionDatum from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "categories": obj.get("categories"),
            "primaryDispatchInterval": obj.get("primaryDispatchInterval"),
            "dispatchInterval": obj.get("dispatchInterval"),
            "schedule": [Schedule.from_dict(_item) for _item in obj["schedule"]] if obj.get("schedule") is not None else None,
            "dispatchCaps": [DispatchCaps.from_dict(_item) for _item in obj["dispatchCaps"]] if obj.get("dispatchCaps") is not None else None,
            "trapeziumAdjustments": [TrapeziumAdjustment.from_dict(_item) for _item in obj["trapeziumAdjustments"]] if obj.get("trapeziumAdjustments") is not None else None,
            "facilityScheduleDetails": [FacilityScheduleDetail.from_dict(_item) for _item in obj["facilityScheduleDetails"]] if obj.get("facilityScheduleDetails") is not None else None,
            "definedContingency": [DefinedContingency.from_dict(_item) for _item in obj["definedContingency"]] if obj.get("definedContingency") is not None else None,
            "constraints": [Constraint.from_dict(_item) for _item in obj["constraints"]] if obj.get("constraints") is not None else None,
            "inServiceQuantities": InServiceQuantities.from_dict(obj["inServiceQuantities"]) if obj.get("inServiceQuantities") is not None else None,
            "availableQuantities": AvailableQuantities.from_dict(obj["availableQuantities"]) if obj.get("availableQuantities") is not None else None,
            "marketShortfalls": MarketShortfalls.from_dict(obj["marketShortfalls"]) if obj.get("marketShortfalls") is not None else None,
            "prices": Prices.from_dict(obj["prices"]) if obj.get("prices") is not None else None,
            "dispatchTotal": DispatchTotal.from_dict(obj["dispatchTotal"]) if obj.get("dispatchTotal") is not None else None,
            "rocofControlRequirements": RocofControlRequirements.from_dict(obj["rocofControlRequirements"]) if obj.get("rocofControlRequirements") is not None else None,
            "contingencySolution": ContingencySolution.from_dict(obj["contingencySolution"]) if obj.get("contingencySolution") is not None else None,
            "priceSetting": [PriceSetting.from_dict(_item) for _item in obj["priceSetting"]] if obj.get("priceSetting") is not None else None,
            "fcessMarketClearingPriceCeilings": [FcessMarketClearingPriceCeilings.from_dict(_item) for _item in obj["fcessMarketClearingPriceCeilings"]] if obj.get("fcessMarketClearingPriceCeilings") is not None else None,
            "marketServiceRequirements": MarketServiceRequirements.from_dict(obj["marketServiceRequirements"]) if obj.get("marketServiceRequirements") is not None else None
        })
        return _obj


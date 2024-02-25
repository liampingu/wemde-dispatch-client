# SolutionDatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **str** |  | [optional] 
**dispatch_interval** | **datetime** | Target Dispatch Interval of the Solution. | [optional] 
**schedule** | [**List[Schedule]**](Schedule.md) | An array of schedule to determine the associated forecast Dispatch Targets, Dispatch Caps, Dispatch Forecasts and Essential System Services Enablement Quantities   for each Dispatch Interval or Pre-Dispatch Interval. | [optional] 
**dispatch_caps** | [**List[DispatchCaps]**](DispatchCaps.md) | Total MW level of Injection or Withdrawal that must not be exceeded by a Semi-Scheduled Facility. | [optional] 
**trapezium_adjustments** | [**List[TrapeziumAdjustment]**](TrapeziumAdjustment.md) |  An array of Trapezium Adjustments that determines the final value used for Enablement Minimum, Enablement Maximum, Low Breakpoint, High Breakpoint, and Ramp-Rates for any Registered Facility participating   in the provision of an Essential System Service based on information available to AEMO from various sources. | [optional] 
**facility_schedule_details** | [**List[FacilityScheduleDetail]**](FacilityScheduleDetail.md) | An array of Facility Schedule Details associated with the Facility in the Solution. | [optional] 
**defined_contingency** | [**List[DefinedContingency]**](DefinedContingency.md) | An array of Defined Contingencies associated with its resolved values | [optional] 
**constraints** | [**List[Constraint]**](Constraint.md) | Array of constraints associated with the Solution in the Dispatch Interval or Pre-Dispatch Interval | [optional] 
**in_service_quantities** | [**InServiceQuantities**](InServiceQuantities.md) |  | [optional] 
**available_quantities** | [**AvailableQuantities**](AvailableQuantities.md) |  | [optional] 
**market_shortfalls** | [**MarketShortfalls**](MarketShortfalls.md) |  | [optional] 
**prices** | [**Prices**](Prices.md) |  | [optional] 
**dispatch_total** | [**DispatchTotal**](DispatchTotal.md) |  | [optional] 
**rocof_control_requirements** | [**RocofControlRequirements**](RocofControlRequirements.md) |  | [optional] 
**contingency_solution** | [**ContingencySolution**](ContingencySolution.md) |  | [optional] 
**price_setting** | [**List[PriceSetting]**](PriceSetting.md) | An array of Price Setting information for each Market Service | [optional] 
**fcess_market_clearing_price_ceilings** | [**List[FcessMarketClearingPriceCeilings]**](FcessMarketClearingPriceCeilings.md) |  | [optional] 
**market_service_requirements** | [**MarketServiceRequirements**](MarketServiceRequirements.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.solution_datum import SolutionDatum

# TODO update the JSON string below
json = "{}"
# create an instance of SolutionDatum from a JSON string
solution_datum_instance = SolutionDatum.from_json(json)
# print the JSON string representation of the object
print SolutionDatum.to_json()

# convert the object into a dict
solution_datum_dict = solution_datum_instance.to_dict()
# create an instance of SolutionDatum from a dict
solution_datum_form_dict = solution_datum.from_dict(solution_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# SwaggerDispatchDataOutcomesSolutionDatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**categories** | **str** |  | [optional] 
**primary_dispatch_interval** | **datetime** |  | [optional] 
**dispatch_interval** | **datetime** |  | [optional] 
**schedule** | [**List[Schedule]**](Schedule.md) |  | [optional] 
**dispatch_caps** | [**List[DispatchCaps]**](DispatchCaps.md) |  | [optional] 
**trapezium_adjustments** | [**List[TrapeziumAdjustment]**](TrapeziumAdjustment.md) |  | [optional] 
**facility_schedule_details** | [**List[FacilityScheduleDetail]**](FacilityScheduleDetail.md) |  | [optional] 
**defined_contingency** | [**List[DefinedContingency]**](DefinedContingency.md) |  | [optional] 
**constraints** | [**List[Constraint]**](Constraint.md) |  | [optional] 
**in_service_quantities** | [**InServiceQuantities**](InServiceQuantities.md) |  | [optional] 
**available_quantities** | [**AvailableQuantities**](AvailableQuantities.md) |  | [optional] 
**market_shortfalls** | [**MarketShortfalls**](MarketShortfalls.md) |  | [optional] 
**prices** | [**Prices**](Prices.md) |  | [optional] 
**dispatch_total** | [**DispatchTotal**](DispatchTotal.md) |  | [optional] 
**rocof_control_requirements** | [**RocofControlRequirements**](RocofControlRequirements.md) |  | [optional] 
**contingency_solution** | [**ContingencySolution**](ContingencySolution.md) |  | [optional] 
**price_setting** | [**List[PriceSetting]**](PriceSetting.md) |  | [optional] 
**fcess_market_clearing_price_ceilings** | [**List[FcessMarketClearingPriceCeilings]**](FcessMarketClearingPriceCeilings.md) |  | [optional] 
**market_service_requirements** | [**MarketServiceRequirements**](MarketServiceRequirements.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dispatch_data_outcomes_solution_datum import SwaggerDispatchDataOutcomesSolutionDatum

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDispatchDataOutcomesSolutionDatum from a JSON string
swagger_dispatch_data_outcomes_solution_datum_instance = SwaggerDispatchDataOutcomesSolutionDatum.from_json(json)
# print the JSON string representation of the object
print SwaggerDispatchDataOutcomesSolutionDatum.to_json()

# convert the object into a dict
swagger_dispatch_data_outcomes_solution_datum_dict = swagger_dispatch_data_outcomes_solution_datum_instance.to_dict()
# create an instance of SwaggerDispatchDataOutcomesSolutionDatum from a dict
swagger_dispatch_data_outcomes_solution_datum_form_dict = swagger_dispatch_data_outcomes_solution_datum.from_dict(swagger_dispatch_data_outcomes_solution_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



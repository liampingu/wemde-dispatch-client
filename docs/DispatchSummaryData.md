# DispatchSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_interval** | **datetime** | Target Dispatch Interval of the Solution. | [optional] 
**markets** | [**Markets**](Markets.md) |  | [optional] 
**schedule** | [**List[Schedule]**](Schedule.md) | An array of schedule to determine the associated forecast Dispatch Targets, Dispatch Caps, Dispatch Forecasts and Essential System Services Enablement Quantities   for each Dispatch Interval or Pre-Dispatch Interval. | [optional] 
**facility_schedule_details** | [**List[FacilityScheduleDetail]**](FacilityScheduleDetail.md) | An array of Facility Schedule Details associated with the Facility in the Solution. | [optional] 
**trapezium_adjustments** | [**List[TrapeziumAdjustment]**](TrapeziumAdjustment.md) |  An array of Trapezium Adjustments that determines the final value used for Enablement Minimum, Enablement Maximum, Low Breakpoint, High Breakpoint, and Ramp-Rates for any Registered Facility participating   in the provision of an Essential System Service based on information available to AEMO from various sources. | [optional] 
**prices** | [**Prices**](Prices.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_summary_data import DispatchSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchSummaryData from a JSON string
dispatch_summary_data_instance = DispatchSummaryData.from_json(json)
# print the JSON string representation of the object
print DispatchSummaryData.to_json()

# convert the object into a dict
dispatch_summary_data_dict = dispatch_summary_data_instance.to_dict()
# create an instance of DispatchSummaryData from a dict
dispatch_summary_data_form_dict = dispatch_summary_data.from_dict(dispatch_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



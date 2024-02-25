# FacilitySchedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | Facility Code to which the the associated quantity of forecast Dispatch Targets, Dispatch Caps, Dispatch Forecasts and Essential System Services Enablement Quantities applies to | [optional] 
**quantity** | **float** | Injection or Withdrawal quantity of the forecast Dispatch Target, Dispatch Cap, Dispatch Forecast and Essential System Services Enablement Quantity | [optional] 
**ess_pre_processing_condition_flag** | **bool** | Determines whether the Registered Facility is eligible to provide the service in line with the ESS Pre-Processing for each ESS Market Service other than Energy that it is participating in | [optional] 

## Example

```python
from wemde_dispatch_client.models.facility_schedule import FacilitySchedule

# TODO update the JSON string below
json = "{}"
# create an instance of FacilitySchedule from a JSON string
facility_schedule_instance = FacilitySchedule.from_json(json)
# print the JSON string representation of the object
print FacilitySchedule.to_json()

# convert the object into a dict
facility_schedule_dict = facility_schedule_instance.to_dict()
# create an instance of FacilitySchedule from a dict
facility_schedule_form_dict = facility_schedule.from_dict(facility_schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



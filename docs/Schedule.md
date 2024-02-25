# Schedule


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | Market Service for which the associated forecast Dispatch Targets, Dispatch Caps, Dispatch Forecasts and Essential System Services Enablement Quantities applies to | [optional] 
**facility_schedule** | [**List[FacilitySchedule]**](FacilitySchedule.md) | An array of Facility Schedule that determines the associated quantity of forecast Dispatch Targets, Dispatch Caps, Dispatch Forecasts and Essential System Services Enablement Quantities  for the relevant Market Service for each Facility. | [optional] 

## Example

```python
from wemde_dispatch_client.models.schedule import Schedule

# TODO update the JSON string below
json = "{}"
# create an instance of Schedule from a JSON string
schedule_instance = Schedule.from_json(json)
# print the JSON string representation of the object
print Schedule.to_json()

# convert the object into a dict
schedule_dict = schedule_instance.to_dict()
# create an instance of Schedule from a dict
schedule_form_dict = schedule.from_dict(schedule_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



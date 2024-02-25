# DspScheduleInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**dispatch_interval** | **datetime** |  | [optional] 
**dsp_unconstrained_withdrawal_quantity** | **float** |  | [optional] 
**dsp_constrained_withdrawal_quantity** | **float** |  | [optional] 
**relevant_demand** | **float** |  | [optional] 
**min_withdrawal** | **float** |  | [optional] 
**rcoq** | **float** |  | [optional] 
**forecast_capacity** | **float** |  | [optional] 
**forecast_reduction** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.dsp_schedule_information import DspScheduleInformation

# TODO update the JSON string below
json = "{}"
# create an instance of DspScheduleInformation from a JSON string
dsp_schedule_information_instance = DspScheduleInformation.from_json(json)
# print the JSON string representation of the object
print DspScheduleInformation.to_json()

# convert the object into a dict
dsp_schedule_information_dict = dsp_schedule_information_instance.to_dict()
# create an instance of DspScheduleInformation from a dict
dsp_schedule_information_form_dict = dsp_schedule_information.from_dict(dsp_schedule_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



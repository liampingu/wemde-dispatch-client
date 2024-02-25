# DSPDispatchInstructionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | Participant Facility Code | [optional] 
**dispatch_interval_from** | **datetime** | Start interval | [optional] 
**dispatch_interval_to** | **datetime** | End interval | [optional] 
**withdrawal_quantity** | **float** | Dispatch Withdrawal quantity for the interval range | [optional] 

## Example

```python
from wemde_dispatch_client.models.dsp_dispatch_instructions_data import DSPDispatchInstructionsData

# TODO update the JSON string below
json = "{}"
# create an instance of DSPDispatchInstructionsData from a JSON string
dsp_dispatch_instructions_data_instance = DSPDispatchInstructionsData.from_json(json)
# print the JSON string representation of the object
print DSPDispatchInstructionsData.to_json()

# convert the object into a dict
dsp_dispatch_instructions_data_dict = dsp_dispatch_instructions_data_instance.to_dict()
# create an instance of DSPDispatchInstructionsData from a dict
dsp_dispatch_instructions_data_form_dict = dsp_dispatch_instructions_data.from_dict(dsp_dispatch_instructions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



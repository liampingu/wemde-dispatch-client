# DispatchInstructionsData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | Participant Facility Code | [optional] 
**sent_out** | [**Dispatch**](Dispatch.md) |  | [optional] 
**as_generated** | [**Dispatch**](Dispatch.md) |  | [optional] 
**ramp_rate** | **float** | Ramp rate value | [optional] 
**regulation_raise_enablement_quantity** | **float** | Enablement quantity for the Regulation Raise | [optional] 
**regulation_lower_enablement_quantity** | **float** | Enablement quantity for the Regulation Lower | [optional] 
**contingency_raise_enablement_quantity** | **float** | Enablement quantity for the Contingency Raise | [optional] 
**contingency_lower_enablement_quantity** | **float** | Enablement quantity for the Contingency Lower | [optional] 
**rocof_enablement_quantity** | **float** | Enablement quantity for the RoCof | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_instructions_data import DispatchInstructionsData

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchInstructionsData from a JSON string
dispatch_instructions_data_instance = DispatchInstructionsData.from_json(json)
# print the JSON string representation of the object
print DispatchInstructionsData.to_json()

# convert the object into a dict
dispatch_instructions_data_dict = dispatch_instructions_data_instance.to_dict()
# create an instance of DispatchInstructionsData from a dict
dispatch_instructions_data_form_dict = dispatch_instructions_data.from_dict(dispatch_instructions_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# DispatchInstructionDetailsResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_instruction_id** | **str** | Unique ID of each Dispatch Instruction | [optional] 
**dispatch_interval** | **datetime** | Timestamp of the primary Dispatch Interval in the series of Solutions generated in a run of a specific Dispatch Run Type. | [optional] 
**issued_time** | **datetime** | Current Datetime | [optional] 
**data** | [**List[DispatchInstructionsData]**](DispatchInstructionsData.md) | Dispatch Instruction Response Payload | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_instruction_details_response import DispatchInstructionDetailsResponse

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchInstructionDetailsResponse from a JSON string
dispatch_instruction_details_response_instance = DispatchInstructionDetailsResponse.from_json(json)
# print the JSON string representation of the object
print DispatchInstructionDetailsResponse.to_json()

# convert the object into a dict
dispatch_instruction_details_response_dict = dispatch_instruction_details_response_instance.to_dict()
# create an instance of DispatchInstructionDetailsResponse from a dict
dispatch_instruction_details_response_form_dict = dispatch_instruction_details_response.from_dict(dispatch_instruction_details_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



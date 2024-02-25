# DspReductionInstruction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_interval** | **datetime** |  | [optional] 
**requested_reductions** | [**List[RequestedReduction]**](RequestedReduction.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.dsp_reduction_instruction import DspReductionInstruction

# TODO update the JSON string below
json = "{}"
# create an instance of DspReductionInstruction from a JSON string
dsp_reduction_instruction_instance = DspReductionInstruction.from_json(json)
# print the JSON string representation of the object
print DspReductionInstruction.to_json()

# convert the object into a dict
dsp_reduction_instruction_dict = dsp_reduction_instruction_instance.to_dict()
# create an instance of DspReductionInstruction from a dict
dsp_reduction_instruction_form_dict = dsp_reduction_instruction.from_dict(dsp_reduction_instruction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



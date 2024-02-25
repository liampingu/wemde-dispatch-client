# DispatchInstructionAckRequest


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**ackstatus** | **str** | Acknowledgement status. Possible values are SUCCESS or FAILURE. | 
**errors** | [**List[DispatchErrors]**](DispatchErrors.md) | List of dispatch errors. | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_instruction_ack_request import DispatchInstructionAckRequest

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchInstructionAckRequest from a JSON string
dispatch_instruction_ack_request_instance = DispatchInstructionAckRequest.from_json(json)
# print the JSON string representation of the object
print DispatchInstructionAckRequest.to_json()

# convert the object into a dict
dispatch_instruction_ack_request_dict = dispatch_instruction_ack_request_instance.to_dict()
# create an instance of DispatchInstructionAckRequest from a dict
dispatch_instruction_ack_request_form_dict = dispatch_instruction_ack_request.from_dict(dispatch_instruction_ack_request_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



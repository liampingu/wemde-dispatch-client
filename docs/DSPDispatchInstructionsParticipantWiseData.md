# DSPDispatchInstructionsParticipantWiseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_instruction_id** | **str** | Unique ID of the Instruction and this ID will be used for the Acknowledgement | [optional] 
**facility_code** | **str** | Participant Facility Code | [optional] 
**issue_time** | **datetime** | Time when the DSP Dispatch Instruction has been issued | [optional] 
**dispatch_interval_from** | **datetime** | Start interval | [optional] 
**dispatch_interval_to** | **datetime** | End interval | [optional] 
**withdrawal_quantity** | **float** | Dispatch Withdrawal quantity for the interval range | [optional] 
**ack_status** | **bool** | Acknowledgement Status | [optional] 

## Example

```python
from wemde_dispatch_client.models.dsp_dispatch_instructions_participant_wise_data import DSPDispatchInstructionsParticipantWiseData

# TODO update the JSON string below
json = "{}"
# create an instance of DSPDispatchInstructionsParticipantWiseData from a JSON string
dsp_dispatch_instructions_participant_wise_data_instance = DSPDispatchInstructionsParticipantWiseData.from_json(json)
# print the JSON string representation of the object
print DSPDispatchInstructionsParticipantWiseData.to_json()

# convert the object into a dict
dsp_dispatch_instructions_participant_wise_data_dict = dsp_dispatch_instructions_participant_wise_data_instance.to_dict()
# create an instance of DSPDispatchInstructionsParticipantWiseData from a dict
dsp_dispatch_instructions_participant_wise_data_form_dict = dsp_dispatch_instructions_participant_wise_data.from_dict(dsp_dispatch_instructions_participant_wise_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



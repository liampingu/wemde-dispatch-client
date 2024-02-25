# SwaggerDSPDispatchInstructionsParticipantWise


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**data** | [**SwaggerDSPDispatchInstructionsParticipantWiseData**](SwaggerDSPDispatchInstructionsParticipantWiseData.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dsp_dispatch_instructions_participant_wise import SwaggerDSPDispatchInstructionsParticipantWise

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDSPDispatchInstructionsParticipantWise from a JSON string
swagger_dsp_dispatch_instructions_participant_wise_instance = SwaggerDSPDispatchInstructionsParticipantWise.from_json(json)
# print the JSON string representation of the object
print SwaggerDSPDispatchInstructionsParticipantWise.to_json()

# convert the object into a dict
swagger_dsp_dispatch_instructions_participant_wise_dict = swagger_dsp_dispatch_instructions_participant_wise_instance.to_dict()
# create an instance of SwaggerDSPDispatchInstructionsParticipantWise from a dict
swagger_dsp_dispatch_instructions_participant_wise_form_dict = swagger_dsp_dispatch_instructions_participant_wise.from_dict(swagger_dsp_dispatch_instructions_participant_wise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



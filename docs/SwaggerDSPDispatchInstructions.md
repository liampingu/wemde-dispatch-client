# SwaggerDSPDispatchInstructions


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**data** | [**SwaggerDSPDispatchInstructionsData**](SwaggerDSPDispatchInstructionsData.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dsp_dispatch_instructions import SwaggerDSPDispatchInstructions

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDSPDispatchInstructions from a JSON string
swagger_dsp_dispatch_instructions_instance = SwaggerDSPDispatchInstructions.from_json(json)
# print the JSON string representation of the object
print SwaggerDSPDispatchInstructions.to_json()

# convert the object into a dict
swagger_dsp_dispatch_instructions_dict = swagger_dsp_dispatch_instructions_instance.to_dict()
# create an instance of SwaggerDSPDispatchInstructions from a dict
swagger_dsp_dispatch_instructions_form_dict = swagger_dsp_dispatch_instructions.from_dict(swagger_dsp_dispatch_instructions_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



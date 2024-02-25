# SwaggerDspScheduleInformation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**data** | [**SwaggerGetDspScheduleInformationResponse**](SwaggerGetDspScheduleInformationResponse.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dsp_schedule_information import SwaggerDspScheduleInformation

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDspScheduleInformation from a JSON string
swagger_dsp_schedule_information_instance = SwaggerDspScheduleInformation.from_json(json)
# print the JSON string representation of the object
print SwaggerDspScheduleInformation.to_json()

# convert the object into a dict
swagger_dsp_schedule_information_dict = swagger_dsp_schedule_information_instance.to_dict()
# create an instance of SwaggerDspScheduleInformation from a dict
swagger_dsp_schedule_information_form_dict = swagger_dsp_schedule_information.from_dict(swagger_dsp_schedule_information_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



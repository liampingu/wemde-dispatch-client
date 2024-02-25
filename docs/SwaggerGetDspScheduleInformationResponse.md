# SwaggerGetDspScheduleInformationResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**issued_time** | **datetime** |  | [optional] 
**sum_of_forecast_capacity** | **float** |  | [optional] 
**sum_of_forecast_reduction** | **float** |  | [optional] 
**dsp_schedule_information** | [**List[DspScheduleInformation]**](DspScheduleInformation.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_get_dsp_schedule_information_response import SwaggerGetDspScheduleInformationResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerGetDspScheduleInformationResponse from a JSON string
swagger_get_dsp_schedule_information_response_instance = SwaggerGetDspScheduleInformationResponse.from_json(json)
# print the JSON string representation of the object
print SwaggerGetDspScheduleInformationResponse.to_json()

# convert the object into a dict
swagger_get_dsp_schedule_information_response_dict = swagger_get_dsp_schedule_information_response_instance.to_dict()
# create an instance of SwaggerGetDspScheduleInformationResponse from a dict
swagger_get_dsp_schedule_information_response_form_dict = swagger_get_dsp_schedule_information_response.from_dict(swagger_get_dsp_schedule_information_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



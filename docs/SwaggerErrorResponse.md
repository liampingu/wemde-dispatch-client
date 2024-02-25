# SwaggerErrorResponse


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**transaction_id** | **str** |  | [optional] 
**errors** | [**List[ErrorStructure]**](ErrorStructure.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_error_response import SwaggerErrorResponse

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerErrorResponse from a JSON string
swagger_error_response_instance = SwaggerErrorResponse.from_json(json)
# print the JSON string representation of the object
print SwaggerErrorResponse.to_json()

# convert the object into a dict
swagger_error_response_dict = swagger_error_response_instance.to_dict()
# create an instance of SwaggerErrorResponse from a dict
swagger_error_response_form_dict = swagger_error_response.from_dict(swagger_error_response_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



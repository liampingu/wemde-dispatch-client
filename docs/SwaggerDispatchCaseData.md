# SwaggerDispatchCaseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DispatchCaseData**](DispatchCaseData.md) |  | [optional] 
**errors** | **List[object]** |  | [optional] 
**warnings** | **List[object]** |  | [optional] 
**infos** | **List[object]** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dispatch_case_data import SwaggerDispatchCaseData

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDispatchCaseData from a JSON string
swagger_dispatch_case_data_instance = SwaggerDispatchCaseData.from_json(json)
# print the JSON string representation of the object
print SwaggerDispatchCaseData.to_json()

# convert the object into a dict
swagger_dispatch_case_data_dict = swagger_dispatch_case_data_instance.to_dict()
# create an instance of SwaggerDispatchCaseData from a dict
swagger_dispatch_case_data_form_dict = swagger_dispatch_case_data.from_dict(swagger_dispatch_case_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



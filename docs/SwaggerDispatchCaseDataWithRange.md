# SwaggerDispatchCaseDataWithRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DispatchCaseDataWithRange**](DispatchCaseDataWithRange.md) |  | [optional] 
**errors** | **List[object]** |  | [optional] 
**warnings** | **List[object]** |  | [optional] 
**infos** | **List[object]** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dispatch_case_data_with_range import SwaggerDispatchCaseDataWithRange

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDispatchCaseDataWithRange from a JSON string
swagger_dispatch_case_data_with_range_instance = SwaggerDispatchCaseDataWithRange.from_json(json)
# print the JSON string representation of the object
print SwaggerDispatchCaseDataWithRange.to_json()

# convert the object into a dict
swagger_dispatch_case_data_with_range_dict = swagger_dispatch_case_data_with_range_instance.to_dict()
# create an instance of SwaggerDispatchCaseDataWithRange from a dict
swagger_dispatch_case_data_with_range_form_dict = swagger_dispatch_case_data_with_range.from_dict(swagger_dispatch_case_data_with_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



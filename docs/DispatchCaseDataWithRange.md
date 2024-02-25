# DispatchCaseDataWithRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_data_issue_id** | **str** | Dispatch Case Data Issue ID. | 
**case_data** | [**List[DataWithRange]**](DataWithRange.md) | Case Data Object. | 

## Example

```python
from wemde_dispatch_client.models.dispatch_case_data_with_range import DispatchCaseDataWithRange

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchCaseDataWithRange from a JSON string
dispatch_case_data_with_range_instance = DispatchCaseDataWithRange.from_json(json)
# print the JSON string representation of the object
print DispatchCaseDataWithRange.to_json()

# convert the object into a dict
dispatch_case_data_with_range_dict = dispatch_case_data_with_range_instance.to_dict()
# create an instance of DispatchCaseDataWithRange from a dict
dispatch_case_data_with_range_form_dict = dispatch_case_data_with_range.from_dict(dispatch_case_data_with_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



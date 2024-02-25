# DispatchCaseData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_dispatch_interval** | **datetime** | Timestamp of the Primary Dispatch Interval in the series of Case Files generated in a run of a specific 25 Dispatch Run Type. | [optional] 
**dispatch_data_issue_id** | **str** | Dispatch Case Data Issue ID. | 
**case_data** | [**List[Data]**](Data.md) | Case Data Object. | 

## Example

```python
from wemde_dispatch_client.models.dispatch_case_data import DispatchCaseData

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchCaseData from a JSON string
dispatch_case_data_instance = DispatchCaseData.from_json(json)
# print the JSON string representation of the object
print DispatchCaseData.to_json()

# convert the object into a dict
dispatch_case_data_dict = dispatch_case_data_instance.to_dict()
# create an instance of DispatchCaseData from a dict
dispatch_case_data_form_dict = dispatch_case_data.from_dict(dispatch_case_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



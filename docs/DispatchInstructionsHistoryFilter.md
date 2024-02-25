# DispatchInstructionsHistoryFilter


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**search_all** | **bool** |  | [optional] 
**facility_id** | **str** |  | [optional] 
**from_date** | **datetime** |  | [optional] 
**to_date** | **datetime** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_instructions_history_filter import DispatchInstructionsHistoryFilter

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchInstructionsHistoryFilter from a JSON string
dispatch_instructions_history_filter_instance = DispatchInstructionsHistoryFilter.from_json(json)
# print the JSON string representation of the object
print DispatchInstructionsHistoryFilter.to_json()

# convert the object into a dict
dispatch_instructions_history_filter_dict = dispatch_instructions_history_filter_instance.to_dict()
# create an instance of DispatchInstructionsHistoryFilter from a dict
dispatch_instructions_history_filter_form_dict = dispatch_instructions_history_filter.from_dict(dispatch_instructions_history_filter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



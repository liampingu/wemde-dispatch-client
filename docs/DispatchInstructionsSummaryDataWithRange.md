# DispatchInstructionsSummaryDataWithRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_data_issue_id** | **str** | Dispatch Summary Data Issue ID. | [optional] 
**dispatch_summary_data** | [**List[DispatchSummaryDataWithRange]**](DispatchSummaryDataWithRange.md) | Dispatch Summary Data Object. | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_instructions_summary_data_with_range import DispatchInstructionsSummaryDataWithRange

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchInstructionsSummaryDataWithRange from a JSON string
dispatch_instructions_summary_data_with_range_instance = DispatchInstructionsSummaryDataWithRange.from_json(json)
# print the JSON string representation of the object
print DispatchInstructionsSummaryDataWithRange.to_json()

# convert the object into a dict
dispatch_instructions_summary_data_with_range_dict = dispatch_instructions_summary_data_with_range_instance.to_dict()
# create an instance of DispatchInstructionsSummaryDataWithRange from a dict
dispatch_instructions_summary_data_with_range_form_dict = dispatch_instructions_summary_data_with_range.from_dict(dispatch_instructions_summary_data_with_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



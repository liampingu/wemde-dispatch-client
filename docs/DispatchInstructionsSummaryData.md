# DispatchInstructionsSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_dispatch_interval** | **datetime** | Timestamp of the primary Dispatch Interval in the series of Solutions generated in a run of a specific Dispatch Run Type. | [optional] 
**dispatch_data_issue_id** | **str** | Dispatch Summary Data Issue ID. | [optional] 
**dispatch_summary_data** | [**List[DispatchSummaryData]**](DispatchSummaryData.md) | Dispatch Summary Data Object. | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_instructions_summary_data import DispatchInstructionsSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchInstructionsSummaryData from a JSON string
dispatch_instructions_summary_data_instance = DispatchInstructionsSummaryData.from_json(json)
# print the JSON string representation of the object
print DispatchInstructionsSummaryData.to_json()

# convert the object into a dict
dispatch_instructions_summary_data_dict = dispatch_instructions_summary_data_instance.to_dict()
# create an instance of DispatchInstructionsSummaryData from a dict
dispatch_instructions_summary_data_form_dict = dispatch_instructions_summary_data.from_dict(dispatch_instructions_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



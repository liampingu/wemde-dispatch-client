# DispatchSolutionData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**primary_dispatch_interval** | **datetime** | Timestamp of the primary Dispatch Interval in the series of Solutions generated in a run of a specific Dispatch Run Type. | [optional] 
**dispatch_data_issue_id** | **str** | Dispatch Solution Data Issue ID. | [optional] 
**dispatch_scenario** | **str** | Dispatch Scenario. | [optional] 
**solution_data** | [**List[SolutionDatum]**](SolutionDatum.md) | Solution Data Object. | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_solution_data import DispatchSolutionData

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchSolutionData from a JSON string
dispatch_solution_data_instance = DispatchSolutionData.from_json(json)
# print the JSON string representation of the object
print DispatchSolutionData.to_json()

# convert the object into a dict
dispatch_solution_data_dict = dispatch_solution_data_instance.to_dict()
# create an instance of DispatchSolutionData from a dict
dispatch_solution_data_form_dict = dispatch_solution_data.from_dict(dispatch_solution_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



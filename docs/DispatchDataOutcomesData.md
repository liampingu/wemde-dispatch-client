# DispatchDataOutcomesData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_data_issue_id** | **str** |  | [optional] 
**solution_data** | [**List[SwaggerDispatchDataOutcomesSolutionDatum]**](SwaggerDispatchDataOutcomesSolutionDatum.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_data_outcomes_data import DispatchDataOutcomesData

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchDataOutcomesData from a JSON string
dispatch_data_outcomes_data_instance = DispatchDataOutcomesData.from_json(json)
# print the JSON string representation of the object
print DispatchDataOutcomesData.to_json()

# convert the object into a dict
dispatch_data_outcomes_data_dict = dispatch_data_outcomes_data_instance.to_dict()
# create an instance of DispatchDataOutcomesData from a dict
dispatch_data_outcomes_data_form_dict = dispatch_data_outcomes_data.from_dict(dispatch_data_outcomes_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



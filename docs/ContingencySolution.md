# ContingencySolution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**solved_inertia** | **float** | Solved Inertia level used from the DFCM matrix lookup | [optional] 
**solved_contingency** | **float** | Solved Contingency level used from the DFCM matrix lookup | [optional] 
**contingency_raise_requirement** | **float** | Total Contingency Raise requirement in which Contingency Raise shortfall is excluded | [optional] 
**contingency_raise_deficit** | **float** | Additional Contingency Raise amount required to satisfy the Contingency Raise Requirement | [optional] 
**demand_level** | **float** | Solved Demand level used from the DFCM matrix lookup | [optional] 
**cleared_contingency_raise** | **float** | Required Contingency Raise Capacity to be dispatched in MW | [optional] 
**largest_contingency** | **float** | Value of the largest credible supply contingency | [optional] 
**contingency_raise_offset** | **float** | Determined offset value of the Contingency Reserve Raise - positive value means less Contingency Raise is required and a negative value means additional Contingency Raise is required | [optional] 
**contingency_lower_offset** | **float** | Determined offset value of the Contingency Reserve Lower - positive value means less Contingency Lower is required and a negative value means additional Contingency Lower is required | [optional] 

## Example

```python
from wemde_dispatch_client.models.contingency_solution import ContingencySolution

# TODO update the JSON string below
json = "{}"
# create an instance of ContingencySolution from a JSON string
contingency_solution_instance = ContingencySolution.from_json(json)
# print the JSON string representation of the object
print ContingencySolution.to_json()

# convert the object into a dict
contingency_solution_dict = contingency_solution_instance.to_dict()
# create an instance of ContingencySolution from a dict
contingency_solution_form_dict = contingency_solution.from_dict(contingency_solution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



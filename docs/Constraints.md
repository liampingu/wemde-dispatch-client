# Constraints

 Constraints that define the physical limits within the transmission network, contingency events, and any other  linear combination of solution variables used as inputs in the Dispatch Engine for the Dispatch Interval.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**constraint_set** | [**List[ConstraintSet]**](ConstraintSet.md) | An array of Constraint Set. | [optional] 
**constraint_equations** | [**List[ConstraintEquation]**](ConstraintEquation.md) | An array of Constraint Equations. | [optional] 

## Example

```python
from wemde_dispatch_client.models.constraints import Constraints

# TODO update the JSON string below
json = "{}"
# create an instance of Constraints from a JSON string
constraints_instance = Constraints.from_json(json)
# print the JSON string representation of the object
print Constraints.to_json()

# convert the object into a dict
constraints_dict = constraints_instance.to_dict()
# create an instance of Constraints from a dict
constraints_form_dict = constraints.from_dict(constraints_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



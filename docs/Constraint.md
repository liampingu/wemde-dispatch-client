# Constraint


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the constraint | [optional] 
**description** | **str** | Detailed description of the constraint | [optional] 
**left_hand_side_value** | **float** | Resolved value of the LHS of the constraint | [optional] 
**operator** | **str** | Operator of the constraint | [optional] 
**constraint_type** | **str** | Constraint Type | [optional] 
**right_hand_side_value** | **float** | Resolved value of the RHS of the constraint | [optional] 
**default_rhs** | **float** | Default RHS value of the constraint | [optional] 
**binding_constraint_flag** | **bool** | Determines if the constraint is binding or not | [optional] 
**near_binding_constraint_flag** | **bool** | Indicates if the constraint is within 10% of binding - the resolved LHS value is within 10% of the resolved RHS value. | [optional] 
**shadow_price** | **float** | Marginal value of the constraint. | [optional] 
**is_intervention_event** | **bool** |  | [optional] 
**slack_variables** | [**List[SlackVariable]**](SlackVariable.md) | Array of slack variables associated with the constraint | [optional] 

## Example

```python
from wemde_dispatch_client.models.constraint import Constraint

# TODO update the JSON string below
json = "{}"
# create an instance of Constraint from a JSON string
constraint_instance = Constraint.from_json(json)
# print the JSON string representation of the object
print Constraint.to_json()

# convert the object into a dict
constraint_dict = constraint_instance.to_dict()
# create an instance of Constraint from a dict
constraint_form_dict = constraint.from_dict(constraint_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



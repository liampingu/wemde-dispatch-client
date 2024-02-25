# ConstraintEquation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the Constraint Equation. | [optional] 
**description** | **str** | Description of the Constraint Equation. | [optional] 
**comments** | **str** | Comments on the Constraint Equation. | [optional] 
**left_hand_side** | [**List[LeftHandSide]**](LeftHandSide.md) | An array of the Left-Hand side terms of the relevant Constraint Equation. | [optional] 
**operator** | **str** | The operator of the Constraint Equation. | [optional] 
**right_hand_side** | [**List[RightHandSide]**](RightHandSide.md) | An array of the Right-Hand side terms of the relevant Constraint Equation. | [optional] 
**right_hand_side_script** | **str** | The equivalent Right-Hand side equation of the Right-Hand side terms of the Constraint Equation. | [optional] 
**required** | **bool** | Flag to indicate if the Constraint Equation is required or not. | [optional] 
**limit_type** | **str** | The Limit Type of the Constriant Equation. | [optional] 
**limit_advice_id** | **str** | The Id of the Limit Advice. | [optional] 
**is_intervention_event** | **bool** |  | [optional] 
**constraint_type** | **str** |  | [optional] 
**default_rhs** | **float** | The default Right-Hand side value of the Constraint Equation if the resolved Right-Hand side terms. | [optional] 
**violation_penalty** | **float** | The penalty value associated with Constraint Equation when it is violated. | [optional] 
**contingency** | **str** | The contingency element associated with the Constraint Equation. | [optional] 
**monitored_element** | **str** | The equipment or entity associated with the Constraint Equation. | [optional] 
**version** | **int** | The version of the Constraint Equation. | [optional] 
**system_configuration** | **str** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.constraint_equation import ConstraintEquation

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintEquation from a JSON string
constraint_equation_instance = ConstraintEquation.from_json(json)
# print the JSON string representation of the object
print ConstraintEquation.to_json()

# convert the object into a dict
constraint_equation_dict = constraint_equation_instance.to_dict()
# create an instance of ConstraintEquation from a dict
constraint_equation_form_dict = constraint_equation.from_dict(constraint_equation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



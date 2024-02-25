# ConstraintViolationParameter

An array of the Constraint Violation Parameters for each Dispatch Interval or Trading Interval. Refer to the XXX procedure.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | **str** | Variable name of the Constraint Violation Parameter. | [optional] 
**price** | **float** | Price associated with the Constraint Violation Parameter. | [optional] 

## Example

```python
from wemde_dispatch_client.models.constraint_violation_parameter import ConstraintViolationParameter

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintViolationParameter from a JSON string
constraint_violation_parameter_instance = ConstraintViolationParameter.from_json(json)
# print the JSON string representation of the object
print ConstraintViolationParameter.to_json()

# convert the object into a dict
constraint_violation_parameter_dict = constraint_violation_parameter_instance.to_dict()
# create an instance of ConstraintViolationParameter from a dict
constraint_violation_parameter_form_dict = constraint_violation_parameter.from_dict(constraint_violation_parameter_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



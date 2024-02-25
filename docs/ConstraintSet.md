# ConstraintSet


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the Constraint Set. | [optional] 
**constraint_equations** | **List[str]** | An array of Constraint Equations that defines a Constraint Set. | [optional] 
**version** | **int** | Version of the Constraint Set. | [optional] 
**description** | **str** | Description of the Constraint Set. | [optional] 
**comments** | **str** | Comments on the Constraint Set. | [optional] 

## Example

```python
from wemde_dispatch_client.models.constraint_set import ConstraintSet

# TODO update the JSON string below
json = "{}"
# create an instance of ConstraintSet from a JSON string
constraint_set_instance = ConstraintSet.from_json(json)
# print the JSON string representation of the object
print ConstraintSet.to_json()

# convert the object into a dict
constraint_set_dict = constraint_set_instance.to_dict()
# create an instance of ConstraintSet from a dict
constraint_set_form_dict = constraint_set.from_dict(constraint_set_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



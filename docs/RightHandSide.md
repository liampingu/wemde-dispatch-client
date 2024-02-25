# RightHandSide

An array of the Right-Hand side terms of the relevant Constraint Equation.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** | The tag for a single term of the Right-Hand side of the Constraint Equation. | [optional] 
**coefficient** | **float** | The coefficient of the term of the Right-Hand side of the Constraint Equation. | [optional] 
**term_type** | **str** | The type of the term. | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.right_hand_side import RightHandSide

# TODO update the JSON string below
json = "{}"
# create an instance of RightHandSide from a JSON string
right_hand_side_instance = RightHandSide.from_json(json)
# print the JSON string representation of the object
print RightHandSide.to_json()

# convert the object into a dict
right_hand_side_dict = right_hand_side_instance.to_dict()
# create an instance of RightHandSide from a dict
right_hand_side_form_dict = right_hand_side.from_dict(right_hand_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# LeftHandSide


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**term** | **str** | The tag for a single term of the Left-Hand side of the Constraint Equation. | [optional] 
**coefficient** | **float** | The coefficient of the term of the Left-Hand side of the Constraint Equation. | [optional] 
**term_type** | **str** | The type of the term. | [optional] 
**index** | **int** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.left_hand_side import LeftHandSide

# TODO update the JSON string below
json = "{}"
# create an instance of LeftHandSide from a JSON string
left_hand_side_instance = LeftHandSide.from_json(json)
# print the JSON string representation of the object
print LeftHandSide.to_json()

# convert the object into a dict
left_hand_side_dict = left_hand_side_instance.to_dict()
# create an instance of LeftHandSide from a dict
left_hand_side_form_dict = left_hand_side.from_dict(left_hand_side_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



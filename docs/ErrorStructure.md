# ErrorStructure


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**code** | **int** | Error Code | [optional] 
**title** | **str** | Error Title | [optional] 
**detail** | **str** | Error Details | [optional] 
**source** | **str** | Error Source | [optional] 

## Example

```python
from wemde_dispatch_client.models.error_structure import ErrorStructure

# TODO update the JSON string below
json = "{}"
# create an instance of ErrorStructure from a JSON string
error_structure_instance = ErrorStructure.from_json(json)
# print the JSON string representation of the object
print ErrorStructure.to_json()

# convert the object into a dict
error_structure_dict = error_structure_instance.to_dict()
# create an instance of ErrorStructure from a dict
error_structure_form_dict = error_structure.from_dict(error_structure_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



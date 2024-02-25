# DispatchErrors


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**title** | **str** |  | [optional] 
**detail** | **str** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_errors import DispatchErrors

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchErrors from a JSON string
dispatch_errors_instance = DispatchErrors.from_json(json)
# print the JSON string representation of the object
print DispatchErrors.to_json()

# convert the object into a dict
dispatch_errors_dict = dispatch_errors_instance.to_dict()
# create an instance of DispatchErrors from a dict
dispatch_errors_form_dict = dispatch_errors.from_dict(dispatch_errors_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



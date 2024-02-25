# Dispatch


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_target** | **float** | Dispatch Target for each Registered Facility for each Market | [optional] 
**dispatch_cap** | **float** | Dispatch Cap for each Registered Facility for each Market | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch import Dispatch

# TODO update the JSON string below
json = "{}"
# create an instance of Dispatch from a JSON string
dispatch_instance = Dispatch.from_json(json)
# print the JSON string representation of the object
print Dispatch.to_json()

# convert the object into a dict
dispatch_dict = dispatch_instance.to_dict()
# create an instance of Dispatch from a dict
dispatch_form_dict = dispatch.from_dict(dispatch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



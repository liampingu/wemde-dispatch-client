# DispatchCaps


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**dispatch_cap** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_caps import DispatchCaps

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchCaps from a JSON string
dispatch_caps_instance = DispatchCaps.from_json(json)
# print the JSON string representation of the object
print DispatchCaps.to_json()

# convert the object into a dict
dispatch_caps_dict = dispatch_caps_instance.to_dict()
# create an instance of DispatchCaps from a dict
dispatch_caps_form_dict = dispatch_caps.from_dict(dispatch_caps_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



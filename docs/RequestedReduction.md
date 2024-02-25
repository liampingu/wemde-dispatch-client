# RequestedReduction


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**requested_reduction_value** | **int** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.requested_reduction import RequestedReduction

# TODO update the JSON string below
json = "{}"
# create an instance of RequestedReduction from a JSON string
requested_reduction_instance = RequestedReduction.from_json(json)
# print the JSON string representation of the object
print RequestedReduction.to_json()

# convert the object into a dict
requested_reduction_dict = requested_reduction_instance.to_dict()
# create an instance of RequestedReduction from a dict
requested_reduction_form_dict = requested_reduction.from_dict(requested_reduction_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



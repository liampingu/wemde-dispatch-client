# RocofControlRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**minimum_rocof_control_requirement** | **float** | Required Minimum Rocof Control Requirements | [optional] 
**additional_rocof_control_requirement** | **float** | Required Additional Rocof Control Requirements | [optional] 
**rocof_control_requirement** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.rocof_control_requirements import RocofControlRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of RocofControlRequirements from a JSON string
rocof_control_requirements_instance = RocofControlRequirements.from_json(json)
# print the JSON string representation of the object
print RocofControlRequirements.to_json()

# convert the object into a dict
rocof_control_requirements_dict = rocof_control_requirements_instance.to_dict()
# create an instance of RocofControlRequirements from a dict
rocof_control_requirements_form_dict = rocof_control_requirements.from_dict(rocof_control_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



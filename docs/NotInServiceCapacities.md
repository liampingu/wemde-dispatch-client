# NotInServiceCapacities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**not_in_service_capacity** | **int** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.not_in_service_capacities import NotInServiceCapacities

# TODO update the JSON string below
json = "{}"
# create an instance of NotInServiceCapacities from a JSON string
not_in_service_capacities_instance = NotInServiceCapacities.from_json(json)
# print the JSON string representation of the object
print NotInServiceCapacities.to_json()

# convert the object into a dict
not_in_service_capacities_dict = not_in_service_capacities_instance.to_dict()
# create an instance of NotInServiceCapacities from a dict
not_in_service_capacities_form_dict = not_in_service_capacities.from_dict(not_in_service_capacities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



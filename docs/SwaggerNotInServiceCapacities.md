# SwaggerNotInServiceCapacities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_interval** | **datetime** |  | [optional] 
**not_in_service_capacities** | [**List[NotInServiceCapacities]**](NotInServiceCapacities.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_not_in_service_capacities import SwaggerNotInServiceCapacities

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerNotInServiceCapacities from a JSON string
swagger_not_in_service_capacities_instance = SwaggerNotInServiceCapacities.from_json(json)
# print the JSON string representation of the object
print SwaggerNotInServiceCapacities.to_json()

# convert the object into a dict
swagger_not_in_service_capacities_dict = swagger_not_in_service_capacities_instance.to_dict()
# create an instance of SwaggerNotInServiceCapacities from a dict
swagger_not_in_service_capacities_form_dict = swagger_not_in_service_capacities.from_dict(swagger_not_in_service_capacities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



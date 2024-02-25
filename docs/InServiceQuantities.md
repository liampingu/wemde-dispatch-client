# InServiceQuantities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy_injection_capacity** | **float** | In-Service Energy Injection Capacity in MW | [optional] 
**energy_withdrawal_capacity** | **float** | In-Service Energy Withdrawal Capacity in MW | [optional] 
**contingency_raise** | **float** | In-Service Contingency Raise Capacity in MW | [optional] 
**contingency_lower** | **float** | In-Service Contingency Lower Capacity in MW | [optional] 
**regulation_raise** | **float** | In-Service Regulation Raise Capacity in MW | [optional] 
**regulation_lower** | **float** | In-Service Regulation Lower Capacity in MW | [optional] 
**rocof** | **float** | In-Service Rocof Capacity in MWs | [optional] 

## Example

```python
from wemde_dispatch_client.models.in_service_quantities import InServiceQuantities

# TODO update the JSON string below
json = "{}"
# create an instance of InServiceQuantities from a JSON string
in_service_quantities_instance = InServiceQuantities.from_json(json)
# print the JSON string representation of the object
print InServiceQuantities.to_json()

# convert the object into a dict
in_service_quantities_dict = in_service_quantities_instance.to_dict()
# create an instance of InServiceQuantities from a dict
in_service_quantities_form_dict = in_service_quantities.from_dict(in_service_quantities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



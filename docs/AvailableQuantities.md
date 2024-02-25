# AvailableQuantities


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy_injection_capacity** | **float** | Available Quantity of Energy Injection Capacity in MW | [optional] 
**energy_withdrawal_capacity** | **float** | Available Quantity of Energy Withdrawal Capacity in MW | [optional] 
**contingency_raise** | **float** | Available Quantity of Contingency Raise Capacity in MW | [optional] 
**contingency_lower** | **float** | Available Quantity of Contingency Lower Capacity in MW | [optional] 
**regulation_raise** | **float** | Available Quantity of Regulation Raise Capacity in MW | [optional] 
**regulation_lower** | **float** | Available Quantity of Regulation Lower Capacity in MW | [optional] 
**rocof** | **float** | Available Quantity of Rocof Capacity in MWs | [optional] 

## Example

```python
from wemde_dispatch_client.models.available_quantities import AvailableQuantities

# TODO update the JSON string below
json = "{}"
# create an instance of AvailableQuantities from a JSON string
available_quantities_instance = AvailableQuantities.from_json(json)
# print the JSON string representation of the object
print AvailableQuantities.to_json()

# convert the object into a dict
available_quantities_dict = available_quantities_instance.to_dict()
# create an instance of AvailableQuantities from a dict
available_quantities_form_dict = available_quantities.from_dict(available_quantities_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



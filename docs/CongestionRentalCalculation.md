# CongestionRentalCalculation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_interval** | **datetime** |  | [optional] 
**congestion_rentals** | [**List[CongestionRental]**](CongestionRental.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.congestion_rental_calculation import CongestionRentalCalculation

# TODO update the JSON string below
json = "{}"
# create an instance of CongestionRentalCalculation from a JSON string
congestion_rental_calculation_instance = CongestionRentalCalculation.from_json(json)
# print the JSON string representation of the object
print CongestionRentalCalculation.to_json()

# convert the object into a dict
congestion_rental_calculation_dict = congestion_rental_calculation_instance.to_dict()
# create an instance of CongestionRentalCalculation from a dict
congestion_rental_calculation_form_dict = congestion_rental_calculation.from_dict(congestion_rental_calculation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



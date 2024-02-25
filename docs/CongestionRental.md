# CongestionRental


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**congestion_rental_value** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.congestion_rental import CongestionRental

# TODO update the JSON string below
json = "{}"
# create an instance of CongestionRental from a JSON string
congestion_rental_instance = CongestionRental.from_json(json)
# print the JSON string representation of the object
print CongestionRental.to_json()

# convert the object into a dict
congestion_rental_dict = congestion_rental_instance.to_dict()
# create an instance of CongestionRental from a dict
congestion_rental_form_dict = congestion_rental.from_dict(congestion_rental_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# RegistrationDatum

An array of Registration data for Registered Facilities.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | The Facility that the Registration Data refers to. | 
**nol** | **bool** | The flag that determines whether a Facility is Normally-On Load or not. | 
**facility_standing_data** | [**FacilityStandingData**](FacilityStandingData.md) |  | 

## Example

```python
from wemde_dispatch_client.models.registration_datum import RegistrationDatum

# TODO update the JSON string below
json = "{}"
# create an instance of RegistrationDatum from a JSON string
registration_datum_instance = RegistrationDatum.from_json(json)
# print the JSON string representation of the object
print RegistrationDatum.to_json()

# convert the object into a dict
registration_datum_dict = registration_datum_instance.to_dict()
# create an instance of RegistrationDatum from a dict
registration_datum_form_dict = registration_datum.from_dict(registration_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



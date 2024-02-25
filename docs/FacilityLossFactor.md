# FacilityLossFactor

An array of Facility Loss Factors.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | The Facility that the Facility Loss Factor refers to. | 
**transmission_loss_factor** | **float** | The Transmission Loss Factor of the Facility. This has a default value of 1 if no Transmission Loss Factor is available for the Facility. | [optional] 
**distribution_loss_factor** | **float** | The Distribution Loss Factor of the Facility. This has a default value of 1 if no Distribution Loss Factor is available for the Facility. | [optional] 

## Example

```python
from wemde_dispatch_client.models.facility_loss_factor import FacilityLossFactor

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityLossFactor from a JSON string
facility_loss_factor_instance = FacilityLossFactor.from_json(json)
# print the JSON string representation of the object
print FacilityLossFactor.to_json()

# convert the object into a dict
facility_loss_factor_dict = facility_loss_factor_instance.to_dict()
# create an instance of FacilityLossFactor from a dict
facility_loss_factor_form_dict = facility_loss_factor.from_dict(facility_loss_factor_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



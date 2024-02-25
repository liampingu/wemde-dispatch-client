# FacilityStandingData

Facility Standing data of the Facility.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_registration_status** | **str** | The Facility Registration Status of the Facility. | 
**facility_class** | **str** | The Facility Class where the Facility belongs to. | 
**storage_constraints** | **bool** | The flag that determines if the Facility is subject to WEMDE Storage Constraints or not. | 
**inertia** | **float** | The associated Inertia with the Facility. | 
**tau_factor** | **float** | The associated Tau Factor with the Facility. | 
**unconstrained_forecast_source** | [**UnconstrainedForecastSourceTypes**](UnconstrainedForecastSourceTypes.md) |  | 
**effective_dispatch_interval_from** | **datetime** | Timestamp of when the Registration data is expected to start its effectivity. | 

## Example

```python
from wemde_dispatch_client.models.facility_standing_data import FacilityStandingData

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityStandingData from a JSON string
facility_standing_data_instance = FacilityStandingData.from_json(json)
# print the JSON string representation of the object
print FacilityStandingData.to_json()

# convert the object into a dict
facility_standing_data_dict = facility_standing_data_instance.to_dict()
# create an instance of FacilityStandingData from a dict
facility_standing_data_form_dict = facility_standing_data.from_dict(facility_standing_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



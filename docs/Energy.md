# Energy

Real-Time Market Submissions for Energy the Market Services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | The Market Service the Real-Time Market Submission applies to. | 
**base_forecast_requirement** | **float** | The total forecast requirement for the relevant Market Service (i.e. energy, regulationRaise,regulationLower) coming from Metrix.  This is also known as the Forecast Unscheduled Operational Demand (as per Tranche 6 changes). | 
**override_forecast_requirement** | **float** | The total override forecast requirement used in replacement to baseForecastRequirement. The baseForecastRequirement is overriden when this field has a valid and acceptable numerical value. | 
**facilities** | [**List[EnergyFacility]**](EnergyFacility.md) | An array of Facilities with Real-Time Market Submissions for the relevant Market Service. | 

## Example

```python
from wemde_dispatch_client.models.energy import Energy

# TODO update the JSON string below
json = "{}"
# create an instance of Energy from a JSON string
energy_instance = Energy.from_json(json)
# print the JSON string representation of the object
print Energy.to_json()

# convert the object into a dict
energy_dict = energy_instance.to_dict()
# create an instance of Energy from a dict
energy_form_dict = energy.from_dict(energy_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



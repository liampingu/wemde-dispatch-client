# RegulationLower

Real-Time Market Submissions for Regulation Lower Market Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | The Market Service the Real-Time Market Submission applies to. | 
**base_forecast_requirement** | **float** | The total forecast requirement for the relevant Market Service. | 
**override_forecast_requirement** | **float** | The total override forecast requirement used in replacement to baseForecastRequirement. The baseForecastRequirement is overriden when this field has a valid and acceptable numerical value. | 
**facilities** | [**List[Facility]**](Facility.md) | An array of Facilities with Real-Time Market Submissions for the relevant Market Service. | 

## Example

```python
from wemde_dispatch_client.models.regulation_lower import RegulationLower

# TODO update the JSON string below
json = "{}"
# create an instance of RegulationLower from a JSON string
regulation_lower_instance = RegulationLower.from_json(json)
# print the JSON string representation of the object
print RegulationLower.to_json()

# convert the object into a dict
regulation_lower_dict = regulation_lower_instance.to_dict()
# create an instance of RegulationLower from a dict
regulation_lower_form_dict = regulation_lower.from_dict(regulation_lower_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



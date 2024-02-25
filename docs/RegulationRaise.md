# RegulationRaise

Real-Time Market Submissions for Regulation Raise Market Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | The Market Service the Real-Time Market Submission applies to. | 
**base_forecast_requirement** | **float** | The total forecast requirement for the relevant Market Service. | 
**override_forecast_requirement** | **float** | The total override forecast requirement used in replacement to baseForecastRequirement. The baseForecastRequirement is overriden when this field has a valid and acceptable numerical value. | 
**facilities** | [**List[Facility]**](Facility.md) | An array of Facilities with Real-Time Market Submissions for the relevant Market Service. | 

## Example

```python
from wemde_dispatch_client.models.regulation_raise import RegulationRaise

# TODO update the JSON string below
json = "{}"
# create an instance of RegulationRaise from a JSON string
regulation_raise_instance = RegulationRaise.from_json(json)
# print the JSON string representation of the object
print RegulationRaise.to_json()

# convert the object into a dict
regulation_raise_dict = regulation_raise_instance.to_dict()
# create an instance of RegulationRaise from a dict
regulation_raise_form_dict = regulation_raise.from_dict(regulation_raise_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



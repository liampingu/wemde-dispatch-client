# Rocof

Real-Time Market Submissions for RoCoF Market Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | The Market Service the Real-Time Market Submission applies to. | 
**base_forecast_requirement** | **float** | The total forecast requirement for the relevant Market Service. | 
**override_forecast_requirement** | **float** | The total override forecast requirement used in replacement to baseForecastRequirement. The baseForecastRequirement is overriden when this field has a valid and acceptable numerical value. | 
**facilities** | [**List[Facility]**](Facility.md) | An array of Facilities with Real-Time Market Submissions for the relevant Market Service. | 

## Example

```python
from wemde_dispatch_client.models.rocof import Rocof

# TODO update the JSON string below
json = "{}"
# create an instance of Rocof from a JSON string
rocof_instance = Rocof.from_json(json)
# print the JSON string representation of the object
print Rocof.to_json()

# convert the object into a dict
rocof_dict = rocof_instance.to_dict()
# create an instance of Rocof from a dict
rocof_form_dict = rocof.from_dict(rocof_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



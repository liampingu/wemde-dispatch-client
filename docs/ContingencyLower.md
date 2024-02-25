# ContingencyLower

Real-Time Market Submissions for Contingency Lower Market Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | The Market Service the Real-Time Market Submission applies to. | 
**base_forecast_requirement** | **float** | The total forecast requirement for the relevant Market Service (i.e. energy, regulationRaise, regulationLower) coming from Metrix. This is also known as the Forecast Unscheduled Operational Demand (as per Tranche 6 changes) | 
**override_forecast_requirement** | **float** | The total override forecast requirement used in replacement to baseForecastRequirement. The baseForecastRequirement is overriden when this field has a valid and acceptable numerical value. | 
**facilities** | [**List[Facility]**](Facility.md) | An array of Facilities with Real-Time Market Submissions for the relevant Market Service. | 

## Example

```python
from wemde_dispatch_client.models.contingency_lower import ContingencyLower

# TODO update the JSON string below
json = "{}"
# create an instance of ContingencyLower from a JSON string
contingency_lower_instance = ContingencyLower.from_json(json)
# print the JSON string representation of the object
print ContingencyLower.to_json()

# convert the object into a dict
contingency_lower_dict = contingency_lower_instance.to_dict()
# create an instance of ContingencyLower from a dict
contingency_lower_form_dict = contingency_lower.from_dict(contingency_lower_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



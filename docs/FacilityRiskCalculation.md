# FacilityRiskCalculation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_interval** | **datetime** |  | [optional] 
**facility_risks** | [**List[FacilityRisk]**](FacilityRisk.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.facility_risk_calculation import FacilityRiskCalculation

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityRiskCalculation from a JSON string
facility_risk_calculation_instance = FacilityRiskCalculation.from_json(json)
# print the JSON string representation of the object
print FacilityRiskCalculation.to_json()

# convert the object into a dict
facility_risk_calculation_dict = facility_risk_calculation_instance.to_dict()
# create an instance of FacilityRiskCalculation from a dict
facility_risk_calculation_form_dict = facility_risk_calculation.from_dict(facility_risk_calculation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FacilityRisk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**facility_risk_value** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.facility_risk import FacilityRisk

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityRisk from a JSON string
facility_risk_instance = FacilityRisk.from_json(json)
# print the JSON string representation of the object
print FacilityRisk.to_json()

# convert the object into a dict
facility_risk_dict = facility_risk_instance.to_dict()
# create an instance of FacilityRisk from a dict
facility_risk_form_dict = facility_risk.from_dict(facility_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



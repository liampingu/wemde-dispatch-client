# NetworkRisk


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**network_contingency** | **str** |  | [optional] 
**network_risk_value** | **float** |  | [optional] 
**associated_facility_codes** | **List[str]** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.network_risk import NetworkRisk

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRisk from a JSON string
network_risk_instance = NetworkRisk.from_json(json)
# print the JSON string representation of the object
print NetworkRisk.to_json()

# convert the object into a dict
network_risk_dict = network_risk_instance.to_dict()
# create an instance of NetworkRisk from a dict
network_risk_form_dict = network_risk.from_dict(network_risk_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



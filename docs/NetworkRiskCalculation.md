# NetworkRiskCalculation


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dispatch_interval** | **datetime** |  | [optional] 
**network_risks** | [**List[NetworkRisk]**](NetworkRisk.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.network_risk_calculation import NetworkRiskCalculation

# TODO update the JSON string below
json = "{}"
# create an instance of NetworkRiskCalculation from a JSON string
network_risk_calculation_instance = NetworkRiskCalculation.from_json(json)
# print the JSON string representation of the object
print NetworkRiskCalculation.to_json()

# convert the object into a dict
network_risk_calculation_dict = network_risk_calculation_instance.to_dict()
# create an instance of NetworkRiskCalculation from a dict
network_risk_calculation_form_dict = network_risk_calculation.from_dict(network_risk_calculation_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



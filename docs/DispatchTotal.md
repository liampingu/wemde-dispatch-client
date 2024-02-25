# DispatchTotal


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy_injection_capacity** | **float** | Required Energy Injection Capacity to be dispatched in MW  This is also known as Forecast Operational Demand (as per Tranche 6). | [optional] 
**energy_withdrawal_capacity** | **float** | Required Energy Withdrawal Capacity to be dispatched in MW, including any NOL Facilities  This is also known as Forecast Operational Withdrawal (as per Tranche 6). | [optional] 
**contingency_raise** | **float** | Required Contingency Raise Capacity to be dispatched in MW | [optional] 
**contingency_lower** | **float** | Required Contingency Lower Capacity to be dispatched in MW | [optional] 
**regulation_raise** | **float** | Required Regulation Raise Capacity to be dispatched in MW | [optional] 
**regulation_lower** | **float** | Required Regulation Lower Capacity to be dispatched in MW | [optional] 
**rocof** | **float** | Required Rocof Capacity to be dispatched in MWs | [optional] 

## Example

```python
from wemde_dispatch_client.models.dispatch_total import DispatchTotal

# TODO update the JSON string below
json = "{}"
# create an instance of DispatchTotal from a JSON string
dispatch_total_instance = DispatchTotal.from_json(json)
# print the JSON string representation of the object
print DispatchTotal.to_json()

# convert the object into a dict
dispatch_total_dict = dispatch_total_instance.to_dict()
# create an instance of DispatchTotal from a dict
dispatch_total_form_dict = dispatch_total.from_dict(dispatch_total_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



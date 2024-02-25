# Tranch

An array of tranches. The Price-Quantity pairs and other components submitted by a Market Participant for a Dispatch Interval.The tranche can be one up to 10 tranches.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tranche** | **int** | The specific tranche that encapsulates a single Fuel Type, Quantity, Loss Factor Adjusted Price, Submitted Price, Capacity Type, and Sync Notice Time(if applicable). | 
**fuel_type** | **str** | The Facility&#39;s Fuel Type for a specific tranche. | [optional] 
**quantity** | **float** | The Injection or Withdrawal quantity offered in the tranche in MW. | 
**submitted_price** | **float** | The tranche price in $/MWh. | 
**lfa_price** | **float** | The Loss Factor Adjusted Price in $/MWh. | [optional] 
**capacity_type** | **str** | The Facility&#39;s Capacity Type for a specific tranche. | [optional] 
**notice_time** | **int** | The time in minutes the Facility needs to synchronize and deliver the quantity offered as available capacity. | [optional] 

## Example

```python
from wemde_dispatch_client.models.tranch import Tranch

# TODO update the JSON string below
json = "{}"
# create an instance of Tranch from a JSON string
tranch_instance = Tranch.from_json(json)
# print the JSON string representation of the object
print Tranch.to_json()

# convert the object into a dict
tranch_dict = tranch_instance.to_dict()
# create an instance of Tranch from a dict
tranch_form_dict = tranch.from_dict(tranch_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



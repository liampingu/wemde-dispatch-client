# Facility

An array of Facilities with Real-Time Market Submissions for the relevant Market Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsp_unconstrained_withdrawal_quantity** | **float** |  | 
**dsp_constrained_withdrawal_quantity** | **float** |  | 
**facility_code** | **str** | The Facility to which the Real-Time Market Submission applies to. | 
**submission_id** | **str** | The submission Id associated with the Real-Time Market Submission. | 
**submission_code** | **str** |  | [optional] 
**tranches** | [**List[Tranch]**](Tranch.md) | An array of tranches. The Price-Quantity pairs and other components submitted by a Market Participant for a Dispatch Interval. The tranche can be one up to 10 tranches. | [optional] 
**maximum_capacity** | **float** | Total quantity of the relevant ESS Market Service the Facility is able to deliver for the Dispatch Interval. | 
**enablement_minimum** | **float** | Level of Injection or Withdrawal (in MW) below which no response is specified as being available. | 
**enablement_minimum_value_used** | **float** |  | [optional] 
**low_breakpoint** | **float** | The MW energy dispatch level below which the Facility cannot provide the maximum quantity of that ESS Market Service which it is capable of providing. | 
**low_breakpoint_value_used** | **float** |  | [optional] 
**high_breakpoint** | **float** | The MW energy dispatch level above which the Facility cannot provide the maximum quantity of that ESS Market System Service which it is capable of providing. | 
**high_breakpoint_value_used** | **float** |  | [optional] 
**enablement_maximum** | **float** | The level of Injection or Withdrawal (in MW) above which no response is specified as being available | 
**enablement_maximum_value_used** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.facility import Facility

# TODO update the JSON string below
json = "{}"
# create an instance of Facility from a JSON string
facility_instance = Facility.from_json(json)
# print the JSON string representation of the object
print Facility.to_json()

# convert the object into a dict
facility_dict = facility_instance.to_dict()
# create an instance of Facility from a dict
facility_form_dict = facility.from_dict(facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



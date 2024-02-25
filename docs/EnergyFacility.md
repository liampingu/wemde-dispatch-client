# EnergyFacility

An array of Facilities with Real-Time Market Submissions for the relevant Market Service.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dsp_unconstrained_withdrawal_quantity** | **float** |  | 
**dsp_constrained_withdrawal_quantity** | **float** |  | 
**facility_code** | **str** | The Facility to which the Real-Time Market Submission applies to. | 
**submission_id** | **str** | The submission Id associated with the Real-Time Market Submission. | 
**submission_code** | **str** |  | 
**max_injection_capacity** | **float** | The Maximum Capacity the Facility can deliver in a Dispatch Interval. | [optional] 
**max_withdrawal_capacity** | **float** | The Maximum Capacity the Facility can consume in a Dispatch Interval. | [optional] 
**unconstrained_injection_forecast** | **float** |  | [optional] 
**unconstrained_withdrawal_forecast** | **float** |  | [optional] 
**inflexible_flag** | **bool** | The ability of the Facility to be dispatched in a Dispatch Interval for a fixed level of Injection or Withdrawal specified in the tranche. | [optional] 
**max_upward_ramp_rate** | **float** | The maximum rate of increase in output per minute of the Facility. | [optional] 
**downwards_ramp_rate_value_used** | **float** |  | [optional] 
**max_downward_ramp_rate** | **float** | The maximum rate of reduction in output per minute of a Registered Facility. | [optional] 
**upwards_ramp_rate_value_used** | **float** |  | [optional] 
**fsip** | [**Fsip**](Fsip.md) |  | [optional] 
**tranches** | [**List[Tranch]**](Tranch.md) | An array of tranches. The Price-Quantity pairs and other components submitted by a Market Participant for a Dispatch Interval. The tranche can be one up to 10 tranches. | [optional] 

## Example

```python
from wemde_dispatch_client.models.energy_facility import EnergyFacility

# TODO update the JSON string below
json = "{}"
# create an instance of EnergyFacility from a JSON string
energy_facility_instance = EnergyFacility.from_json(json)
# print the JSON string representation of the object
print EnergyFacility.to_json()

# convert the object into a dict
energy_facility_dict = energy_facility_instance.to_dict()
# create an instance of EnergyFacility from a dict
energy_facility_form_dict = energy_facility.from_dict(energy_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



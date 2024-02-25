# FacilityScheduleDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | Facility Code to which the associated values Facility Schedule Details applies to | [optional] 
**contingency_raise_pf** | **float** | The Contingency Raise Performance Factor of the Facility | [optional] 
**contingency_lower_pf** | **float** | The Contingency Lower Performance Factor of the Facility | [optional] 
**regulation_raise_pf** | **float** | The Regulation Raise Performance Factor of the Facility | [optional] 
**regulation_lower_pf** | **float** | The Regulation Lower Performance Factor of the Facility | [optional] 
**rocof_pf** | **float** | The RoCoF Performance Factor of the Facility | [optional] 
**dispatch_binding_flag** | **bool** | Determines if the Semi-Scheduled Facility&#39;s Dispatch Cap is Binding due to a constraint. | [optional] 
**contingency** | **float** | Solved Contingency level associated with the Facility | [optional] 
**initial_mw** | **float** | Initial MW of the Facility based from the SCADA | [optional] 
**fast_start_flag** | **bool** |  | [optional] 
**fast_start_initial_mode_time** | **int** | Gets or sets the Initial Fast Start Mode | [optional] 
**fast_start_initial_mode** | **int** | Gets or sets the Initial Fast Start Mode | [optional] 
**what_if_initial_mw** | **float** | WhatIf Initial MW of the Facility if an Intervention Constraint is present. If none, the value is the same with the Initial MW. | [optional] 
**fast_start_target_mode** | **int** | Fast-Start Current Mode of the Facility in the current Solution | [optional] 
**fast_start_target_mode_time** | **int** | Fast-Start Current Mode Time of the Facility in the current Solution | [optional] 
**estimated_fcess_uplift_payment** | **float** |  | [optional] 
**nol_demand** | **float** |  | [optional] 
**congestion_rental** | **float** |  | [optional] 
**facility_risk** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.facility_schedule_detail import FacilityScheduleDetail

# TODO update the JSON string below
json = "{}"
# create an instance of FacilityScheduleDetail from a JSON string
facility_schedule_detail_instance = FacilityScheduleDetail.from_json(json)
# print the JSON string representation of the object
print FacilityScheduleDetail.to_json()

# convert the object into a dict
facility_schedule_detail_dict = facility_schedule_detail_instance.to_dict()
# create an instance of FacilityScheduleDetail from a dict
facility_schedule_detail_form_dict = facility_schedule_detail.from_dict(facility_schedule_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



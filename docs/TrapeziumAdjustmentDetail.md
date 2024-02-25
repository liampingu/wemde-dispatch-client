# TrapeziumAdjustmentDetail


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | Facility Code to which the associated values of Trapezium Adjustments applies to | [optional] 
**enablement_minimum_value_used** | **float** | Enablement Minimum Value used in the Dispatch Engine | [optional] 
**low_breakpoint_value_used** | **float** | Low Breakpoint Value used in the Dispatch Engine | [optional] 
**high_breakpoint_value_used** | **float** | High Breakpoint Value used in the Dispatch Engine | [optional] 
**enablement_maximum_value_used** | **float** | Enablement Maximum Value used in the Dispatch Engine | [optional] 
**downwards_ramp_rate_value_used** | **float** | Downwards Ramp Rate Value used in the Dispatch Engine | [optional] 
**upwards_ramp_rate_value_used** | **float** | Upwards Ramp Rate Value used in the Dispatch Engine | [optional] 

## Example

```python
from wemde_dispatch_client.models.trapezium_adjustment_detail import TrapeziumAdjustmentDetail

# TODO update the JSON string below
json = "{}"
# create an instance of TrapeziumAdjustmentDetail from a JSON string
trapezium_adjustment_detail_instance = TrapeziumAdjustmentDetail.from_json(json)
# print the JSON string representation of the object
print TrapeziumAdjustmentDetail.to_json()

# convert the object into a dict
trapezium_adjustment_detail_dict = trapezium_adjustment_detail_instance.to_dict()
# create an instance of TrapeziumAdjustmentDetail from a dict
trapezium_adjustment_detail_form_dict = trapezium_adjustment_detail.from_dict(trapezium_adjustment_detail_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



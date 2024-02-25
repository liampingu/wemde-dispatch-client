# TrapeziumAdjustment


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | Market Service for which the Trapezium Adjustments in a Semi-Scheduled Facility applies to | [optional] 
**trapezium_adjustment_details** | [**List[TrapeziumAdjustmentDetail]**](TrapeziumAdjustmentDetail.md) | An array of Trapezium Adjustment Details that determines the final value of Enablement Minimum, Enablement Maximum, Low Breakpoint, High Breakpoint, and Ramp-Rates used in a relevant Market Service for each Facility | [optional] 

## Example

```python
from wemde_dispatch_client.models.trapezium_adjustment import TrapeziumAdjustment

# TODO update the JSON string below
json = "{}"
# create an instance of TrapeziumAdjustment from a JSON string
trapezium_adjustment_instance = TrapeziumAdjustment.from_json(json)
# print the JSON string representation of the object
print TrapeziumAdjustment.to_json()

# convert the object into a dict
trapezium_adjustment_dict = trapezium_adjustment_instance.to_dict()
# create an instance of TrapeziumAdjustment from a dict
trapezium_adjustment_form_dict = trapezium_adjustment.from_dict(trapezium_adjustment_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



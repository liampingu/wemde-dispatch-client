# UnconstrainedForecastDatum


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**unconstrained_injection_forecast_mw** | **float** |  | [optional] 
**unconstrained_withdrawal_forecast_mw** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.unconstrained_forecast_datum import UnconstrainedForecastDatum

# TODO update the JSON string below
json = "{}"
# create an instance of UnconstrainedForecastDatum from a JSON string
unconstrained_forecast_datum_instance = UnconstrainedForecastDatum.from_json(json)
# print the JSON string representation of the object
print UnconstrainedForecastDatum.to_json()

# convert the object into a dict
unconstrained_forecast_datum_dict = unconstrained_forecast_datum_instance.to_dict()
# create an instance of UnconstrainedForecastDatum from a dict
unconstrained_forecast_datum_form_dict = unconstrained_forecast_datum.from_dict(unconstrained_forecast_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



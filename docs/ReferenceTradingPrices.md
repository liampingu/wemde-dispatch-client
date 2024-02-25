# ReferenceTradingPrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_interval** | **datetime** |  | [optional] 
**reference_trading_price** | **float** |  | [optional] 
**is_published** | **bool** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.reference_trading_prices import ReferenceTradingPrices

# TODO update the JSON string below
json = "{}"
# create an instance of ReferenceTradingPrices from a JSON string
reference_trading_prices_instance = ReferenceTradingPrices.from_json(json)
# print the JSON string representation of the object
print ReferenceTradingPrices.to_json()

# convert the object into a dict
reference_trading_prices_dict = reference_trading_prices_instance.to_dict()
# create an instance of ReferenceTradingPrices from a dict
reference_trading_prices_form_dict = reference_trading_prices.from_dict(reference_trading_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



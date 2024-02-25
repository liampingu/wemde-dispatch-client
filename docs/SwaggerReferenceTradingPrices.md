# SwaggerReferenceTradingPrices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_day** | **str** |  | [optional] 
**reference_trading_prices** | [**List[ReferenceTradingPrices]**](ReferenceTradingPrices.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_reference_trading_prices import SwaggerReferenceTradingPrices

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerReferenceTradingPrices from a JSON string
swagger_reference_trading_prices_instance = SwaggerReferenceTradingPrices.from_json(json)
# print the JSON string representation of the object
print SwaggerReferenceTradingPrices.to_json()

# convert the object into a dict
swagger_reference_trading_prices_dict = swagger_reference_trading_prices_instance.to_dict()
# create an instance of SwaggerReferenceTradingPrices from a dict
swagger_reference_trading_prices_form_dict = swagger_reference_trading_prices.from_dict(swagger_reference_trading_prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



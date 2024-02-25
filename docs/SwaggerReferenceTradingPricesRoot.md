# SwaggerReferenceTradingPricesRoot


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**SwaggerReferenceTradingPrices**](SwaggerReferenceTradingPrices.md) |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_reference_trading_prices_root import SwaggerReferenceTradingPricesRoot

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerReferenceTradingPricesRoot from a JSON string
swagger_reference_trading_prices_root_instance = SwaggerReferenceTradingPricesRoot.from_json(json)
# print the JSON string representation of the object
print SwaggerReferenceTradingPricesRoot.to_json()

# convert the object into a dict
swagger_reference_trading_prices_root_dict = swagger_reference_trading_prices_root_instance.to_dict()
# create an instance of SwaggerReferenceTradingPricesRoot from a dict
swagger_reference_trading_prices_root_form_dict = swagger_reference_trading_prices_root.from_dict(swagger_reference_trading_prices_root_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



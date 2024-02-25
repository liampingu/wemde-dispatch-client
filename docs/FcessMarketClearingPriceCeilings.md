# FcessMarketClearingPriceCeilings


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**fcess_market_service** | **str** |  | [optional] 
**price_ceiling** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.fcess_market_clearing_price_ceilings import FcessMarketClearingPriceCeilings

# TODO update the JSON string below
json = "{}"
# create an instance of FcessMarketClearingPriceCeilings from a JSON string
fcess_market_clearing_price_ceilings_instance = FcessMarketClearingPriceCeilings.from_json(json)
# print the JSON string representation of the object
print FcessMarketClearingPriceCeilings.to_json()

# convert the object into a dict
fcess_market_clearing_price_ceilings_dict = fcess_market_clearing_price_ceilings_instance.to_dict()
# create an instance of FcessMarketClearingPriceCeilings from a dict
fcess_market_clearing_price_ceilings_form_dict = fcess_market_clearing_price_ceilings.from_dict(fcess_market_clearing_price_ceilings_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



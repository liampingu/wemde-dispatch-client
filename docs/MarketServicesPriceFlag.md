# MarketServicesPriceFlag

 The Market Services Price flags that determine if the price for a Market Service must be set to the Market Price  Cap, overriding the original price determined as part of the solve.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy_price_at_cap** | **bool** | The flag that determines if the Energy Market Service must be set to the Market Price Cap for the Dispatch Interval. | 
**regulation_raise_price_at_cap** | **bool** | The flag that determines if the Regulation Raise Market Service must be set to the Market Price Cap for the Dispatch Interval. | 
**regulation_lower_price_at_cap** | **bool** | The flag that determines if the Regulation Lower Market Service must be set to the Market Price Cap for the Dispatch Interval. | 
**contingency_lower_price_at_cap** | **bool** | The flag that determines if the Contingency Lower Market Service must be set to the Market Price Cap for the Dispatch Interval. | 
**contingency_raise_price_at_cap** | **bool** | The flag that determines if the Contingency Raise Market Service must be set to the Market Price Cap for the Dispatch Interval. | 
**rocof_price_at_cap** | **bool** | The flag that determines if the RoCoF Market Service must be set to the Market Price Cap for the Dispatch Interval. | 

## Example

```python
from wemde_dispatch_client.models.market_services_price_flag import MarketServicesPriceFlag

# TODO update the JSON string below
json = "{}"
# create an instance of MarketServicesPriceFlag from a JSON string
market_services_price_flag_instance = MarketServicesPriceFlag.from_json(json)
# print the JSON string representation of the object
print MarketServicesPriceFlag.to_json()

# convert the object into a dict
market_services_price_flag_dict = market_services_price_flag_instance.to_dict()
# create an instance of MarketServicesPriceFlag from a dict
market_services_price_flag_form_dict = market_services_price_flag.from_dict(market_services_price_flag_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



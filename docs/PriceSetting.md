# PriceSetting


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | Market Service the Facility is trading into. | [optional] 
**is_market_service_capped** | **bool** | Facility that set the Market Clearing Price | [optional] 
**contributions** | [**List[PriceSettingContribution]**](PriceSettingContribution.md) | Details of contributions for each variable | [optional] 

## Example

```python
from wemde_dispatch_client.models.price_setting import PriceSetting

# TODO update the JSON string below
json = "{}"
# create an instance of PriceSetting from a JSON string
price_setting_instance = PriceSetting.from_json(json)
# print the JSON string representation of the object
print PriceSetting.to_json()

# convert the object into a dict
price_setting_dict = price_setting_instance.to_dict()
# create an instance of PriceSetting from a dict
price_setting_form_dict = price_setting.from_dict(price_setting_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# MarketSubCategory


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**market_service** | **str** | The Market Service the Real-Time Market Submission applies to. | [optional] 
**base_forecast_requirement** | **float** | The total forecast requirement for the relevant Market Service. | [optional] 
**override_forecast_requirement** | **float** | The total override forecast requirement used in replacement to baseForecastRequirement. The  baseForecastRequirement is overriden when this field has a valid and acceptable numerical value. | [optional] 

## Example

```python
from wemde_dispatch_client.models.market_sub_category import MarketSubCategory

# TODO update the JSON string below
json = "{}"
# create an instance of MarketSubCategory from a JSON string
market_sub_category_instance = MarketSubCategory.from_json(json)
# print the JSON string representation of the object
print MarketSubCategory.to_json()

# convert the object into a dict
market_sub_category_dict = market_sub_category_instance.to_dict()
# create an instance of MarketSubCategory from a dict
market_sub_category_form_dict = market_sub_category.from_dict(market_sub_category_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



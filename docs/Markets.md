# Markets


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy** | [**MarketSubCategory**](MarketSubCategory.md) |  | [optional] 
**regulation_raise** | [**MarketSubCategory**](MarketSubCategory.md) |  | [optional] 
**regulation_lower** | [**MarketSubCategory**](MarketSubCategory.md) |  | [optional] 
**contingency_raise** | [**MarketSubCategory**](MarketSubCategory.md) |  | [optional] 
**contingency_lower** | [**MarketSubCategory**](MarketSubCategory.md) |  | [optional] 
**rocof** | [**MarketSubCategory**](MarketSubCategory.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.markets import Markets

# TODO update the JSON string below
json = "{}"
# create an instance of Markets from a JSON string
markets_instance = Markets.from_json(json)
# print the JSON string representation of the object
print Markets.to_json()

# convert the object into a dict
markets_dict = markets_instance.to_dict()
# create an instance of Markets from a dict
markets_form_dict = markets.from_dict(markets_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



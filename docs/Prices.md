# Prices


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy** | **float** | Market Clearing Price for Energy. | [optional] 
**contingency_lower** | **float** | Market Clearing Price for Contingency Lower. | [optional] 
**regulation_raise** | **float** | Market Clearing Price for Regulation Raise. | [optional] 
**regulation_lower** | **float** | Market Clearing Price for Regulation Lower. | [optional] 
**rocof** | **float** | Market Clearing Price for Rocof. | [optional] 
**contingency_raise** | **float** | Market Clearing Price for Contingency Raise. | [optional] 

## Example

```python
from wemde_dispatch_client.models.prices import Prices

# TODO update the JSON string below
json = "{}"
# create an instance of Prices from a JSON string
prices_instance = Prices.from_json(json)
# print the JSON string representation of the object
print Prices.to_json()

# convert the object into a dict
prices_dict = prices_instance.to_dict()
# create an instance of Prices from a dict
prices_form_dict = prices.from_dict(prices_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



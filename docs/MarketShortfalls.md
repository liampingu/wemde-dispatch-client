# MarketShortfalls


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy_deficit** | **float** | Amount of Energy shortfall in MW | [optional] 
**regulation_raise_deficit** | **float** | Amount of Regulation Raise shortfall in MW | [optional] 
**regulation_lower_deficit** | **float** | Amount of Regulation Lower shortfall in MW | [optional] 
**contingency_raise_deficit** | **float** | Amount of Contingency Raise shortfall in MW | [optional] 
**contingency_lower_deficit** | **float** | Amount of Contingency Lower shortfall in MW | [optional] 
**rocof_deficit** | **float** | Amount of Rocof shortfall in MW | [optional] 

## Example

```python
from wemde_dispatch_client.models.market_shortfalls import MarketShortfalls

# TODO update the JSON string below
json = "{}"
# create an instance of MarketShortfalls from a JSON string
market_shortfalls_instance = MarketShortfalls.from_json(json)
# print the JSON string representation of the object
print MarketShortfalls.to_json()

# convert the object into a dict
market_shortfalls_dict = market_shortfalls_instance.to_dict()
# create an instance of MarketShortfalls from a dict
market_shortfalls_form_dict = market_shortfalls.from_dict(market_shortfalls_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



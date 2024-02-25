# Market

Real-Time Market Submissions for all the Market Services.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy** | [**Energy**](Energy.md) |  | [optional] 
**regulation_raise** | [**RegulationRaise**](RegulationRaise.md) |  | [optional] 
**regulation_lower** | [**RegulationLower**](RegulationLower.md) |  | [optional] 
**contingency_raise** | [**ContingencyRaise**](ContingencyRaise.md) |  | [optional] 
**contingency_lower** | [**ContingencyLower**](ContingencyLower.md) |  | [optional] 
**rocof** | [**Rocof**](Rocof.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.market import Market

# TODO update the JSON string below
json = "{}"
# create an instance of Market from a JSON string
market_instance = Market.from_json(json)
# print the JSON string representation of the object
print Market.to_json()

# convert the object into a dict
market_dict = market_instance.to_dict()
# create an instance of Market from a dict
market_form_dict = market.from_dict(market_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



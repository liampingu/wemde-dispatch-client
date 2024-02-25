# MarketServiceRequirements


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**energy** | **float** |  | [optional] 
**regulation_raise** | **float** |  | [optional] 
**regulation_lower** | **float** |  | [optional] 
**contingency_raise** | **float** |  | [optional] 
**contingency_lower** | **float** |  | [optional] 
**rocof** | **float** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.market_service_requirements import MarketServiceRequirements

# TODO update the JSON string below
json = "{}"
# create an instance of MarketServiceRequirements from a JSON string
market_service_requirements_instance = MarketServiceRequirements.from_json(json)
# print the JSON string representation of the object
print MarketServiceRequirements.to_json()

# convert the object into a dict
market_service_requirements_dict = market_service_requirements_instance.to_dict()
# create an instance of MarketServiceRequirements from a dict
market_service_requirements_form_dict = market_service_requirements.from_dict(market_service_requirements_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



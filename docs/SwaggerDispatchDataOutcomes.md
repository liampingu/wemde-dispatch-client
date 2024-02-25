# SwaggerDispatchDataOutcomes


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**DispatchDataOutcomesData**](DispatchDataOutcomesData.md) |  | [optional] 
**errors** | **List[object]** |  | [optional] 
**warnings** | **List[object]** |  | [optional] 
**infos** | **List[object]** |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dispatch_data_outcomes import SwaggerDispatchDataOutcomes

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDispatchDataOutcomes from a JSON string
swagger_dispatch_data_outcomes_instance = SwaggerDispatchDataOutcomes.from_json(json)
# print the JSON string representation of the object
print SwaggerDispatchDataOutcomes.to_json()

# convert the object into a dict
swagger_dispatch_data_outcomes_dict = swagger_dispatch_data_outcomes_instance.to_dict()
# create an instance of SwaggerDispatchDataOutcomes from a dict
swagger_dispatch_data_outcomes_form_dict = swagger_dispatch_data_outcomes.from_dict(swagger_dispatch_data_outcomes_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



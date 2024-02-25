# SwaggerDispatchSummaryData


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**errors** | **List[object]** |  | [optional] 
**warnings** | **List[object]** |  | [optional] 
**infos** | **List[object]** |  | [optional] 
**transaction_id** | **str** |  | [optional] 
**data** | [**DispatchInstructionsSummaryData**](DispatchInstructionsSummaryData.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_dispatch_summary_data import SwaggerDispatchSummaryData

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerDispatchSummaryData from a JSON string
swagger_dispatch_summary_data_instance = SwaggerDispatchSummaryData.from_json(json)
# print the JSON string representation of the object
print SwaggerDispatchSummaryData.to_json()

# convert the object into a dict
swagger_dispatch_summary_data_dict = swagger_dispatch_summary_data_instance.to_dict()
# create an instance of SwaggerDispatchSummaryData from a dict
swagger_dispatch_summary_data_form_dict = swagger_dispatch_summary_data.from_dict(swagger_dispatch_summary_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



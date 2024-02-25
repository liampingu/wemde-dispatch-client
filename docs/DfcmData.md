# DfcmData

Dynamic Frequency Control Model data used in the Dispatch Engine calculations.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**dfcm_id** | **str** | The Id of the DFCM data. | [optional] 
**dfcm_schema_version** | **str** | The version of the DFCM data. | [optional] 
**frequency_limits** | [**FrequencyLimits**](FrequencyLimits.md) |  | [optional] 
**dfcm_validation_details** | [**DfcmValidationDetails**](DfcmValidationDetails.md) |  | [optional] 
**tau_valuesfor_cr_performance_factors** | **List[float]** | An array of tau values for Contingency Raise Performance Factors. | [optional] 

## Example

```python
from wemde_dispatch_client.models.dfcm_data import DfcmData

# TODO update the JSON string below
json = "{}"
# create an instance of DfcmData from a JSON string
dfcm_data_instance = DfcmData.from_json(json)
# print the JSON string representation of the object
print DfcmData.to_json()

# convert the object into a dict
dfcm_data_dict = dfcm_data_instance.to_dict()
# create an instance of DfcmData from a dict
dfcm_data_form_dict = dfcm_data.from_dict(dfcm_data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



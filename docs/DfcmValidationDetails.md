# DfcmValidationDetails

The values used for the validation of the DFCM data inputs.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**inertia_range_minimum** | **float** | The minimum Inertia limit in the DFCM data table. | [optional] 
**inertia_range_maximum** | **float** | The maximum Inertia limit in the DFCM data table. | [optional] 
**inertia_range_step** | **float** | The required step size of Inertia values from the minimum to the maximum Inertia value. | [optional] 
**largest_contingency_size_minimum** | **float** | The minimum Largest Contingency Size limit in the DFCM data table. | [optional] 
**largest_contingency_size_maximum** | **float** | The maximum Largest Contingency Size limit in the DFCM data table. | [optional] 
**largest_contingency_size_step** | **float** |  The required step size of Largest Contingency Size values from the minimum to the maximum Largest  Contingency Size value. | [optional] 

## Example

```python
from wemde_dispatch_client.models.dfcm_validation_details import DfcmValidationDetails

# TODO update the JSON string below
json = "{}"
# create an instance of DfcmValidationDetails from a JSON string
dfcm_validation_details_instance = DfcmValidationDetails.from_json(json)
# print the JSON string representation of the object
print DfcmValidationDetails.to_json()

# convert the object into a dict
dfcm_validation_details_dict = dfcm_validation_details_instance.to_dict()
# create an instance of DfcmValidationDetails from a dict
dfcm_validation_details_form_dict = dfcm_validation_details.from_dict(dfcm_validation_details_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# FrequencyLimits

The frequency limits associated with the DFCM data.

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**rocof_max** | **float** | The maximum RoCoF frequency limit. | 
**rocof_min** | **float** | The minimum RoCoF frequency limit. | 
**fmin** | **float** | The minimum frequency limit. | 
**fmax** | **float** | The maximum frequency limit. | 
**fss** | **float** | The frequency steady-state limit. | 

## Example

```python
from wemde_dispatch_client.models.frequency_limits import FrequencyLimits

# TODO update the JSON string below
json = "{}"
# create an instance of FrequencyLimits from a JSON string
frequency_limits_instance = FrequencyLimits.from_json(json)
# print the JSON string representation of the object
print FrequencyLimits.to_json()

# convert the object into a dict
frequency_limits_dict = frequency_limits_instance.to_dict()
# create an instance of FrequencyLimits from a dict
frequency_limits_form_dict = frequency_limits.from_dict(frequency_limits_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



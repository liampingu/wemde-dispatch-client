# Fsip


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**t1** | **float** | The time it takes for the Facility to synchronise after receiving dispatch instruction. | 
**t2** | **float** | The time it takes for the Facility to reach minimum loading. | 
**t3** | **float** | The time required for the Facility to operate at or beyond the minimum loading. | 
**t4** | **float** | The time required for the Facility to shut down from minimum loading. | 
**minimum_load** | **float** | The quantity (in MW) of Injection or Withdrawal that the Facility must be operated at or beyond during the period t3. | 

## Example

```python
from wemde_dispatch_client.models.fsip import Fsip

# TODO update the JSON string below
json = "{}"
# create an instance of Fsip from a JSON string
fsip_instance = Fsip.from_json(json)
# print the JSON string representation of the object
print Fsip.to_json()

# convert the object into a dict
fsip_dict = fsip_instance.to_dict()
# create an instance of Fsip from a dict
fsip_form_dict = fsip.from_dict(fsip_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Scadum

 Real-Time inputs used in network constraint equations and Dispatch Engine calculations.  An array of data point inputs and its associated properties.  GSS

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**tag** | **str** | Name of the tag that corresponds to a data point. | 
**value** | **str** | Value of the data point | 
**value_data_type** | **str** | Data type identifer of the data point&#39;s value. | 
**quality_flag** | **str** | Status of the returned data point&#39;s value. | 
**data_source** | **str** | Source identifier of the data point value. Data is sourced from scada. | 
**as_at_time_stamp** | **datetime** | Timestamp when the data point was retrieved. | 

## Example

```python
from wemde_dispatch_client.models.scadum import Scadum

# TODO update the JSON string below
json = "{}"
# create an instance of Scadum from a JSON string
scadum_instance = Scadum.from_json(json)
# print the JSON string representation of the object
print Scadum.to_json()

# convert the object into a dict
scadum_dict = scadum_instance.to_dict()
# create an instance of Scadum from a dict
scadum_form_dict = scadum.from_dict(scadum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



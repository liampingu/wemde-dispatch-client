# RcmDatum

An array of Relevant Demands and Reserve Capacity Obligation Quantities from the Reserve Capacity Mechanism(RCM).

## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** | The DSP Facility that the Relevant Demand and Reserve Capacity Obligation Quantity refers to. | 
**rcoq** | **float** | The Reserve Capacity Obligation Quantity of the Facility. | 

## Example

```python
from wemde_dispatch_client.models.rcm_datum import RcmDatum

# TODO update the JSON string below
json = "{}"
# create an instance of RcmDatum from a JSON string
rcm_datum_instance = RcmDatum.from_json(json)
# print the JSON string representation of the object
print RcmDatum.to_json()

# convert the object into a dict
rcm_datum_dict = rcm_datum_instance.to_dict()
# create an instance of RcmDatum from a dict
rcm_datum_form_dict = rcm_datum.from_dict(rcm_datum_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



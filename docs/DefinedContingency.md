# DefinedContingency


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**id** | **str** | Id of the Defined Contingency | [optional] 
**value_of_contingency** | **float** | Resolved value of the Defined Contingency | [optional] 

## Example

```python
from wemde_dispatch_client.models.defined_contingency import DefinedContingency

# TODO update the JSON string below
json = "{}"
# create an instance of DefinedContingency from a JSON string
defined_contingency_instance = DefinedContingency.from_json(json)
# print the JSON string representation of the object
print DefinedContingency.to_json()

# convert the object into a dict
defined_contingency_dict = defined_contingency_instance.to_dict()
# create an instance of DefinedContingency from a dict
defined_contingency_form_dict = defined_contingency.from_dict(defined_contingency_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



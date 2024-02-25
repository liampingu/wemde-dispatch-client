# SlackVariable


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**variable** | **str** | Variable name of the slack | [optional] 
**value** | **float** | Value of the slack | [optional] 

## Example

```python
from wemde_dispatch_client.models.slack_variable import SlackVariable

# TODO update the JSON string below
json = "{}"
# create an instance of SlackVariable from a JSON string
slack_variable_instance = SlackVariable.from_json(json)
# print the JSON string representation of the object
print SlackVariable.to_json()

# convert the object into a dict
slack_variable_dict = slack_variable_instance.to_dict()
# create an instance of SlackVariable from a dict
slack_variable_form_dict = slack_variable.from_dict(slack_variable_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



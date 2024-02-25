# PriceSettingContribution


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**contributing_variable** | **str** | Xpress variable that moves due to change on the constraint RHS | [optional] 
**by_how_much** | **float** | the amount of movement from the contributingVariable due to the change on the constraint RHS | [optional] 
**objective_coefficient** | **float** | coefficient of the contributingVariable in the objective function | [optional] 

## Example

```python
from wemde_dispatch_client.models.price_setting_contribution import PriceSettingContribution

# TODO update the JSON string below
json = "{}"
# create an instance of PriceSettingContribution from a JSON string
price_setting_contribution_instance = PriceSettingContribution.from_json(json)
# print the JSON string representation of the object
print PriceSettingContribution.to_json()

# convert the object into a dict
price_setting_contribution_dict = price_setting_contribution_instance.to_dict()
# create an instance of PriceSettingContribution from a dict
price_setting_contribution_form_dict = price_setting_contribution.from_dict(price_setting_contribution_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



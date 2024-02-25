# SwaggerTradingDayReport


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**data** | [**TradingDayReports**](TradingDayReports.md) |  | [optional] 
**transaction_id** | **str** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_trading_day_report import SwaggerTradingDayReport

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerTradingDayReport from a JSON string
swagger_trading_day_report_instance = SwaggerTradingDayReport.from_json(json)
# print the JSON string representation of the object
print SwaggerTradingDayReport.to_json()

# convert the object into a dict
swagger_trading_day_report_dict = swagger_trading_day_report_instance.to_dict()
# create an instance of SwaggerTradingDayReport from a dict
swagger_trading_day_report_form_dict = swagger_trading_day_report.from_dict(swagger_trading_day_report_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



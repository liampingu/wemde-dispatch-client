# SwaggerTradingDayReportFacility


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**facility_code** | **str** |  | [optional] 
**energy_uplift_price** | **float** |  | [optional] 
**uplift_mispricing_trigger** | **int** |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.swagger_trading_day_report_facility import SwaggerTradingDayReportFacility

# TODO update the JSON string below
json = "{}"
# create an instance of SwaggerTradingDayReportFacility from a JSON string
swagger_trading_day_report_facility_instance = SwaggerTradingDayReportFacility.from_json(json)
# print the JSON string representation of the object
print SwaggerTradingDayReportFacility.to_json()

# convert the object into a dict
swagger_trading_day_report_facility_dict = swagger_trading_day_report_facility_instance.to_dict()
# create an instance of SwaggerTradingDayReportFacility from a dict
swagger_trading_day_report_facility_form_dict = swagger_trading_day_report_facility.from_dict(swagger_trading_day_report_facility_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



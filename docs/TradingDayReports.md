# TradingDayReports


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**trading_day** | **datetime** |  | [optional] 
**dsp_reduction_instructions** | [**List[DspReductionInstruction]**](DspReductionInstruction.md) |  | [optional] 
**congestion_rental_calculations** | [**List[CongestionRentalCalculation]**](CongestionRentalCalculation.md) |  | [optional] 
**facility_risk_calculations** | [**List[FacilityRiskCalculation]**](FacilityRiskCalculation.md) |  | [optional] 
**network_risk_calculations** | [**List[NetworkRiskCalculation]**](NetworkRiskCalculation.md) |  | [optional] 
**energy_uplift_prices_and_uplift_payment_mispricing_triggers** | [**List[EnergyUpliftPricesAndUpliftPaymentMispricingTrigger]**](EnergyUpliftPricesAndUpliftPaymentMispricingTrigger.md) |  | [optional] 

## Example

```python
from wemde_dispatch_client.models.trading_day_reports import TradingDayReports

# TODO update the JSON string below
json = "{}"
# create an instance of TradingDayReports from a JSON string
trading_day_reports_instance = TradingDayReports.from_json(json)
# print the JSON string representation of the object
print TradingDayReports.to_json()

# convert the object into a dict
trading_day_reports_dict = trading_day_reports_instance.to_dict()
# create an instance of TradingDayReports from a dict
trading_day_reports_form_dict = trading_day_reports.from_dict(trading_day_reports_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



# Data


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario** | **str** |  | [optional] 
**dispatch_interval** | **datetime** | Target Dispatch Interval for which the relevant Market Schedules are being calculated. | 
**parameters** | [**List[Parameter]**](Parameter.md) | An array of the Dispatch Solver Parameters for each Dispatch Interval or Trading Interval. | 
**constraint_violation_parameters** | [**List[ConstraintViolationParameter]**](ConstraintViolationParameter.md) | An array of the Constraint Violation Parameters for each Dispatch Interval or Trading Interval. Refer to the XXX procedure | 
**scada** | [**List[Scadum]**](Scadum.md) | Real-Time inputs used in network constraint equations and Dispatch Engine calculations.  An array of data point inputs and its associated properties. | 
**constraint_look_up** | [**ConstraintLookUp**](ConstraintLookUp.md) |  | [optional] 
**constraints** | [**Constraints**](Constraints.md) |  | [optional] 
**dfcm_data** | [**DfcmData**](DfcmData.md) |  | [optional] 
**unconstrained_forecast** | [**List[UnconstrainedForecastDatum]**](UnconstrainedForecastDatum.md) |  | [optional] 
**registration_data** | [**List[RegistrationDatum]**](RegistrationDatum.md) | An array of Registration data for Registered Facilities. | 
**facility_loss_factors** | [**List[FacilityLossFactor]**](FacilityLossFactor.md) | An array of Facility Loss Factors. | 
**rcm_data** | [**List[RcmDatum]**](RcmDatum.md) | An array of Relevant Demands and Reserve Capacity Obligation Quantities from the Reserve Capacity Mechanism 463 (RCM). | [optional] 
**market_services_price_flag** | [**MarketServicesPriceFlag**](MarketServicesPriceFlag.md) |  | [optional] 
**markets** | [**Market**](Market.md) |  | 

## Example

```python
from wemde_dispatch_client.models.data import Data

# TODO update the JSON string below
json = "{}"
# create an instance of Data from a JSON string
data_instance = Data.from_json(json)
# print the JSON string representation of the object
print Data.to_json()

# convert the object into a dict
data_dict = data_instance.to_dict()
# create an instance of Data from a dict
data_form_dict = data.from_dict(data_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



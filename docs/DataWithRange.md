# DataWithRange


## Properties

Name | Type | Description | Notes
------------ | ------------- | ------------- | -------------
**scenario** | **str** |  | [optional] 
**dispatch_interval** | **datetime** | Target Dispatch Interval for which the relevant Market Schedules are being calculated. | 
**primary_dispatch_interval** | **datetime** | Timestamp of the Primary Dispatch Interval in the series of Case Files generated in a run of a specific 25 Dispatch Run Type. | [optional] 
**parameters** | [**List[Parameter]**](Parameter.md) | An array of the Dispatch Solver Parameters for each Dispatch Interval or Trading Interval. | 
**constraint_violation_parameters** | [**List[ConstraintViolationParameter]**](ConstraintViolationParameter.md) | An array of the Constraint Violation Parameters for each Dispatch Interval or Trading Interval. Refer to the XXX procedure | 
**scada** | [**List[Scadum]**](Scadum.md) | Real-Time inputs used in network constraint equations and Dispatch Engine calculations.  An array of data point inputs and its associated properties. | 
**constraint_look_up** | [**ConstraintLookUp**](ConstraintLookUp.md) |  | [optional] 
**constraints** | [**Constraints**](Constraints.md) |  | [optional] 
**dfcm_data** | [**DfcmData**](DfcmData.md) |  | [optional] 
**registration_data** | [**List[RegistrationDatum]**](RegistrationDatum.md) | An array of Registration data for Registered Facilities. | 
**facility_loss_factors** | [**List[FacilityLossFactor]**](FacilityLossFactor.md) | An array of Facility Loss Factors. | 
**uigf** | [**List[Uigf]**](Uigf.md) | An array of Unconstrained Intermittent Generation Forecasts. | [optional] 
**rcm_data** | [**List[RcmDatum]**](RcmDatum.md) | An array of Relevant Demands and Reserve Capacity Obligation Quantities from the Reserve Capacity Mechanism 463 (RCM). | [optional] 
**market_services_price_flag** | [**MarketServicesPriceFlag**](MarketServicesPriceFlag.md) |  | [optional] 
**markets** | [**Market**](Market.md) |  | 

## Example

```python
from wemde_dispatch_client.models.data_with_range import DataWithRange

# TODO update the JSON string below
json = "{}"
# create an instance of DataWithRange from a JSON string
data_with_range_instance = DataWithRange.from_json(json)
# print the JSON string representation of the object
print DataWithRange.to_json()

# convert the object into a dict
data_with_range_dict = data_with_range_instance.to_dict()
# create an instance of DataWithRange from a dict
data_with_range_form_dict = data_with_range.from_dict(data_with_range_dict)
```
[[Back to Model list]](../README.md#documentation-for-models) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to README]](../README.md)



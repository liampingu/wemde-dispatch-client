# wemde_dispatch_client.TradingDayReportApi

All URIs are relative to *https://apis.prod.aemo.com.au:9319/WEM/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_tradingdayreport_tradingdayreport**](TradingDayReportApi.md#get_api_v1_tradingdayreport_tradingdayreport) | **GET** /tradingDayReport/tradingDayReport | Retrieves the Trading Day Report


# **get_api_v1_tradingdayreport_tradingdayreport**
> SwaggerTradingDayReport get_api_v1_tradingdayreport_tradingdayreport(trading_day, x_initiating_participant_id, x_market)

Retrieves the Trading Day Report

Retrieves the Trading Day Report

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_trading_day_report import SwaggerTradingDayReport
from wemde_dispatch_client.rest import ApiException
from pprint import pprint

# Defining the host is optional and defaults to https://apis.prod.aemo.com.au:9319/WEM/v1
# See configuration.py for a list of all supported configuration parameters.
configuration = wemde_dispatch_client.Configuration(
    host = "https://apis.prod.aemo.com.au:9319/WEM/v1"
)


# Enter a context with an instance of the API client
with wemde_dispatch_client.ApiClient(configuration) as api_client:
    # Create an instance of the API class
    api_instance = wemde_dispatch_client.TradingDayReportApi(api_client)
    trading_day = 'trading_day_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market

    try:
        # Retrieves the Trading Day Report
        api_response = api_instance.get_api_v1_tradingdayreport_tradingdayreport(trading_day, x_initiating_participant_id, x_market)
        print("The response of TradingDayReportApi->get_api_v1_tradingdayreport_tradingdayreport:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling TradingDayReportApi->get_api_v1_tradingdayreport_tradingdayreport: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **trading_day** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 

### Return type

[**SwaggerTradingDayReport**](SwaggerTradingDayReport.md)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: text/plain, application/json, text/json

### HTTP response details

| Status code | Description | Response headers |
|-------------|-------------|------------------|
**200** | Success |  -  |
**400** | Bad request |  -  |
**401** | Unauthorized |  -  |
**403** | Forbidden |  -  |
**404** | Not Found |  -  |
**405** | Method not allowed |  -  |
**413** | Payload Too Large |  -  |
**422** | Client Error |  -  |
**429** | Too many request |  -  |
**500** | Application Unavailable or Server Error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


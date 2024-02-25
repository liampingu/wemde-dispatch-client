# wemde_dispatch_client.ReferenceTradingPriceApi

All URIs are relative to *https://apis.prod.aemo.com.au:9319/WEM/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_referencetradingprices**](ReferenceTradingPriceApi.md#get_referencetradingprices) | **GET** /referenceTradingPrice/referenceTradingPrices | /referenceTradingPrices - GET


# **get_referencetradingprices**
> SwaggerReferenceTradingPricesRoot get_referencetradingprices(x_initiating_participant_id, x_market, trading_interval_from=trading_interval_from, trading_interval_to=trading_interval_to)

/referenceTradingPrices - GET

/referenceTradingPrices - GET

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_reference_trading_prices_root import SwaggerReferenceTradingPricesRoot
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
    api_instance = wemde_dispatch_client.ReferenceTradingPriceApi(api_client)
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    trading_interval_from = 'trading_interval_from_example' # str | Format - date-time (as date-time in RFC3339). (optional)
    trading_interval_to = 'trading_interval_to_example' # str | Format - date-time (as date-time in RFC3339). (optional)

    try:
        # /referenceTradingPrices - GET
        api_response = api_instance.get_referencetradingprices(x_initiating_participant_id, x_market, trading_interval_from=trading_interval_from, trading_interval_to=trading_interval_to)
        print("The response of ReferenceTradingPriceApi->get_referencetradingprices:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling ReferenceTradingPriceApi->get_referencetradingprices: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **trading_interval_from** | **str**| Format - date-time (as date-time in RFC3339). | [optional] 
 **trading_interval_to** | **str**| Format - date-time (as date-time in RFC3339). | [optional] 

### Return type

[**SwaggerReferenceTradingPricesRoot**](SwaggerReferenceTradingPricesRoot.md)

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
**500** | Server error or application unavailable |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


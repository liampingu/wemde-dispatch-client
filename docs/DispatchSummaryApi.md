# wemde_dispatch_client.DispatchSummaryApi

All URIs are relative to *https://apis.prod.aemo.com.au:9319/WEM/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_dispatchsummary_dispatchdata**](DispatchSummaryApi.md#get_api_v1_dispatchsummary_dispatchdata) | **GET** /dispatchSummary/dispatchData | Retrieves the Dispatch Summary Data for Dispatch Run
[**get_api_v1_dispatchsummary_dispatchdataoutcomes**](DispatchSummaryApi.md#get_api_v1_dispatchsummary_dispatchdataoutcomes) | **GET** /dispatchSummary/dispatchDataOutcomes | Retrieves Dispatch Summary Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals
[**get_api_v1_dispatchsummary_predispatchdata**](DispatchSummaryApi.md#get_api_v1_dispatchsummary_predispatchdata) | **GET** /dispatchSummary/preDispatchData | Retrieves the Dispatch Summary Data for Pre-Dispatch Run
[**get_api_v1_dispatchsummary_weekaheaddispatchdata**](DispatchSummaryApi.md#get_api_v1_dispatchsummary_weekaheaddispatchdata) | **GET** /dispatchSummary/weekAheadDispatchData | Retrieves the Dispatch Summary Data for Week Ahead Dispatch Run


# **get_api_v1_dispatchsummary_dispatchdata**
> SwaggerDispatchSummaryData get_api_v1_dispatchsummary_dispatchdata(x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, primary_dispatch_interval=primary_dispatch_interval, facility_code=facility_code)

Retrieves the Dispatch Summary Data for Dispatch Run

Retrieves the Dispatch Summary Data for Dispatch Run

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_summary_data import SwaggerDispatchSummaryData
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
    api_instance = wemde_dispatch_client.DispatchSummaryApi(api_client)
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    facility_code = 'facility_code_example' # str |  (optional)

    try:
        # Retrieves the Dispatch Summary Data for Dispatch Run
        api_response = api_instance.get_api_v1_dispatchsummary_dispatchdata(x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, primary_dispatch_interval=primary_dispatch_interval, facility_code=facility_code)
        print("The response of DispatchSummaryApi->get_api_v1_dispatchsummary_dispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchSummaryApi->get_api_v1_dispatchsummary_dispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **dispatch_interval_start_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **dispatch_interval_end_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **primary_dispatch_interval** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **facility_code** | **str**|  | [optional] 

### Return type

[**SwaggerDispatchSummaryData**](SwaggerDispatchSummaryData.md)

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
**500** | Application unavailable or server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_dispatchsummary_dispatchdataoutcomes**
> SwaggerDispatchSummaryDataWithRange get_api_v1_dispatchsummary_dispatchdataoutcomes(primary_dispatch_interval_from, primary_dispatch_interval_to, x_initiating_participant_id, x_market, facility_code=facility_code)

Retrieves Dispatch Summary Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals

Retrieves Dispatch Summary Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_summary_data_with_range import SwaggerDispatchSummaryDataWithRange
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
    api_instance = wemde_dispatch_client.DispatchSummaryApi(api_client)
    primary_dispatch_interval_from = 'primary_dispatch_interval_from_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    primary_dispatch_interval_to = 'primary_dispatch_interval_to_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    facility_code = 'facility_code_example' # str |  (optional)

    try:
        # Retrieves Dispatch Summary Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals
        api_response = api_instance.get_api_v1_dispatchsummary_dispatchdataoutcomes(primary_dispatch_interval_from, primary_dispatch_interval_to, x_initiating_participant_id, x_market, facility_code=facility_code)
        print("The response of DispatchSummaryApi->get_api_v1_dispatchsummary_dispatchdataoutcomes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchSummaryApi->get_api_v1_dispatchsummary_dispatchdataoutcomes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_dispatch_interval_from** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **primary_dispatch_interval_to** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **facility_code** | **str**|  | [optional] 

### Return type

[**SwaggerDispatchSummaryDataWithRange**](SwaggerDispatchSummaryDataWithRange.md)

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
**500** | Application unavailable or server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_dispatchsummary_predispatchdata**
> SwaggerDispatchSummaryData get_api_v1_dispatchsummary_predispatchdata(x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, primary_dispatch_interval=primary_dispatch_interval, facility_code=facility_code)

Retrieves the Dispatch Summary Data for Pre-Dispatch Run

Retrieves the Dispatch Summary Data for Pre-Dispatch Run

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_summary_data import SwaggerDispatchSummaryData
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
    api_instance = wemde_dispatch_client.DispatchSummaryApi(api_client)
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    facility_code = 'facility_code_example' # str |  (optional)

    try:
        # Retrieves the Dispatch Summary Data for Pre-Dispatch Run
        api_response = api_instance.get_api_v1_dispatchsummary_predispatchdata(x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, primary_dispatch_interval=primary_dispatch_interval, facility_code=facility_code)
        print("The response of DispatchSummaryApi->get_api_v1_dispatchsummary_predispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchSummaryApi->get_api_v1_dispatchsummary_predispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **dispatch_interval_start_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **dispatch_interval_end_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **primary_dispatch_interval** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **facility_code** | **str**|  | [optional] 

### Return type

[**SwaggerDispatchSummaryData**](SwaggerDispatchSummaryData.md)

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
**500** | Application unavailable or server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)

# **get_api_v1_dispatchsummary_weekaheaddispatchdata**
> SwaggerDispatchSummaryData get_api_v1_dispatchsummary_weekaheaddispatchdata(x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, primary_dispatch_interval=primary_dispatch_interval, facility_code=facility_code)

Retrieves the Dispatch Summary Data for Week Ahead Dispatch Run

Retrieves the Dispatch Summary Data for Week Ahead Dispatch Run

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_summary_data import SwaggerDispatchSummaryData
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
    api_instance = wemde_dispatch_client.DispatchSummaryApi(api_client)
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    facility_code = 'facility_code_example' # str |  (optional)

    try:
        # Retrieves the Dispatch Summary Data for Week Ahead Dispatch Run
        api_response = api_instance.get_api_v1_dispatchsummary_weekaheaddispatchdata(x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, primary_dispatch_interval=primary_dispatch_interval, facility_code=facility_code)
        print("The response of DispatchSummaryApi->get_api_v1_dispatchsummary_weekaheaddispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchSummaryApi->get_api_v1_dispatchsummary_weekaheaddispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **dispatch_interval_start_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **dispatch_interval_end_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **primary_dispatch_interval** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **facility_code** | **str**|  | [optional] 

### Return type

[**SwaggerDispatchSummaryData**](SwaggerDispatchSummaryData.md)

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
**500** | Application unavailable or server error |  -  |

[[Back to top]](#) [[Back to API list]](../README.md#documentation-for-api-endpoints) [[Back to Model list]](../README.md#documentation-for-models) [[Back to README]](../README.md)


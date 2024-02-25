# wemde_dispatch_client.DispatchCaseApi

All URIs are relative to *https://apis.prod.aemo.com.au:9319/WEM/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_dispatchcase_dispatchdata**](DispatchCaseApi.md#get_api_v1_dispatchcase_dispatchdata) | **GET** /dispatchCase/dispatchData | Retrieves the Case Data for Dispatch Run
[**get_api_v1_dispatchcase_dispatchdataoutcomes**](DispatchCaseApi.md#get_api_v1_dispatchcase_dispatchdataoutcomes) | **GET** /dispatchCase/dispatchDataOutcomes | Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals
[**get_api_v1_dispatchcase_predispatchdata**](DispatchCaseApi.md#get_api_v1_dispatchcase_predispatchdata) | **GET** /dispatchCase/preDispatchData | Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals
[**get_api_v1_dispatchcase_weekaheaddispatchdata**](DispatchCaseApi.md#get_api_v1_dispatchcase_weekaheaddispatchdata) | **GET** /dispatchCase/weekAheadDispatchData | Retrieves the Case Data for Week Ahead Dispatch Run


# **get_api_v1_dispatchcase_dispatchdata**
> SwaggerDispatchCaseData get_api_v1_dispatchcase_dispatchdata(primary_dispatch_interval, x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, accept_encoding=accept_encoding)

Retrieves the Case Data for Dispatch Run

Retrieves the Case Data for Dispatch Run

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_case_data import SwaggerDispatchCaseData
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
    api_instance = wemde_dispatch_client.DispatchCaseApi(api_client)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    accept_encoding = 'gzip' # str |  (optional) (default to 'gzip')

    try:
        # Retrieves the Case Data for Dispatch Run
        api_response = api_instance.get_api_v1_dispatchcase_dispatchdata(primary_dispatch_interval, x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, accept_encoding=accept_encoding)
        print("The response of DispatchCaseApi->get_api_v1_dispatchcase_dispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchCaseApi->get_api_v1_dispatchcase_dispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_dispatch_interval** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **dispatch_interval_start_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **dispatch_interval_end_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **accept_encoding** | **str**|  | [optional] [default to &#39;gzip&#39;]

### Return type

[**SwaggerDispatchCaseData**](SwaggerDispatchCaseData.md)

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

# **get_api_v1_dispatchcase_dispatchdataoutcomes**
> SwaggerDispatchCaseDataWithRange get_api_v1_dispatchcase_dispatchdataoutcomes(primary_dispatch_interval_from, primary_dispatch_interval_to, x_initiating_participant_id, x_market, accept_encoding=accept_encoding)

Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals

Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_case_data_with_range import SwaggerDispatchCaseDataWithRange
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
    api_instance = wemde_dispatch_client.DispatchCaseApi(api_client)
    primary_dispatch_interval_from = 'primary_dispatch_interval_from_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    primary_dispatch_interval_to = 'primary_dispatch_interval_to_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    accept_encoding = 'gzip' # str |  (optional) (default to 'gzip')

    try:
        # Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals
        api_response = api_instance.get_api_v1_dispatchcase_dispatchdataoutcomes(primary_dispatch_interval_from, primary_dispatch_interval_to, x_initiating_participant_id, x_market, accept_encoding=accept_encoding)
        print("The response of DispatchCaseApi->get_api_v1_dispatchcase_dispatchdataoutcomes:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchCaseApi->get_api_v1_dispatchcase_dispatchdataoutcomes: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_dispatch_interval_from** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **primary_dispatch_interval_to** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **accept_encoding** | **str**|  | [optional] [default to &#39;gzip&#39;]

### Return type

[**SwaggerDispatchCaseDataWithRange**](SwaggerDispatchCaseDataWithRange.md)

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

# **get_api_v1_dispatchcase_predispatchdata**
> SwaggerDispatchCaseData get_api_v1_dispatchcase_predispatchdata(primary_dispatch_interval, x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, accept_encoding=accept_encoding)

Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals

Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_case_data import SwaggerDispatchCaseData
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
    api_instance = wemde_dispatch_client.DispatchCaseApi(api_client)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    accept_encoding = 'gzip' # str |  (optional) (default to 'gzip')

    try:
        # Retrieves Case Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals
        api_response = api_instance.get_api_v1_dispatchcase_predispatchdata(primary_dispatch_interval, x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, accept_encoding=accept_encoding)
        print("The response of DispatchCaseApi->get_api_v1_dispatchcase_predispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchCaseApi->get_api_v1_dispatchcase_predispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_dispatch_interval** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **dispatch_interval_start_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **dispatch_interval_end_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **accept_encoding** | **str**|  | [optional] [default to &#39;gzip&#39;]

### Return type

[**SwaggerDispatchCaseData**](SwaggerDispatchCaseData.md)

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

# **get_api_v1_dispatchcase_weekaheaddispatchdata**
> SwaggerDispatchCaseData get_api_v1_dispatchcase_weekaheaddispatchdata(primary_dispatch_interval, x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, accept_encoding=accept_encoding)

Retrieves the Case Data for Week Ahead Dispatch Run

Retrieves the Case Data for Week Ahead Dispatch Run

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_case_data import SwaggerDispatchCaseData
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
    api_instance = wemde_dispatch_client.DispatchCaseApi(api_client)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    accept_encoding = 'gzip' # str |  (optional) (default to 'gzip')

    try:
        # Retrieves the Case Data for Week Ahead Dispatch Run
        api_response = api_instance.get_api_v1_dispatchcase_weekaheaddispatchdata(primary_dispatch_interval, x_initiating_participant_id, x_market, dispatch_interval_start_date=dispatch_interval_start_date, dispatch_interval_end_date=dispatch_interval_end_date, accept_encoding=accept_encoding)
        print("The response of DispatchCaseApi->get_api_v1_dispatchcase_weekaheaddispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchCaseApi->get_api_v1_dispatchcase_weekaheaddispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_dispatch_interval** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **dispatch_interval_start_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **dispatch_interval_end_date** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **accept_encoding** | **str**|  | [optional] [default to &#39;gzip&#39;]

### Return type

[**SwaggerDispatchCaseData**](SwaggerDispatchCaseData.md)

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


# wemde_dispatch_client.DSPDispatchInstructionApi

All URIs are relative to *https://apis.prod.aemo.com.au:9319/WEM/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_dspdispatchinstructionparticipantwise**](DSPDispatchInstructionApi.md#get_dspdispatchinstructionparticipantwise) | **GET** /DSPDispatchInstruction/DSPDispatchInstructionParticipantWise | Retrieves Participant wise DSP dispatch instruction for each participant
[**get_dspdispatchinstructions**](DSPDispatchInstructionApi.md#get_dspdispatchinstructions) | **GET** /DSPDispatchInstruction/DSPDispatchInstructions | Retrieves the DSP dispatch instruction for all participants
[**get_predispatchdata**](DSPDispatchInstructionApi.md#get_predispatchdata) | **GET** /DSPDispatchInstruction/preDispatchData | Pre-Dispatch DSP Schedule information for the a specified interval (for Pre-Dispatch 2 days between start and end dates of the request)
[**get_weekaheaddispatchdata**](DSPDispatchInstructionApi.md#get_weekaheaddispatchdata) | **GET** /DSPDispatchInstruction/weekAheadDispatchData | Week-Ahead Dispatch DSP Schedule information for the a specified interval (7 days between start and end dates for week ahead)
[**put_dispatchinstructionack_dispatchinstructionid**](DSPDispatchInstructionApi.md#put_dispatchinstructionack_dispatchinstructionid) | **PUT** /DSPDispatchInstruction/dispatchInstructionAck/{dispatchInstructionId} | Acknowledge the Dispatch Instruction


# **get_dspdispatchinstructionparticipantwise**
> SwaggerDSPDispatchInstructionsParticipantWise get_dspdispatchinstructionparticipantwise(x_initiating_participant_id, x_market, dispatch_interval_from=dispatch_interval_from, facility_code=facility_code)

Retrieves Participant wise DSP dispatch instruction for each participant

Retrieves Participant wise DSP dispatch instruction for each participant

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dsp_dispatch_instructions_participant_wise import SwaggerDSPDispatchInstructionsParticipantWise
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
    api_instance = wemde_dispatch_client.DSPDispatchInstructionApi(api_client)
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    dispatch_interval_from = 'dispatch_interval_from_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    facility_code = 'facility_code_example' # str |  (optional)

    try:
        # Retrieves Participant wise DSP dispatch instruction for each participant
        api_response = api_instance.get_dspdispatchinstructionparticipantwise(x_initiating_participant_id, x_market, dispatch_interval_from=dispatch_interval_from, facility_code=facility_code)
        print("The response of DSPDispatchInstructionApi->get_dspdispatchinstructionparticipantwise:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DSPDispatchInstructionApi->get_dspdispatchinstructionparticipantwise: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **dispatch_interval_from** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **facility_code** | **str**|  | [optional] 

### Return type

[**SwaggerDSPDispatchInstructionsParticipantWise**](SwaggerDSPDispatchInstructionsParticipantWise.md)

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

# **get_dspdispatchinstructions**
> SwaggerDSPDispatchInstructions get_dspdispatchinstructions(x_initiating_participant_id, x_market, facility_code=facility_code, interval_from=interval_from, interval_to=interval_to)

Retrieves the DSP dispatch instruction for all participants

Retrieves the DSP dispatch instruction for all participants

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dsp_dispatch_instructions import SwaggerDSPDispatchInstructions
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
    api_instance = wemde_dispatch_client.DSPDispatchInstructionApi(api_client)
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    facility_code = 'facility_code_example' # str |  (optional)
    interval_from = 'interval_from_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)
    interval_to = 'interval_to_example' # str | Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (optional)

    try:
        # Retrieves the DSP dispatch instruction for all participants
        api_response = api_instance.get_dspdispatchinstructions(x_initiating_participant_id, x_market, facility_code=facility_code, interval_from=interval_from, interval_to=interval_to)
        print("The response of DSPDispatchInstructionApi->get_dspdispatchinstructions:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DSPDispatchInstructionApi->get_dspdispatchinstructions: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **facility_code** | **str**|  | [optional] 
 **interval_from** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 
 **interval_to** | **str**| Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 | [optional] 

### Return type

[**SwaggerDSPDispatchInstructions**](SwaggerDSPDispatchInstructions.md)

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

# **get_predispatchdata**
> SwaggerDspScheduleInformation get_predispatchdata(primary_dispatch_interval, dispatch_interval_start_date, dispatch_interval_end_date, x_initiating_participant_id, x_market)

Pre-Dispatch DSP Schedule information for the a specified interval (for Pre-Dispatch 2 days between start and end dates of the request)

Pre-Dispatch DSP Schedule information for the a specified interval (for Pre-Dispatch 2 days between start and end dates of the request)

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dsp_schedule_information import SwaggerDspScheduleInformation
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
    api_instance = wemde_dispatch_client.DSPDispatchInstructionApi(api_client)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | primary dispatch interval
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | dispatch interval start date
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | dispatch interval end date
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market

    try:
        # Pre-Dispatch DSP Schedule information for the a specified interval (for Pre-Dispatch 2 days between start and end dates of the request)
        api_response = api_instance.get_predispatchdata(primary_dispatch_interval, dispatch_interval_start_date, dispatch_interval_end_date, x_initiating_participant_id, x_market)
        print("The response of DSPDispatchInstructionApi->get_predispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DSPDispatchInstructionApi->get_predispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_dispatch_interval** | **str**| primary dispatch interval | 
 **dispatch_interval_start_date** | **str**| dispatch interval start date | 
 **dispatch_interval_end_date** | **str**| dispatch interval end date | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 

### Return type

[**SwaggerDspScheduleInformation**](SwaggerDspScheduleInformation.md)

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

# **get_weekaheaddispatchdata**
> SwaggerDspScheduleInformation get_weekaheaddispatchdata(primary_dispatch_interval, dispatch_interval_start_date, dispatch_interval_end_date, x_initiating_participant_id, x_market)

Week-Ahead Dispatch DSP Schedule information for the a specified interval (7 days between start and end dates for week ahead)

Week-Ahead Dispatch DSP Schedule information for the a specified interval (7 days between start and end dates for week ahead)

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dsp_schedule_information import SwaggerDspScheduleInformation
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
    api_instance = wemde_dispatch_client.DSPDispatchInstructionApi(api_client)
    primary_dispatch_interval = 'primary_dispatch_interval_example' # str | primary dispatch interval
    dispatch_interval_start_date = 'dispatch_interval_start_date_example' # str | dispatch interval start date
    dispatch_interval_end_date = 'dispatch_interval_end_date_example' # str | dispatch interval end date
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market

    try:
        # Week-Ahead Dispatch DSP Schedule information for the a specified interval (7 days between start and end dates for week ahead)
        api_response = api_instance.get_weekaheaddispatchdata(primary_dispatch_interval, dispatch_interval_start_date, dispatch_interval_end_date, x_initiating_participant_id, x_market)
        print("The response of DSPDispatchInstructionApi->get_weekaheaddispatchdata:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DSPDispatchInstructionApi->get_weekaheaddispatchdata: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **primary_dispatch_interval** | **str**| primary dispatch interval | 
 **dispatch_interval_start_date** | **str**| dispatch interval start date | 
 **dispatch_interval_end_date** | **str**| dispatch interval end date | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 

### Return type

[**SwaggerDspScheduleInformation**](SwaggerDspScheduleInformation.md)

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

# **put_dispatchinstructionack_dispatchinstructionid**
> put_dispatchinstructionack_dispatchinstructionid(dispatch_instruction_id, x_initiating_participant_id, x_market)

Acknowledge the Dispatch Instruction

Acknowledge the Dispatch Instruction

### Example


```python
import wemde_dispatch_client
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
    api_instance = wemde_dispatch_client.DSPDispatchInstructionApi(api_client)
    dispatch_instruction_id = 'dispatch_instruction_id_example' # str | Format - uuid.
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market

    try:
        # Acknowledge the Dispatch Instruction
        api_instance.put_dispatchinstructionack_dispatchinstructionid(dispatch_instruction_id, x_initiating_participant_id, x_market)
    except Exception as e:
        print("Exception when calling DSPDispatchInstructionApi->put_dispatchinstructionack_dispatchinstructionid: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **dispatch_instruction_id** | **str**| Format - uuid. | 
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 

### Return type

void (empty response body)

### Authorization

No authorization required

### HTTP request headers

 - **Content-Type**: Not defined
 - **Accept**: application/json, text/plain, text/json

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


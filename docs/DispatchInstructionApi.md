# wemde_dispatch_client.DispatchInstructionApi

All URIs are relative to *https://apis.prod.aemo.com.au:9319/WEM/v1*

Method | HTTP request | Description
------------- | ------------- | -------------
[**get_api_v1_dispatchinstruction_dispatchinstruction**](DispatchInstructionApi.md#get_api_v1_dispatchinstruction_dispatchinstruction) | **GET** /dispatchInstruction/dispatchInstruction | Retrieves the recent dispatch instruction for each participant


# **get_api_v1_dispatchinstruction_dispatchinstruction**
> SwaggerDispatchInstructionData get_api_v1_dispatchinstruction_dispatchinstruction(x_initiating_participant_id, x_market, facility_code=facility_code, updated_records_only=updated_records_only)

Retrieves the recent dispatch instruction for each participant

Retrieves the recent dispatch instruction for each participant

### Example


```python
import wemde_dispatch_client
from wemde_dispatch_client.models.swagger_dispatch_instruction_data import SwaggerDispatchInstructionData
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
    api_instance = wemde_dispatch_client.DispatchInstructionApi(api_client)
    x_initiating_participant_id = 'x_initiating_participant_id_example' # str | The id of the Initiating Participant
    x_market = 'x_market_example' # str | The id of the market
    facility_code = 'facility_code_example' # str |  (optional)
    updated_records_only = False # bool |  (optional) (default to False)

    try:
        # Retrieves the recent dispatch instruction for each participant
        api_response = api_instance.get_api_v1_dispatchinstruction_dispatchinstruction(x_initiating_participant_id, x_market, facility_code=facility_code, updated_records_only=updated_records_only)
        print("The response of DispatchInstructionApi->get_api_v1_dispatchinstruction_dispatchinstruction:\n")
        pprint(api_response)
    except Exception as e:
        print("Exception when calling DispatchInstructionApi->get_api_v1_dispatchinstruction_dispatchinstruction: %s\n" % e)
```



### Parameters


Name | Type | Description  | Notes
------------- | ------------- | ------------- | -------------
 **x_initiating_participant_id** | **str**| The id of the Initiating Participant | 
 **x_market** | **str**| The id of the market | 
 **facility_code** | **str**|  | [optional] 
 **updated_records_only** | **bool**|  | [optional] [default to False]

### Return type

[**SwaggerDispatchInstructionData**](SwaggerDispatchInstructionData.md)

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


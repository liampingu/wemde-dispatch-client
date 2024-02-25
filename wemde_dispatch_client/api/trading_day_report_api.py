# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501

import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictStr
from typing_extensions import Annotated
from wemde_dispatch_client.models.swagger_trading_day_report import SwaggerTradingDayReport

from wemde_dispatch_client.api_client import ApiClient, RequestSerialized
from wemde_dispatch_client.api_response import ApiResponse
from wemde_dispatch_client.rest import RESTResponseType


class TradingDayReportApi:
    """NOTE: This class is auto generated by OpenAPI Generator
    Ref: https://openapi-generator.tech

    Do not edit the class manually.
    """

    def __init__(self, api_client=None) -> None:
        if api_client is None:
            api_client = ApiClient.get_default()
        self.api_client = api_client


    @validate_call
    def get_api_v1_tradingdayreport_tradingdayreport(
        self,
        trading_day: Annotated[StrictStr, Field(description="Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00")],
        x_initiating_participant_id: Annotated[StrictStr, Field(description="The id of the Initiating Participant")],
        x_market: Annotated[StrictStr, Field(description="The id of the market")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SwaggerTradingDayReport:
        """Retrieves the Trading Day Report

        Retrieves the Trading Day Report

        :param trading_day: Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (required)
        :type trading_day: str
        :param x_initiating_participant_id: The id of the Initiating Participant (required)
        :type x_initiating_participant_id: str
        :param x_market: The id of the market (required)
        :type x_market: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_api_v1_tradingdayreport_tradingdayreport_serialize(
            trading_day=trading_day,
            x_initiating_participant_id=x_initiating_participant_id,
            x_market=x_market,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SwaggerTradingDayReport",
            '400': "SwaggerErrorResponse",
            '401': "SwaggerErrorResponse",
            '403': "SwaggerErrorResponse",
            '404': "SwaggerErrorResponse",
            '405': "SwaggerErrorResponse",
            '413': "SwaggerErrorResponse",
            '422': "SwaggerErrorResponse",
            '429': "SwaggerErrorResponse",
            '500': "SwaggerErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_api_v1_tradingdayreport_tradingdayreport_with_http_info(
        self,
        trading_day: Annotated[StrictStr, Field(description="Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00")],
        x_initiating_participant_id: Annotated[StrictStr, Field(description="The id of the Initiating Participant")],
        x_market: Annotated[StrictStr, Field(description="The id of the market")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SwaggerTradingDayReport]:
        """Retrieves the Trading Day Report

        Retrieves the Trading Day Report

        :param trading_day: Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (required)
        :type trading_day: str
        :param x_initiating_participant_id: The id of the Initiating Participant (required)
        :type x_initiating_participant_id: str
        :param x_market: The id of the market (required)
        :type x_market: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_api_v1_tradingdayreport_tradingdayreport_serialize(
            trading_day=trading_day,
            x_initiating_participant_id=x_initiating_participant_id,
            x_market=x_market,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SwaggerTradingDayReport",
            '400': "SwaggerErrorResponse",
            '401': "SwaggerErrorResponse",
            '403': "SwaggerErrorResponse",
            '404': "SwaggerErrorResponse",
            '405': "SwaggerErrorResponse",
            '413': "SwaggerErrorResponse",
            '422': "SwaggerErrorResponse",
            '429': "SwaggerErrorResponse",
            '500': "SwaggerErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_api_v1_tradingdayreport_tradingdayreport_without_preload_content(
        self,
        trading_day: Annotated[StrictStr, Field(description="Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00")],
        x_initiating_participant_id: Annotated[StrictStr, Field(description="The id of the Initiating Participant")],
        x_market: Annotated[StrictStr, Field(description="The id of the market")],
        _request_timeout: Union[
            None,
            Annotated[StrictFloat, Field(gt=0)],
            Tuple[
                Annotated[StrictFloat, Field(gt=0)],
                Annotated[StrictFloat, Field(gt=0)]
            ]
        ] = None,
        _request_auth: Optional[Dict[StrictStr, Any]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieves the Trading Day Report

        Retrieves the Trading Day Report

        :param trading_day: Default date format: yyyy-MM-ddTHH:mm:ss+08:00. For request, the offset +08:00 is optional - api will by default treat incoming time as +08:00 (required)
        :type trading_day: str
        :param x_initiating_participant_id: The id of the Initiating Participant (required)
        :type x_initiating_participant_id: str
        :param x_market: The id of the market (required)
        :type x_market: str
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _request_auth: set to override the auth_settings for an a single
                              request; this effectively ignores the
                              authentication in the spec for a single request.
        :type _request_auth: dict, optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_api_v1_tradingdayreport_tradingdayreport_serialize(
            trading_day=trading_day,
            x_initiating_participant_id=x_initiating_participant_id,
            x_market=x_market,
            _request_auth=_request_auth,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SwaggerTradingDayReport",
            '400': "SwaggerErrorResponse",
            '401': "SwaggerErrorResponse",
            '403': "SwaggerErrorResponse",
            '404': "SwaggerErrorResponse",
            '405': "SwaggerErrorResponse",
            '413': "SwaggerErrorResponse",
            '422': "SwaggerErrorResponse",
            '429': "SwaggerErrorResponse",
            '500': "SwaggerErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout=_request_timeout
        )
        return response_data.response


    def _get_api_v1_tradingdayreport_tradingdayreport_serialize(
        self,
        trading_day,
        x_initiating_participant_id,
        x_market,
        _request_auth,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[str, str] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        # process the query parameters
        if trading_day is not None:
            
            _query_params.append(('tradingDay', trading_day))
            
        # process the header parameters
        if x_initiating_participant_id is not None:
            _header_params['x-initiatingParticipantId'] = x_initiating_participant_id
        if x_market is not None:
            _header_params['x-market'] = x_market
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        _header_params['Accept'] = self.api_client.select_header_accept(
            [
                'text/plain', 
                'application/json', 
                'text/json'
            ]
        )


        # authentication setting
        _auth_settings: List[str] = [
        ]

        return self.api_client.param_serialize(
            method='GET',
            resource_path='/tradingDayReport/tradingDayReport',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            auth_settings=_auth_settings,
            collection_formats=_collection_formats,
            _host=_host,
            _request_auth=_request_auth
        )


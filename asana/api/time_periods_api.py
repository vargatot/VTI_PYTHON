# coding: utf-8

"""
    Asana

    This is the interface for interacting with the [Asana Platform](https://developers.asana.com). Our API reference is generated from our [OpenAPI spec] (https://raw.githubusercontent.com/Asana/openapi/master/defs/asana_oas.yaml).  # noqa: E501

    OpenAPI spec version: 1.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import re  # noqa: F401

# python 2 and python 3 compatibility library
import six
from asana.api_client import ApiClient
from asana.pagination.event_iterator import EventIterator
from asana.pagination.page_iterator import PageIterator

class TimePeriodsApi(object):
    """NOTE: This class is auto generated by the swagger code generator program.

    Do not edit the class manually.
    Ref: https://github.com/swagger-api/swagger-codegen
    """

    def __init__(self, api_client=None):
        if api_client is None:
            api_client = ApiClient()
        self.api_client = api_client

    def get_time_period(self, time_period_gid, opts, **kwargs):  # noqa: E501
        """Get a time period  # noqa: E501

        Returns the full record for a single time period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_period(time_period_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str time_period_gid: Globally unique identifier for the time period. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimePeriodResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_time_period_with_http_info(time_period_gid, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_time_period_with_http_info(time_period_gid, opts, **kwargs)  # noqa: E501
            return data

    def get_time_period_with_http_info(self, time_period_gid, opts, **kwargs):  # noqa: E501
        """Get a time period  # noqa: E501

        Returns the full record for a single time period.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_period_with_http_info(time_period_gid, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str time_period_gid: Globally unique identifier for the time period. (required)
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimePeriodResponseData
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_time_period" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'time_period_gid' is set
        if (time_period_gid is None):
            raise ValueError("Missing the required parameter `time_period_gid` when calling `get_time_period`")  # noqa: E501

        collection_formats = {}

        path_params = {}
        path_params['time_period_gid'] = time_period_gid  # noqa: E501

        query_params = {}
        query_params = opts


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/time_periods/{time_period_gid}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            (data) = self.api_client.call_api(
                '/time_periods/{time_period_gid}', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
            if params.get('_return_http_data_only') == False:
                return data
            return data["data"] if data else data
        else:
            return self.api_client.call_api(
            '/time_periods/{time_period_gid}', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def get_time_periods(self, workspace, opts, **kwargs):  # noqa: E501
        """Get time periods  # noqa: E501

        Returns compact time period records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_periods(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Globally unique identifier for the workspace. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
        :param date start_on: ISO 8601 date string
        :param date end_on: ISO 8601 date string
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimePeriodResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = kwargs.get("_return_http_data_only", True)
        if kwargs.get('async_req'):
            return self.get_time_periods_with_http_info(workspace, opts, **kwargs)  # noqa: E501
        else:
            (data) = self.get_time_periods_with_http_info(workspace, opts, **kwargs)  # noqa: E501
            return data

    def get_time_periods_with_http_info(self, workspace, opts, **kwargs):  # noqa: E501
        """Get time periods  # noqa: E501

        Returns compact time period records.  # noqa: E501
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.get_time_periods_with_http_info(workspace, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str workspace: Globally unique identifier for the workspace. (required)
        :param int limit: Results per page. The number of objects to return per page. The value must be between 1 and 100.
        :param str offset: Offset token. An offset to the next page returned by the API. A pagination request will return an offset token, which can be used as an input parameter to the next request. If an offset is not passed in, the API will return the first page of results. *Note: You can only pass in an offset that was returned to you via a previously paginated request.*
        :param date start_on: ISO 8601 date string
        :param date end_on: ISO 8601 date string
        :param list[str] opt_fields: This endpoint returns a compact resource, which excludes some properties by default. To include those optional properties, set this query parameter to a comma-separated list of the properties you wish to include.
        :return: TimePeriodResponseArray
                 If the method is called asynchronously,
                 returns the request thread.
        """
        all_params = []
        all_params.append('async_req')
        all_params.append('header_params')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')
        all_params.append('full_payload')
        all_params.append('item_limit')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method get_time_periods" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'workspace' is set
        if (workspace is None):
            raise ValueError("Missing the required parameter `workspace` when calling `get_time_periods`")  # noqa: E501

        collection_formats = {}

        path_params = {}

        query_params = {}
        query_params = opts
        query_params['workspace'] = workspace


        header_params = kwargs.get("header_params", {})

        form_params = []
        local_var_files = {}

        body_params = None

        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json; charset=UTF-8'])  # noqa: E501

        # Authentication setting
        auth_settings = ['personalAccessToken']  # noqa: E501

        # hard checking for True boolean value because user can provide full_payload or async_req with any data type
        if kwargs.get("full_payload", False) is True or kwargs.get('async_req', False) is True:
            return self.api_client.call_api(
                '/time_periods', 'GET',
                path_params,
                query_params,
                header_params,
                body=body_params,
                post_params=form_params,
                files=local_var_files,
                response_type=object,  # noqa: E501
                auth_settings=auth_settings,
                async_req=params.get('async_req'),
                _return_http_data_only=params.get('_return_http_data_only'),
                _preload_content=params.get('_preload_content', True),
                _request_timeout=params.get('_request_timeout'),
                collection_formats=collection_formats
            )
        elif self.api_client.configuration.return_page_iterator:
            query_params["limit"] = query_params.get("limit", self.api_client.configuration.page_limit)
            return PageIterator(
                self.api_client,
                {
                    "resource_path": '/time_periods',
                    "method": 'GET',
                    "path_params": path_params,
                    "query_params": query_params,
                    "header_params": header_params,
                    "body": body_params,
                    "post_params": form_params,
                    "files": local_var_files,
                    "response_type": object,
                    "auth_settings": auth_settings,
                    "async_req": params.get('async_req'),
                    "_return_http_data_only": params.get('_return_http_data_only'),
                    "_preload_content": params.get('_preload_content', True),
                    "_request_timeout": params.get('_request_timeout'),
                    "collection_formats": collection_formats
                },
                **kwargs
            ).items()
        else:
            return self.api_client.call_api(
            '/time_periods', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=object,  # noqa: E501
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import json
from enum import Enum
from typing_extensions import Self


class UnconstrainedForecastSourceTypes(str, Enum):
    """
    UnconstrainedForecastSourceTypes
    """

    """
    allowed enum values
    """
    SCADA = 'scada'
    RTMS = 'rtms'
    PERSISTENCE = 'persistence'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of UnconstrainedForecastSourceTypes from a JSON string"""
        return cls(json.loads(json_str))



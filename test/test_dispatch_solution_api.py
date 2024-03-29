# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.api.dispatch_solution_api import DispatchSolutionApi


class TestDispatchSolutionApi(unittest.TestCase):
    """DispatchSolutionApi unit test stubs"""

    def setUp(self) -> None:
        self.api = DispatchSolutionApi()

    def tearDown(self) -> None:
        pass

    def test_get_api_v1_dispatchsolution_dispatchdata(self) -> None:
        """Test case for get_api_v1_dispatchsolution_dispatchdata

        Retrieves the Solution Data for Dispatch Run
        """
        pass

    def test_get_api_v1_dispatchsolution_dispatchdataoutcomes(self) -> None:
        """Test case for get_api_v1_dispatchsolution_dispatchdataoutcomes

        Retrieves Solution Data from the Central Dispatch Process through a range of past Primary Dispatch Intervals
        """
        pass

    def test_get_api_v1_dispatchsolution_predispatchdata(self) -> None:
        """Test case for get_api_v1_dispatchsolution_predispatchdata

        Retrieves the Solution Data for Pre-Dispatch Run
        """
        pass

    def test_get_api_v1_dispatchsolution_weekaheaddispatchdata(self) -> None:
        """Test case for get_api_v1_dispatchsolution_weekaheaddispatchdata

        Retrieves the Solution Data for Week Ahead Dispatch Run
        """
        pass


if __name__ == '__main__':
    unittest.main()

# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.market_sub_category import MarketSubCategory

class TestMarketSubCategory(unittest.TestCase):
    """MarketSubCategory unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarketSubCategory:
        """Test MarketSubCategory
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarketSubCategory`
        """
        model = MarketSubCategory()
        if include_optional:
            return MarketSubCategory(
                market_service = '',
                base_forecast_requirement = 1.337,
                override_forecast_requirement = 1.337
            )
        else:
            return MarketSubCategory(
        )
        """

    def testMarketSubCategory(self):
        """Test MarketSubCategory"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
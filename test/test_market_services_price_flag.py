# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.market_services_price_flag import MarketServicesPriceFlag

class TestMarketServicesPriceFlag(unittest.TestCase):
    """MarketServicesPriceFlag unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> MarketServicesPriceFlag:
        """Test MarketServicesPriceFlag
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `MarketServicesPriceFlag`
        """
        model = MarketServicesPriceFlag()
        if include_optional:
            return MarketServicesPriceFlag(
                energy_price_at_cap = True,
                regulation_raise_price_at_cap = True,
                regulation_lower_price_at_cap = True,
                contingency_lower_price_at_cap = True,
                contingency_raise_price_at_cap = True,
                rocof_price_at_cap = True
            )
        else:
            return MarketServicesPriceFlag(
                energy_price_at_cap = True,
                regulation_raise_price_at_cap = True,
                regulation_lower_price_at_cap = True,
                contingency_lower_price_at_cap = True,
                contingency_raise_price_at_cap = True,
                rocof_price_at_cap = True,
        )
        """

    def testMarketServicesPriceFlag(self):
        """Test MarketServicesPriceFlag"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

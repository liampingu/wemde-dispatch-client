# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.tranch import Tranch

class TestTranch(unittest.TestCase):
    """Tranch unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Tranch:
        """Test Tranch
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Tranch`
        """
        model = Tranch()
        if include_optional:
            return Tranch(
                tranche = 56,
                fuel_type = '',
                quantity = 1.337,
                submitted_price = 1.337,
                lfa_price = 1.337,
                capacity_type = '',
                notice_time = 56
            )
        else:
            return Tranch(
                tranche = 56,
                quantity = 1.337,
                submitted_price = 1.337,
        )
        """

    def testTranch(self):
        """Test Tranch"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
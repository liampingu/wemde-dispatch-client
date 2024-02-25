# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.dispatch_total import DispatchTotal

class TestDispatchTotal(unittest.TestCase):
    """DispatchTotal unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DispatchTotal:
        """Test DispatchTotal
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DispatchTotal`
        """
        model = DispatchTotal()
        if include_optional:
            return DispatchTotal(
                energy_injection_capacity = 1.337,
                energy_withdrawal_capacity = 1.337,
                contingency_raise = 1.337,
                contingency_lower = 1.337,
                regulation_raise = 1.337,
                regulation_lower = 1.337,
                rocof = 1.337
            )
        else:
            return DispatchTotal(
        )
        """

    def testDispatchTotal(self):
        """Test DispatchTotal"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
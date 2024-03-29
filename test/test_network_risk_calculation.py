# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.network_risk_calculation import NetworkRiskCalculation

class TestNetworkRiskCalculation(unittest.TestCase):
    """NetworkRiskCalculation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> NetworkRiskCalculation:
        """Test NetworkRiskCalculation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `NetworkRiskCalculation`
        """
        model = NetworkRiskCalculation()
        if include_optional:
            return NetworkRiskCalculation(
                dispatch_interval = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                network_risks = [
                    wemde_dispatch_client.models.network_risk.NetworkRisk(
                        network_contingency = '', 
                        network_risk_value = 1.337, 
                        associated_facility_codes = [
                            ''
                            ], )
                    ]
            )
        else:
            return NetworkRiskCalculation(
        )
        """

    def testNetworkRiskCalculation(self):
        """Test NetworkRiskCalculation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

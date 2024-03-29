# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.facility import Facility

class TestFacility(unittest.TestCase):
    """Facility unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> Facility:
        """Test Facility
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `Facility`
        """
        model = Facility()
        if include_optional:
            return Facility(
                dsp_unconstrained_withdrawal_quantity = 1.337,
                dsp_constrained_withdrawal_quantity = 1.337,
                facility_code = '',
                submission_id = '',
                submission_code = '',
                tranches = [
                    wemde_dispatch_client.models.tranch.Tranch(
                        tranche = 56, 
                        fuel_type = '', 
                        quantity = 1.337, 
                        submitted_price = 1.337, 
                        lfa_price = 1.337, 
                        capacity_type = '', 
                        notice_time = 56, )
                    ],
                maximum_capacity = 1.337,
                enablement_minimum = 1.337,
                enablement_minimum_value_used = 1.337,
                low_breakpoint = 1.337,
                low_breakpoint_value_used = 1.337,
                high_breakpoint = 1.337,
                high_breakpoint_value_used = 1.337,
                enablement_maximum = 1.337,
                enablement_maximum_value_used = 1.337
            )
        else:
            return Facility(
                dsp_unconstrained_withdrawal_quantity = 1.337,
                dsp_constrained_withdrawal_quantity = 1.337,
                facility_code = '',
                submission_id = '',
                maximum_capacity = 1.337,
                enablement_minimum = 1.337,
                low_breakpoint = 1.337,
                high_breakpoint = 1.337,
                enablement_maximum = 1.337,
        )
        """

    def testFacility(self):
        """Test Facility"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

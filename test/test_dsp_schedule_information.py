# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.dsp_schedule_information import DspScheduleInformation

class TestDspScheduleInformation(unittest.TestCase):
    """DspScheduleInformation unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DspScheduleInformation:
        """Test DspScheduleInformation
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DspScheduleInformation`
        """
        model = DspScheduleInformation()
        if include_optional:
            return DspScheduleInformation(
                facility_code = '',
                dispatch_interval = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'),
                dsp_unconstrained_withdrawal_quantity = 1.337,
                dsp_constrained_withdrawal_quantity = 1.337,
                relevant_demand = 1.337,
                min_withdrawal = 1.337,
                rcoq = 1.337,
                forecast_capacity = 1.337,
                forecast_reduction = 1.337
            )
        else:
            return DspScheduleInformation(
        )
        """

    def testDspScheduleInformation(self):
        """Test DspScheduleInformation"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

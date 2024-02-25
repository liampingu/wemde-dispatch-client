# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.dfcm_data import DfcmData

class TestDfcmData(unittest.TestCase):
    """DfcmData unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DfcmData:
        """Test DfcmData
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DfcmData`
        """
        model = DfcmData()
        if include_optional:
            return DfcmData(
                dfcm_id = '',
                dfcm_schema_version = '',
                frequency_limits = wemde_dispatch_client.models.frequency_limits.FrequencyLimits(
                    rocof_max = 1.337, 
                    rocof_min = 1.337, 
                    fmin = 1.337, 
                    fmax = 1.337, 
                    fss = 1.337, ),
                dfcm_validation_details = wemde_dispatch_client.models.dfcm_validation_details.DfcmValidationDetails(
                    inertia_range_minimum = 1.337, 
                    inertia_range_maximum = 1.337, 
                    inertia_range_step = 1.337, 
                    largest_contingency_size_minimum = 1.337, 
                    largest_contingency_size_maximum = 1.337, 
                    largest_contingency_size_step = 1.337, ),
                tau_valuesfor_cr_performance_factors = [
                    1.337
                    ]
            )
        else:
            return DfcmData(
        )
        """

    def testDfcmData(self):
        """Test DfcmData"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

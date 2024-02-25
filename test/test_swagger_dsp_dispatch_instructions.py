# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.swagger_dsp_dispatch_instructions import SwaggerDSPDispatchInstructions

class TestSwaggerDSPDispatchInstructions(unittest.TestCase):
    """SwaggerDSPDispatchInstructions unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwaggerDSPDispatchInstructions:
        """Test SwaggerDSPDispatchInstructions
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwaggerDSPDispatchInstructions`
        """
        model = SwaggerDSPDispatchInstructions()
        if include_optional:
            return SwaggerDSPDispatchInstructions(
                transaction_id = '',
                data = wemde_dispatch_client.models.swagger_dsp_dispatch_instructions_data.SwaggerDSPDispatchInstructionsData(
                    issued_time = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                    dsp_dispatch_instructions = [
                        wemde_dispatch_client.models.dsp_dispatch_instructions_data.DSPDispatchInstructionsData(
                            facility_code = '', 
                            dispatch_interval_from = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            dispatch_interval_to = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                            withdrawal_quantity = 1.337, )
                        ], )
            )
        else:
            return SwaggerDSPDispatchInstructions(
        )
        """

    def testSwaggerDSPDispatchInstructions(self):
        """Test SwaggerDSPDispatchInstructions"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
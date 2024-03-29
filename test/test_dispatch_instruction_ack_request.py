# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.dispatch_instruction_ack_request import DispatchInstructionAckRequest

class TestDispatchInstructionAckRequest(unittest.TestCase):
    """DispatchInstructionAckRequest unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> DispatchInstructionAckRequest:
        """Test DispatchInstructionAckRequest
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `DispatchInstructionAckRequest`
        """
        model = DispatchInstructionAckRequest()
        if include_optional:
            return DispatchInstructionAckRequest(
                ackstatus = '',
                errors = [
                    wemde_dispatch_client.models.dispatch_errors.DispatchErrors(
                        title = '', 
                        detail = '', )
                    ]
            )
        else:
            return DispatchInstructionAckRequest(
                ackstatus = '',
        )
        """

    def testDispatchInstructionAckRequest(self):
        """Test DispatchInstructionAckRequest"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

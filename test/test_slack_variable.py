# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.slack_variable import SlackVariable

class TestSlackVariable(unittest.TestCase):
    """SlackVariable unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SlackVariable:
        """Test SlackVariable
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SlackVariable`
        """
        model = SlackVariable()
        if include_optional:
            return SlackVariable(
                variable = '',
                value = 1.337
            )
        else:
            return SlackVariable(
        )
        """

    def testSlackVariable(self):
        """Test SlackVariable"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()
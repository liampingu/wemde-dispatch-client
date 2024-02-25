# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.error_structure import ErrorStructure

class TestErrorStructure(unittest.TestCase):
    """ErrorStructure unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ErrorStructure:
        """Test ErrorStructure
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ErrorStructure`
        """
        model = ErrorStructure()
        if include_optional:
            return ErrorStructure(
                code = 56,
                title = '',
                detail = '',
                source = ''
            )
        else:
            return ErrorStructure(
        )
        """

    def testErrorStructure(self):
        """Test ErrorStructure"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

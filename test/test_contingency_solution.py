# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.contingency_solution import ContingencySolution

class TestContingencySolution(unittest.TestCase):
    """ContingencySolution unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> ContingencySolution:
        """Test ContingencySolution
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `ContingencySolution`
        """
        model = ContingencySolution()
        if include_optional:
            return ContingencySolution(
                solved_inertia = 1.337,
                solved_contingency = 1.337,
                contingency_raise_requirement = 1.337,
                contingency_raise_deficit = 1.337,
                demand_level = 1.337,
                cleared_contingency_raise = 1.337,
                largest_contingency = 1.337,
                contingency_raise_offset = 1.337,
                contingency_lower_offset = 1.337
            )
        else:
            return ContingencySolution(
        )
        """

    def testContingencySolution(self):
        """Test ContingencySolution"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

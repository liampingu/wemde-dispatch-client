# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


import unittest

from wemde_dispatch_client.models.swagger_not_in_service_capacities_root import SwaggerNotInServiceCapacitiesRoot

class TestSwaggerNotInServiceCapacitiesRoot(unittest.TestCase):
    """SwaggerNotInServiceCapacitiesRoot unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> SwaggerNotInServiceCapacitiesRoot:
        """Test SwaggerNotInServiceCapacitiesRoot
            include_option is a boolean, when False only required
            params are included, when True both required and
            optional params are included """
        # uncomment below to create an instance of `SwaggerNotInServiceCapacitiesRoot`
        """
        model = SwaggerNotInServiceCapacitiesRoot()
        if include_optional:
            return SwaggerNotInServiceCapacitiesRoot(
                data = [
                    wemde_dispatch_client.models.swagger_not_in_service_capacities.SwaggerNotInServiceCapacities(
                        dispatch_interval = datetime.datetime.strptime('2013-10-20 19:20:30.00', '%Y-%m-%d %H:%M:%S.%f'), 
                        not_in_service_capacities = [
                            wemde_dispatch_client.models.not_in_service_capacities.NotInServiceCapacities(
                                facility_code = '', 
                                not_in_service_capacity = 56, )
                            ], )
                    ],
                transaction_id = ''
            )
        else:
            return SwaggerNotInServiceCapacitiesRoot(
        )
        """

    def testSwaggerNotInServiceCapacitiesRoot(self):
        """Test SwaggerNotInServiceCapacitiesRoot"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)

if __name__ == '__main__':
    unittest.main()

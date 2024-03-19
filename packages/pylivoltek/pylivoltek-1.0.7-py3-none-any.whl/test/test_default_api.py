# coding: utf-8

"""
    Livoltek API

    No description provided (generated by Swagger Codegen https://github.com/swagger-api/swagger-codegen)  # noqa: E501

    OpenAPI spec version: 1.0.0
    
    Generated by: https://github.com/swagger-api/swagger-codegen.git
"""

from __future__ import absolute_import

import unittest

import pylivoltek
from pylivoltek.api.default_api import DefaultApi  # noqa: E501
from pylivoltek.rest import ApiException


class TestDefaultApi(unittest.TestCase):
    """DefaultApi unit test stubs"""

    def setUp(self):
        self.api = DefaultApi()  # noqa: E501

    def tearDown(self):
        pass

    def test_hess_api_device_device_id_real_electricity_get(self):
        """Test case for hess_api_device_device_id_real_electricity_get

        Device Generation or Consumption  # noqa: E501
        """
        pass

    def test_hess_api_device_site_id_list_get(self):
        """Test case for hess_api_device_site_id_list_get

        Device List  # noqa: E501
        """
        pass

    def test_hess_api_login_post(self):
        """Test case for hess_api_login_post

        API User Login and Get Token  # noqa: E501
        """
        pass

    def test_hess_api_site_site_id_cur_powerflow_get(self):
        """Test case for hess_api_site_site_id_cur_powerflow_get

        Current Power Flow  # noqa: E501
        """
        pass

    def test_hess_api_site_site_id_overview_get(self):
        """Test case for hess_api_site_site_id_overview_get

        Site Generation Overview  # noqa: E501
        """
        pass

    def test_hess_api_user_sites_list_get(self):
        """Test case for hess_api_user_sites_list_get

        Site List  # noqa: E501
        """
        pass


if __name__ == '__main__':
    unittest.main()

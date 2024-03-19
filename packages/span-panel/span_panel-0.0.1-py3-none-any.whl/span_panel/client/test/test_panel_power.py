"""
    Span

    Span Panel REST API

    The version of the OpenAPI document: v1
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""

from __future__ import annotations

import unittest

from span_panel.client.models.panel_power import PanelPower


class TestPanelPower(unittest.TestCase):
    """PanelPower unit test stubs"""

    def setUp(self):
        pass

    def tearDown(self):
        pass

    def make_instance(self, include_optional) -> PanelPower:
        """Test PanelPower
        include_option is a boolean, when False only required
        params are included, when True both required and
        optional params are included"""
        # uncomment below to create an instance of `PanelPower`
        """
        model = PanelPower()  # noqa: E501
        if include_optional:
            return PanelPower(
                instant_grid_power_w = 1.337,
                feedthrough_power_w = 1.337
            )
        else:
            return PanelPower(
                instant_grid_power_w = 1.337,
                feedthrough_power_w = 1.337,
        )
        """

    def testPanelPower(self):
        """Test PanelPower"""
        # inst_req_only = self.make_instance(include_optional=False)
        # inst_req_and_optional = self.make_instance(include_optional=True)


if __name__ == "__main__":
    unittest.main()

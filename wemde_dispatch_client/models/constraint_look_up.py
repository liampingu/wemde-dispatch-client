# coding: utf-8

"""
    WEMDE Dispatch

    No description provided (generated by Openapi Generator https://github.com/openapitools/openapi-generator)

    The version of the OpenAPI document: 1.0
    Generated by OpenAPI Generator (https://openapi-generator.tech)

    Do not edit the class manually.
"""  # noqa: E501


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing import Optional, Set
from typing_extensions import Self

class ConstraintLookUp(BaseModel):
    """
    ConstraintLookUp
    """ # noqa: E501
    forecast_regional_forecast_south_west_great_southern_region_base_load_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.regionalForecast-southWestGreatSouthernRegionBaseLoad-expected")
    forecast_regional_forecast_south_west_great_southern_region_load_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.regionalForecast-southWestGreatSouthernRegionLoad-expected")
    forecast_regional_forecast_north_country_region_load_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.regionalForecast-northCountryRegionLoad-expected")
    forecast_nsg_forecast_warradarge_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_walkaway_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_yandin_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_warradarge_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-bomAccessA-high")
    forecast_nsg_forecast_walkaway_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-bomAccessA-high")
    forecast_nsg_forecast_yandin_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-bomAccessA-high")
    forecast_nsg_forecast_warradarge_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-bomAccessA-low")
    forecast_nsg_forecast_walkaway_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-bomAccessA-low")
    forecast_nsg_forecast_yandin_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-bomAccessA-low")
    forecast_ess_regulation_raise_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.ess-regulationRaise-expected")
    forecast_ess_regulation_lower_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.ess-regulationLower-expected")
    forecast_ess_contingency_lower_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.ess-contingencyLower-expected")
    forecast_energy_forecast_operational_demand_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.energy-forecastOperationalDemand-expected")
    forecast_energy_forecast_operational_demand_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.energy-forecastOperationalDemand-high")
    forecast_energy_forecast_operational_demand_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.energy-forecastOperationalDemand-low")
    forecast_nsg_forecast_warradarge_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-wz-expected")
    forecast_nsg_forecast_walkaway_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-wz-expected")
    forecast_nsg_forecast_yandin_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-wz-expected")
    forecast_nsg_forecast_warradarge_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-wz-high")
    forecast_nsg_forecast_walkaway_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-wz-high")
    forecast_nsg_forecast_yandin_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-wz-high")
    forecast_nsg_forecast_warradarge_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-wz-low")
    forecast_nsg_forecast_walkaway_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-wz-low")
    forecast_nsg_forecast_yandin_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-wz-low")
    forecast_nsg_forecast_warradarge_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-bomCombined-expected")
    forecast_nsg_forecast_walkaway_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-bomCombined-expected")
    forecast_nsg_forecast_yandin_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-bomCombined-expected")
    forecast_nsg_forecast_warradarge_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-bomCombined-high")
    forecast_nsg_forecast_walkaway_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-bomCombined-high")
    forecast_nsg_forecast_yandin_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-bomCombined-high")
    forecast_nsg_forecast_warradarge_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-warradargeWindFarm-bomCombined-low")
    forecast_nsg_forecast_walkaway_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-walkawayWindFarm-bomCombined-low")
    forecast_nsg_forecast_yandin_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-yandinWindFarm-bomCombined-low")
    forecast_nsg_forecast_albany_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-wz-expected")
    forecast_nsg_forecast_badgingarra_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-wz-expected")
    forecast_nsg_forecast_albany_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_badgingarra_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_emu_downs_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-wz-expected")
    forecast_nsg_forecast_collgar_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_collgar_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-wz-expected")
    forecast_nsg_forecast_albany_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-bomCombined-expected")
    forecast_nsg_forecast_emu_downs_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_badgingarra_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-bomCombined-expected")
    forecast_nsg_forecast_mumbida_wind_farm_bom_access_a_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-bomAccessA-expected")
    forecast_nsg_forecast_collgar_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-bomCombined-expected")
    forecast_nsg_forecast_albany_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-bomAccessA-high")
    forecast_nsg_forecast_emu_downs_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-bomCombined-expected")
    forecast_nsg_forecast_badgingarra_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-bomAccessA-high")
    forecast_nsg_forecast_mumbida_wind_farm_bom_combined_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-bomCombined-expected")
    forecast_nsg_forecast_mumbida_wind_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-wz-expected")
    forecast_nsg_forecast_collgar_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-bomAccessA-high")
    forecast_nsg_forecast_albany_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-bomCombined-high")
    forecast_nsg_forecast_emu_downs_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-bomAccessA-high")
    forecast_nsg_forecast_albany_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-wz-high")
    forecast_nsg_forecast_badgingarra_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-bomCombined-high")
    forecast_nsg_forecast_mumbida_wind_farm_bom_access_a_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-bomAccessA-high")
    forecast_nsg_forecast_badgingarra_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-wz-high")
    forecast_nsg_forecast_collgar_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-bomCombined-high")
    forecast_nsg_forecast_albany_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-bomAccessA-low")
    forecast_nsg_forecast_emu_downs_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-wz-high")
    forecast_nsg_forecast_emu_downs_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-bomCombined-high")
    forecast_nsg_forecast_badgingarra_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-bomAccessA-low")
    forecast_nsg_forecast_collgar_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-wz-high")
    forecast_nsg_forecast_mumbida_wind_farm_bom_combined_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-bomCombined-high")
    forecast_nsg_forecast_collgar_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-bomAccessA-low")
    forecast_nsg_forecast_mumbida_wind_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-wz-high")
    forecast_nsg_forecast_albany_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-bomCombined-low")
    forecast_nsg_forecast_emu_downs_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-bomAccessA-low")
    forecast_nsg_forecast_albany_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-albanyWindFarm-wz-low")
    forecast_nsg_forecast_badgingarra_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-bomCombined-low")
    forecast_nsg_forecast_mumbida_wind_farm_bom_access_a_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-bomAccessA-low")
    forecast_nsg_forecast_badgingarra_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-badgingarraWindFarm-wz-low")
    forecast_nsg_forecast_collgar_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-bomCombined-low")
    forecast_nsg_forecast_emu_downs_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-wz-low")
    forecast_nsg_forecast_emu_downs_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-emuDownsWindFarm-bomCombined-low")
    forecast_nsg_forecast_collgar_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-collgarWindFarm-wz-low")
    forecast_nsg_forecast_mumbida_wind_farm_bom_combined_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-bomCombined-low")
    forecast_nsg_forecast_mumbida_wind_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mumbidaWindFarm-wz-low")
    forecast_nsg_forecast_mungara_solar_farm_bom_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mungaraSolarFarm-bom-expected")
    forecast_nsg_forecast_merredin_solar_farm_bom_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-merredinSolarFarm-bom-expected")
    forecast_nsg_forecast_mungara_solar_farm_bom_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mungaraSolarFarm-bom-high")
    forecast_nsg_forecast_merredin_solar_farm_bom_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-merredinSolarFarm-bom-high")
    forecast_nsg_forecast_mungara_solar_farm_bom_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mungaraSolarFarm-bom-low")
    forecast_nsg_forecast_merredin_solar_farm_bom_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-merredinSolarFarm-bom-low")
    forecast_nsg_forecast_merredin_solar_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-merredinSolarFarm-wz-expected")
    forecast_nsg_forecast_mungara_solar_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mungaraSolarFarm-wz-high")
    forecast_nsg_forecast_merredin_solar_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-merredinSolarFarm-wz-low")
    forecast_nsg_forecast_mungara_solar_farm_wz_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mungaraSolarFarm-wz-expected")
    forecast_nsg_forecast_merredin_solar_farm_wz_high: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-merredinSolarFarm-wz-high")
    forecast_nsg_forecast_mungara_solar_farm_wz_low: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.nsgForecast-mungaraSolarFarm-wz-low")
    forecast_regional_forecast_eastern_goldfields_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.regionalForecast-easternGoldfields-expected")
    forecast_regional_forecast_north_of_three_springs_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.regionalForecast-northOfThreeSprings-expected")
    forecast_regional_forecast_north_country_region_base_load_expected: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="forecast.regionalForecast-northCountryRegionBaseLoad-expected")
    solver_minutes_since_primary: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="solver.minutesSincePrimary")
    __properties: ClassVar[List[str]] = ["forecast.regionalForecast-southWestGreatSouthernRegionBaseLoad-expected", "forecast.regionalForecast-southWestGreatSouthernRegionLoad-expected", "forecast.regionalForecast-northCountryRegionLoad-expected", "forecast.nsgForecast-warradargeWindFarm-bomAccessA-expected", "forecast.nsgForecast-walkawayWindFarm-bomAccessA-expected", "forecast.nsgForecast-yandinWindFarm-bomAccessA-expected", "forecast.nsgForecast-warradargeWindFarm-bomAccessA-high", "forecast.nsgForecast-walkawayWindFarm-bomAccessA-high", "forecast.nsgForecast-yandinWindFarm-bomAccessA-high", "forecast.nsgForecast-warradargeWindFarm-bomAccessA-low", "forecast.nsgForecast-walkawayWindFarm-bomAccessA-low", "forecast.nsgForecast-yandinWindFarm-bomAccessA-low", "forecast.ess-regulationRaise-expected", "forecast.ess-regulationLower-expected", "forecast.ess-contingencyLower-expected", "forecast.energy-forecastOperationalDemand-expected", "forecast.energy-forecastOperationalDemand-high", "forecast.energy-forecastOperationalDemand-low", "forecast.nsgForecast-warradargeWindFarm-wz-expected", "forecast.nsgForecast-walkawayWindFarm-wz-expected", "forecast.nsgForecast-yandinWindFarm-wz-expected", "forecast.nsgForecast-warradargeWindFarm-wz-high", "forecast.nsgForecast-walkawayWindFarm-wz-high", "forecast.nsgForecast-yandinWindFarm-wz-high", "forecast.nsgForecast-warradargeWindFarm-wz-low", "forecast.nsgForecast-walkawayWindFarm-wz-low", "forecast.nsgForecast-yandinWindFarm-wz-low", "forecast.nsgForecast-warradargeWindFarm-bomCombined-expected", "forecast.nsgForecast-walkawayWindFarm-bomCombined-expected", "forecast.nsgForecast-yandinWindFarm-bomCombined-expected", "forecast.nsgForecast-warradargeWindFarm-bomCombined-high", "forecast.nsgForecast-walkawayWindFarm-bomCombined-high", "forecast.nsgForecast-yandinWindFarm-bomCombined-high", "forecast.nsgForecast-warradargeWindFarm-bomCombined-low", "forecast.nsgForecast-walkawayWindFarm-bomCombined-low", "forecast.nsgForecast-yandinWindFarm-bomCombined-low", "forecast.nsgForecast-albanyWindFarm-wz-expected", "forecast.nsgForecast-badgingarraWindFarm-wz-expected", "forecast.nsgForecast-albanyWindFarm-bomAccessA-expected", "forecast.nsgForecast-badgingarraWindFarm-bomAccessA-expected", "forecast.nsgForecast-emuDownsWindFarm-wz-expected", "forecast.nsgForecast-collgarWindFarm-bomAccessA-expected", "forecast.nsgForecast-collgarWindFarm-wz-expected", "forecast.nsgForecast-albanyWindFarm-bomCombined-expected", "forecast.nsgForecast-emuDownsWindFarm-bomAccessA-expected", "forecast.nsgForecast-badgingarraWindFarm-bomCombined-expected", "forecast.nsgForecast-mumbidaWindFarm-bomAccessA-expected", "forecast.nsgForecast-collgarWindFarm-bomCombined-expected", "forecast.nsgForecast-albanyWindFarm-bomAccessA-high", "forecast.nsgForecast-emuDownsWindFarm-bomCombined-expected", "forecast.nsgForecast-badgingarraWindFarm-bomAccessA-high", "forecast.nsgForecast-mumbidaWindFarm-bomCombined-expected", "forecast.nsgForecast-mumbidaWindFarm-wz-expected", "forecast.nsgForecast-collgarWindFarm-bomAccessA-high", "forecast.nsgForecast-albanyWindFarm-bomCombined-high", "forecast.nsgForecast-emuDownsWindFarm-bomAccessA-high", "forecast.nsgForecast-albanyWindFarm-wz-high", "forecast.nsgForecast-badgingarraWindFarm-bomCombined-high", "forecast.nsgForecast-mumbidaWindFarm-bomAccessA-high", "forecast.nsgForecast-badgingarraWindFarm-wz-high", "forecast.nsgForecast-collgarWindFarm-bomCombined-high", "forecast.nsgForecast-albanyWindFarm-bomAccessA-low", "forecast.nsgForecast-emuDownsWindFarm-wz-high", "forecast.nsgForecast-emuDownsWindFarm-bomCombined-high", "forecast.nsgForecast-badgingarraWindFarm-bomAccessA-low", "forecast.nsgForecast-collgarWindFarm-wz-high", "forecast.nsgForecast-mumbidaWindFarm-bomCombined-high", "forecast.nsgForecast-collgarWindFarm-bomAccessA-low", "forecast.nsgForecast-mumbidaWindFarm-wz-high", "forecast.nsgForecast-albanyWindFarm-bomCombined-low", "forecast.nsgForecast-emuDownsWindFarm-bomAccessA-low", "forecast.nsgForecast-albanyWindFarm-wz-low", "forecast.nsgForecast-badgingarraWindFarm-bomCombined-low", "forecast.nsgForecast-mumbidaWindFarm-bomAccessA-low", "forecast.nsgForecast-badgingarraWindFarm-wz-low", "forecast.nsgForecast-collgarWindFarm-bomCombined-low", "forecast.nsgForecast-emuDownsWindFarm-wz-low", "forecast.nsgForecast-emuDownsWindFarm-bomCombined-low", "forecast.nsgForecast-collgarWindFarm-wz-low", "forecast.nsgForecast-mumbidaWindFarm-bomCombined-low", "forecast.nsgForecast-mumbidaWindFarm-wz-low", "forecast.nsgForecast-mungaraSolarFarm-bom-expected", "forecast.nsgForecast-merredinSolarFarm-bom-expected", "forecast.nsgForecast-mungaraSolarFarm-bom-high", "forecast.nsgForecast-merredinSolarFarm-bom-high", "forecast.nsgForecast-mungaraSolarFarm-bom-low", "forecast.nsgForecast-merredinSolarFarm-bom-low", "forecast.nsgForecast-merredinSolarFarm-wz-expected", "forecast.nsgForecast-mungaraSolarFarm-wz-high", "forecast.nsgForecast-merredinSolarFarm-wz-low", "forecast.nsgForecast-mungaraSolarFarm-wz-expected", "forecast.nsgForecast-merredinSolarFarm-wz-high", "forecast.nsgForecast-mungaraSolarFarm-wz-low", "forecast.regionalForecast-easternGoldfields-expected", "forecast.regionalForecast-northOfThreeSprings-expected", "forecast.regionalForecast-northCountryRegionBaseLoad-expected", "solver.minutesSincePrimary"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of ConstraintLookUp from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ConstraintLookUp from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "forecast.regionalForecast-southWestGreatSouthernRegionBaseLoad-expected": obj.get("forecast.regionalForecast-southWestGreatSouthernRegionBaseLoad-expected"),
            "forecast.regionalForecast-southWestGreatSouthernRegionLoad-expected": obj.get("forecast.regionalForecast-southWestGreatSouthernRegionLoad-expected"),
            "forecast.regionalForecast-northCountryRegionLoad-expected": obj.get("forecast.regionalForecast-northCountryRegionLoad-expected"),
            "forecast.nsgForecast-warradargeWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-warradargeWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-walkawayWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-walkawayWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-yandinWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-yandinWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-warradargeWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-warradargeWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-walkawayWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-walkawayWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-yandinWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-yandinWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-warradargeWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-warradargeWindFarm-bomAccessA-low"),
            "forecast.nsgForecast-walkawayWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-walkawayWindFarm-bomAccessA-low"),
            "forecast.nsgForecast-yandinWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-yandinWindFarm-bomAccessA-low"),
            "forecast.ess-regulationRaise-expected": obj.get("forecast.ess-regulationRaise-expected"),
            "forecast.ess-regulationLower-expected": obj.get("forecast.ess-regulationLower-expected"),
            "forecast.ess-contingencyLower-expected": obj.get("forecast.ess-contingencyLower-expected"),
            "forecast.energy-forecastOperationalDemand-expected": obj.get("forecast.energy-forecastOperationalDemand-expected"),
            "forecast.energy-forecastOperationalDemand-high": obj.get("forecast.energy-forecastOperationalDemand-high"),
            "forecast.energy-forecastOperationalDemand-low": obj.get("forecast.energy-forecastOperationalDemand-low"),
            "forecast.nsgForecast-warradargeWindFarm-wz-expected": obj.get("forecast.nsgForecast-warradargeWindFarm-wz-expected"),
            "forecast.nsgForecast-walkawayWindFarm-wz-expected": obj.get("forecast.nsgForecast-walkawayWindFarm-wz-expected"),
            "forecast.nsgForecast-yandinWindFarm-wz-expected": obj.get("forecast.nsgForecast-yandinWindFarm-wz-expected"),
            "forecast.nsgForecast-warradargeWindFarm-wz-high": obj.get("forecast.nsgForecast-warradargeWindFarm-wz-high"),
            "forecast.nsgForecast-walkawayWindFarm-wz-high": obj.get("forecast.nsgForecast-walkawayWindFarm-wz-high"),
            "forecast.nsgForecast-yandinWindFarm-wz-high": obj.get("forecast.nsgForecast-yandinWindFarm-wz-high"),
            "forecast.nsgForecast-warradargeWindFarm-wz-low": obj.get("forecast.nsgForecast-warradargeWindFarm-wz-low"),
            "forecast.nsgForecast-walkawayWindFarm-wz-low": obj.get("forecast.nsgForecast-walkawayWindFarm-wz-low"),
            "forecast.nsgForecast-yandinWindFarm-wz-low": obj.get("forecast.nsgForecast-yandinWindFarm-wz-low"),
            "forecast.nsgForecast-warradargeWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-warradargeWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-walkawayWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-walkawayWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-yandinWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-yandinWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-warradargeWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-warradargeWindFarm-bomCombined-high"),
            "forecast.nsgForecast-walkawayWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-walkawayWindFarm-bomCombined-high"),
            "forecast.nsgForecast-yandinWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-yandinWindFarm-bomCombined-high"),
            "forecast.nsgForecast-warradargeWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-warradargeWindFarm-bomCombined-low"),
            "forecast.nsgForecast-walkawayWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-walkawayWindFarm-bomCombined-low"),
            "forecast.nsgForecast-yandinWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-yandinWindFarm-bomCombined-low"),
            "forecast.nsgForecast-albanyWindFarm-wz-expected": obj.get("forecast.nsgForecast-albanyWindFarm-wz-expected"),
            "forecast.nsgForecast-badgingarraWindFarm-wz-expected": obj.get("forecast.nsgForecast-badgingarraWindFarm-wz-expected"),
            "forecast.nsgForecast-albanyWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-albanyWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-badgingarraWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-badgingarraWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-emuDownsWindFarm-wz-expected": obj.get("forecast.nsgForecast-emuDownsWindFarm-wz-expected"),
            "forecast.nsgForecast-collgarWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-collgarWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-collgarWindFarm-wz-expected": obj.get("forecast.nsgForecast-collgarWindFarm-wz-expected"),
            "forecast.nsgForecast-albanyWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-albanyWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-emuDownsWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-emuDownsWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-badgingarraWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-badgingarraWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-mumbidaWindFarm-bomAccessA-expected": obj.get("forecast.nsgForecast-mumbidaWindFarm-bomAccessA-expected"),
            "forecast.nsgForecast-collgarWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-collgarWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-albanyWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-albanyWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-emuDownsWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-emuDownsWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-badgingarraWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-badgingarraWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-mumbidaWindFarm-bomCombined-expected": obj.get("forecast.nsgForecast-mumbidaWindFarm-bomCombined-expected"),
            "forecast.nsgForecast-mumbidaWindFarm-wz-expected": obj.get("forecast.nsgForecast-mumbidaWindFarm-wz-expected"),
            "forecast.nsgForecast-collgarWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-collgarWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-albanyWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-albanyWindFarm-bomCombined-high"),
            "forecast.nsgForecast-emuDownsWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-emuDownsWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-albanyWindFarm-wz-high": obj.get("forecast.nsgForecast-albanyWindFarm-wz-high"),
            "forecast.nsgForecast-badgingarraWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-badgingarraWindFarm-bomCombined-high"),
            "forecast.nsgForecast-mumbidaWindFarm-bomAccessA-high": obj.get("forecast.nsgForecast-mumbidaWindFarm-bomAccessA-high"),
            "forecast.nsgForecast-badgingarraWindFarm-wz-high": obj.get("forecast.nsgForecast-badgingarraWindFarm-wz-high"),
            "forecast.nsgForecast-collgarWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-collgarWindFarm-bomCombined-high"),
            "forecast.nsgForecast-albanyWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-albanyWindFarm-bomAccessA-low"),
            "forecast.nsgForecast-emuDownsWindFarm-wz-high": obj.get("forecast.nsgForecast-emuDownsWindFarm-wz-high"),
            "forecast.nsgForecast-emuDownsWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-emuDownsWindFarm-bomCombined-high"),
            "forecast.nsgForecast-badgingarraWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-badgingarraWindFarm-bomAccessA-low"),
            "forecast.nsgForecast-collgarWindFarm-wz-high": obj.get("forecast.nsgForecast-collgarWindFarm-wz-high"),
            "forecast.nsgForecast-mumbidaWindFarm-bomCombined-high": obj.get("forecast.nsgForecast-mumbidaWindFarm-bomCombined-high"),
            "forecast.nsgForecast-collgarWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-collgarWindFarm-bomAccessA-low"),
            "forecast.nsgForecast-mumbidaWindFarm-wz-high": obj.get("forecast.nsgForecast-mumbidaWindFarm-wz-high"),
            "forecast.nsgForecast-albanyWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-albanyWindFarm-bomCombined-low"),
            "forecast.nsgForecast-emuDownsWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-emuDownsWindFarm-bomAccessA-low"),
            "forecast.nsgForecast-albanyWindFarm-wz-low": obj.get("forecast.nsgForecast-albanyWindFarm-wz-low"),
            "forecast.nsgForecast-badgingarraWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-badgingarraWindFarm-bomCombined-low"),
            "forecast.nsgForecast-mumbidaWindFarm-bomAccessA-low": obj.get("forecast.nsgForecast-mumbidaWindFarm-bomAccessA-low"),
            "forecast.nsgForecast-badgingarraWindFarm-wz-low": obj.get("forecast.nsgForecast-badgingarraWindFarm-wz-low"),
            "forecast.nsgForecast-collgarWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-collgarWindFarm-bomCombined-low"),
            "forecast.nsgForecast-emuDownsWindFarm-wz-low": obj.get("forecast.nsgForecast-emuDownsWindFarm-wz-low"),
            "forecast.nsgForecast-emuDownsWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-emuDownsWindFarm-bomCombined-low"),
            "forecast.nsgForecast-collgarWindFarm-wz-low": obj.get("forecast.nsgForecast-collgarWindFarm-wz-low"),
            "forecast.nsgForecast-mumbidaWindFarm-bomCombined-low": obj.get("forecast.nsgForecast-mumbidaWindFarm-bomCombined-low"),
            "forecast.nsgForecast-mumbidaWindFarm-wz-low": obj.get("forecast.nsgForecast-mumbidaWindFarm-wz-low"),
            "forecast.nsgForecast-mungaraSolarFarm-bom-expected": obj.get("forecast.nsgForecast-mungaraSolarFarm-bom-expected"),
            "forecast.nsgForecast-merredinSolarFarm-bom-expected": obj.get("forecast.nsgForecast-merredinSolarFarm-bom-expected"),
            "forecast.nsgForecast-mungaraSolarFarm-bom-high": obj.get("forecast.nsgForecast-mungaraSolarFarm-bom-high"),
            "forecast.nsgForecast-merredinSolarFarm-bom-high": obj.get("forecast.nsgForecast-merredinSolarFarm-bom-high"),
            "forecast.nsgForecast-mungaraSolarFarm-bom-low": obj.get("forecast.nsgForecast-mungaraSolarFarm-bom-low"),
            "forecast.nsgForecast-merredinSolarFarm-bom-low": obj.get("forecast.nsgForecast-merredinSolarFarm-bom-low"),
            "forecast.nsgForecast-merredinSolarFarm-wz-expected": obj.get("forecast.nsgForecast-merredinSolarFarm-wz-expected"),
            "forecast.nsgForecast-mungaraSolarFarm-wz-high": obj.get("forecast.nsgForecast-mungaraSolarFarm-wz-high"),
            "forecast.nsgForecast-merredinSolarFarm-wz-low": obj.get("forecast.nsgForecast-merredinSolarFarm-wz-low"),
            "forecast.nsgForecast-mungaraSolarFarm-wz-expected": obj.get("forecast.nsgForecast-mungaraSolarFarm-wz-expected"),
            "forecast.nsgForecast-merredinSolarFarm-wz-high": obj.get("forecast.nsgForecast-merredinSolarFarm-wz-high"),
            "forecast.nsgForecast-mungaraSolarFarm-wz-low": obj.get("forecast.nsgForecast-mungaraSolarFarm-wz-low"),
            "forecast.regionalForecast-easternGoldfields-expected": obj.get("forecast.regionalForecast-easternGoldfields-expected"),
            "forecast.regionalForecast-northOfThreeSprings-expected": obj.get("forecast.regionalForecast-northOfThreeSprings-expected"),
            "forecast.regionalForecast-northCountryRegionBaseLoad-expected": obj.get("forecast.regionalForecast-northCountryRegionBaseLoad-expected"),
            "solver.minutesSincePrimary": obj.get("solver.minutesSincePrimary")
        })
        return _obj



from abm.space.geospace.base import BaseGeoSpace
from abm.visualizations.modules.MapModule import MapModule

from mesa.datacollection import DataCollector
"""
from abm.models.enum.age_group import AgeGroup

from abm.utils.collectors.geospatial.total_susceptible import get_localized_susceptible
from abm.utils.collectors.geospatial.total_exposed import get_localized_exposed
from abm.utils.collectors.geospatial.total_infected import get_localized_infected
from abm.utils.collectors.geospatial.total_deaths import get_localized_death
from abm.utils.collectors.geospatial.total_recovered import get_localized_recovered
from abm.utils.collectors.geospatial.total_vaccinated import get_localized_vaccinated
from abm.utils.collectors.geospatial.total_vaccinated_age_group import get_localized_vaccine_distribution

from abm.utils.modules.optimization.vaccine_distribution_optimization import vaccine_distribution_optimization
from abm.utils.modules.json_updater import json_updater

from abm.visualizations.charts.summary import SummaryChartModule
from abm.visualizations.charts.distribution import DistributionChartModule
"""
#from abm.visualizations.elements.label import Label
from abm.visualizations.portrayals.geospatial import agent_portrayal


import numpy as np
import pandas as pd
import json

class GeoSpaceEnvironment:

    def __init__(self, 
        model, 
        geojson_file, 
        geojson_feature_key, 
        locations, 
        center_coords, 
        population,
        scale = 1000):

        self.model                  = model
        self.geo_space              = BaseGeoSpace(
                                        model = model, 
                                        geojson_file = geojson_file, 
                                        geojson_feature_key = geojson_feature_key, 
                                        nlocations = len(locations)
                                    )
                                    
        self.center_coords          = center_coords
        self.locations              = locations
        self.population             = population

        self.map                    = self.get_map()
        self.agent_locations        = self.get_geospace().agents

        self.data                   = []
        self.scale                  = scale
        self.initialized_data()
        
    def initialized_agents(self, shape_idx, gender, migrant_type, population, **kwargs):
        
        location = "loc_" + str(shape_idx)
        
        for person in range(int(np.ceil(population))):
            
            pox_x, pos_y = self.grid.random_position(location)
            age = 1
        
        
            
    def get_geospace(self):
        return self.geo_space
        
    def get_map(self, zoom = 6, width = 960, height = 480):
        return MapModule(
            portrayal_method = agent_portrayal,
            view = self.center_coords,
            zoom = zoom,
            map_height = height,
            map_width = width
        )
            
                
    def initialized_data(self):
        print("Initializing the data ...")
        for idx, agent in enumerate(self.agent_locations):
            self.data.append(
                {
                    "LOCATION_NAME": repr(agent),
                    "IDX" : idx
                }
            )
            
    
        

        
            

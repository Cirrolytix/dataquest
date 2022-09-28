from mesa import Model
from mesa.time import RandomActivation
from mesa.datacollection import DataCollector

from abm.models.agents.geospatial.person import Person

from abm.models.enum.age_group import AgeGroup
from abm.models.enum.gender import Gender
from abm.models.enum.migrant_type import MigrantType

from shapely.geometry import Point

import numpy as np

class GeoSimulationEnvironment(Model):
    
    description = (
        """
        agent-based model 
        """
    )

    def __init__(
        self,
        
        density     = 0.8, 
        minority_pc = 0.2, 
        homophily   = 3,
        purchasing_power = 0.1,
        inflation = 0.1,
        internal_migrants = 0.1,
        intl_migrants = 0.1,
        intended_migrants = 0.1,
        remittance = 0.1,
        employment = 0.1,
        youth = 0.1,
        unemployment = 0.1,
        tenure = 0.1,
        skill_1 = True,
        skill_2 = True,
        skill_3 = True,
        skill_4 = True,
        skill_5 = True,
        skill_6 = True,
        skill_7 = True,
        skill_8 = True,
        skill_9 = True,
        environment = object
        ):
    
        self.density     = density
        self.minority_pc = minority_pc
        self.homophily   = homophily

        self.purchasing_power = purchasing_power
        self.inflation = inflation

        self.day         = 0

        self.schedule    = RandomActivation(self)
        self.running     = True
        #self.grid        = environment.get_geospace()

        
    def initialized_all_agents(self):
        for shape_idx, location_data in enumerate(self.environment.data, start = 1):

            print("Initializing Agents for {0}".format(location_data["LOCATION_NAME"]))
                                    
            self.initialized_agents(shape_idx, MigrantType.Local, 1000)
            self.initialized_agents(shape_idx, MigrantType.Local, 1000)


    def step(self):
        self.day += 1
        self.schedule.step()

        self.grid._recreate_rtree()

    def roll_probability(self, threshold):
        return np.random.uniform(0.0, 1.0) < threshold
    
    def randomized_age(self):        
        rand_ages = []
        for age in range(9):
            rand_ages.append(np.random.randint(10 * age, 10 * age + 9))
            
        return rand_ages

    def initialized_agents(self, shape_idx, migrant_type, population, **kwargs):
        
        location = "loc_" + str(shape_idx)
                
        for i in range(int(np.ceil(population))): 
                       
            pos_x, pos_y = self.grid.random_position(location)
            age          = int(np.random.choice(self.randomized_age(), p = 0.6))                            
                
            agent = Person(
                model               = self,
                shape               = Point(pos_x, pos_y),
                migrant_type        = migrant_type,
                age                 = 25.9,
                skills              = 0.5,
                satisfaction        = 0.5,
                cash_liquidity      = 1000
            )

            self.grid.add_agents(agent)
            self.schedule.add(agent)     

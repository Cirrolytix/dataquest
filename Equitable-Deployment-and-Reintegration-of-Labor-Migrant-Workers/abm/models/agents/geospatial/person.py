from mesa_geo.geoagent import GeoAgent

import numpy as np
import uuid
from shapely.geometry import Point

from abm.models.enum.age_group import AgeGroup
from abm.models.enum.gender import Gender
from abm.models.enum.migrant_type import MigrantType


class Person(GeoAgent):
    """
    Schelling Segregation Person agent
    """

    def __init__(self, 
        model, 
        shape, 
        migrant_type,
        age = 25.9,
        gender = Gender.Female,
        skills = 0.5,
        satisfaction = 0.5,
        cash_liquidity = 1000
        ):
        
        """
        Create a new Schelling agent.

        Args:
           unique_id: Unique identifier for the agent.
           x, y: Agent initial location.
           agent_type: Indicator for the agent's type (minority=1, majority=0)
        """
        super().__init__(uuid.uuid4().hex, model, shape)
        self.unique_id      = uuid.uuid4().hex
        self.model          = model

        self.migrant_type   = migrant_type
        self.age            = age
        self.skills         = skills
        self.satisfaction   = satisfaction
        self.cash_liquidity = cash_liquidity

        self.set_age_group()

    def set_age_group(self):
      if (self.age >= 0) and (self.age <= 19):
        self.age_group = AgeGroup.A00to19
      elif (self.age >= 20) and (self.age <= 39):
        self.age_group = AgeGroup.A20to39
      elif (self.age >= 40) and (self.age <= 59):
        self.age_group = AgeGroup.A40to59
      elif (self.age >= 60):
        self.age_group = AgeGroup.A60toXX

    def get_migrant_type(self):
        return self.migrant_type

    def set_as_local_migrant(self):
        self.migrant_type = MigrantType.Local

    def set_as_intl_migrant(self):
        self.migrant_type = MigrantType.International

    def is_local_migrant(self):
      return self.get_migrant_type() == MigrantType.Local

    def is_intl_migrant(self):
      return self.get_migrant_type() == MigrantType.International

    def roll_probability(self, threshold):      
      return np.random.uniform(0.0, 1.0) <= threshold

    def update_cash_liquidity(self):

        if self.roll_probability(threshold = 0.75):

            if self.is_intl_migrant():
                self.cash_liquidity = self.cash_liquidity * (1 + 0.087)

            if self.is_local_migrant():
                self.cash_liquidity = self.cash_liquidity * (1 - 0.087)

    def is_below_cash_liquidity(self, threshold = 700):
        if self.cash_liquidity <= threshold:
            self.set_as_intl_migrant()

    # Logic in terms of Time Step
    def step(self):
        neighbors = self.model.grid.get_neighbors_within_distance(self, 500)
        for neighbor in neighbors:
            if isinstance(neighbor, Person):

                self.update_cash_liquidity()
                
                # Add Logic here for Migrant Worker
                
                if self.is_intl_migrant():
                    if self.is_below_cash_liquidity():
                        self.move()
                        
                if self.is_local_migrant():
                    if self.is_below_cash_liquidity():
                        self.move()

    # Logic in terms of Movement
    def move(self):
        self.move_to_next()

    # Function to Move in terms of Space
    def move_to_next(self):
        new_x = self.shape.x + self.random.randint(-100, 100)
        new_y = self.shape.y + self.random.randint(-100, 100)
        self.shape = Point(new_x, new_y)
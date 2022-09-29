from abm.models.agents.geospatial.person import Person
from abm.space.geoagents.base import BaseGeoAgent

def agent_portrayal(agent):
    if agent is None:
        return
    
    portrayal = {}
    
    if isinstance(agent, Person):
        portrayal = {
            "radius":                           "1",
            "Shape":                            "Circle", 
            "Age":                              int(agent.age)
        }


    elif isinstance(agent, BaseGeoAgent):
        portrayal = { "color": "Blue" }

    return portrayal



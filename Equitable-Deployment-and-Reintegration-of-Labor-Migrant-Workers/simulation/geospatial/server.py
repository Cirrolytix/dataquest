import os

from mesa.visualization.ModularVisualization import ModularServer
from mesa.visualization.UserParam import UserSettableParameter


from simulation.geospatial.model import GeoSimulationEnvironment
from abm.space.geospace import GeoSpaceEnvironment
from abm.space.geojson.constants import PH_MAP_GEOJSON

PORT = os.environ.get('PORT', '8524')


simulation_model        = GeoSimulationEnvironment
center_coords           = [12.5706885,122.6795535]

performance_factor       = 40
scale                    = 1000 * performance_factor  

"""
"properties": {
    "Shape_Leng": 390.774375451,
    "Shape_Area": 24.5388565131,
    "ADM0_EN": "Philippines (the)",
    "ADM0_PCODE":"PH",
    "ADM0_REF":"",
    "ADM0ALT1EN":"",
    "ADM0ALT2EN":"",
    "date":"2018-01-26T00:00:00.000Z",
    "validOn":"2018-01-30T00:00:00.000Z",
    "validTo":"1899-11-30T00:00:00.000Z"
}
"""

locations  = ["Philippines"]
population = [100000]

environment             = GeoSpaceEnvironment(
                            model               = simulation_model, 
                            geojson_file        = PH_MAP_GEOJSON, 
                            geojson_feature_key = "NAME_ISO", 
                            locations           = locations, 
                            center_coords       = center_coords, 
                            population          = population,
                            scale = 1000)

environment.scale       = scale

environment.data        = {
    "LOCATION_NAME": "Philippines",
    "POPULATION": 1000,
    "SCALE": 1000,
    "JOB_AVAILABLE": 1000,
    "DATA" : {

    }

}

simulation_model.grid   = environment.get_geospace()

components = [
    environment.map
]

internal_migrants_option            = UserSettableParameter('checkbox', 'Internal Migrants', value = True)
intl_migrants_option                = UserSettableParameter('checkbox', 'International Migrants', value = True)
intended_migrants_option            = UserSettableParameter('checkbox', 'Intended Migration Destination', value = True)
remittance_option                   = UserSettableParameter('checkbox', 'Persons with Functional Difficulty', value = True)

employment_option             = UserSettableParameter('checkbox', 'Employment to Population ratio', value = True)
youth_option                  = UserSettableParameter('checkbox', 'Share of youth not in education, employment or training', value = True)
unemployment_option           = UserSettableParameter('checkbox', 'Unemployment', value = True)
tenure_option                 = UserSettableParameter('checkbox', 'Tenure', value = True)

skill_1_option = UserSettableParameter('checkbox', 'Automotive and Land Transportation', value = True)
skill_2_option = UserSettableParameter('checkbox', 'Human Health / Health Care', value = True)
skill_3_option = UserSettableParameter('checkbox', 'Information and Communication Technology', value = True)
skill_4_option = UserSettableParameter('checkbox', 'Logistics', value = True)
skill_5_option = UserSettableParameter('checkbox', 'Maritime', value = True)
skill_6_option = UserSettableParameter('checkbox', 'Metals and Engineering', value = True)
skill_7_option = UserSettableParameter('checkbox', 'Maritime', value = True)
skill_8_option = UserSettableParameter('checkbox', 'Social, Community Development and Other Services', value = True)
skill_9_option = UserSettableParameter('checkbox', 'Tourism (Hotel and Restaurant)', value = True)

inflation          = UserSettableParameter("slider", "Inflation", 0.00, 0.00, 1.0, 0.01)
purchasing_power   = UserSettableParameter("slider", "Purchasing Power", 0, 0.5, 2.0, 0.1)

model_params = {
    "model_desc":  UserSettableParameter('static_text', value = "Policy Making Parameters"),
    "economic_lbl":  UserSettableParameter('static_text', value = "Economic Factors"),
    "purchasing_power" : purchasing_power,
    "inflation" : inflation,
    "deployment_lbl":  UserSettableParameter('static_text', value = "Deployment of Migrant Workers"),
    "internal_migrants": intended_migrants_option,
    "intl_migrants": intl_migrants_option,
    "intended_migrants": intended_migrants_option,
    "remittance":  remittance_option,
    "reintegration_lbl":  UserSettableParameter('static_text', value = "Reintegration of Migrant Workers"),
    "employment": employment_option,
    "youth": youth_option,
    "unemployment": unemployment_option,
    "tenure": tenure_option,
    "skills_lbl":  UserSettableParameter('static_text', value = "Skills of Migrant Workers"),
    "skill_1": skill_1_option,
    "skill_2": skill_2_option,
    "skill_3": skill_3_option,
    "skill_4": skill_4_option,
    "skill_5": skill_5_option,
    "skill_6": skill_6_option,
    "skill_7": skill_7_option,
    "skill_8": skill_8_option,
    "skill_9": skill_9_option,
    "environment": environment
}

server = ModularServer(
    simulation_model,
    components,
    "Equitable Deployment and Reintegration of Labor Migrant Workers",
    model_params = model_params)

server.port = PORT

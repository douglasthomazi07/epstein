import mesa

from .model import EpsteinCivilViolence
from .agent import Citizen, Cop


COP_COLOR = "#000000"
AGENT_QUIET_COLOR = "#0066CC"
AGENT_REBEL_COLOR = "#CC0000"
JAIL_COLOR = "#757575"


def citizen_cop_portrayal(agent):
    if agent is None:
        return

    portrayal = {
        "Shape": "circle",
        "x": agent.pos[0],
        "y": agent.pos[1],
        "Filled": "true",
    }

    if type(agent) is Citizen:
        color = (
            AGENT_QUIET_COLOR if agent.condition == "Quiescent" else AGENT_REBEL_COLOR
        )
        color = JAIL_COLOR if agent.jail_sentence else color
        portrayal["Color"] = color
        portrayal["r"] = 0.8
        portrayal["Layer"] = 0

    elif type(agent) is Cop:
        portrayal["Color"] = COP_COLOR
        portrayal["r"] = 0.5
        portrayal["Layer"] = 1
    return portrayal

canvas_element = mesa.visualization.CanvasGrid(citizen_cop_portrayal, 20, 20, 500, 500)
chart_element = mesa.visualization.ChartModule(
    [
        {"Label": "Quiescent", "Color": AGENT_QUIET_COLOR},
        {"Label": "Active", "Color": AGENT_REBEL_COLOR},
        {"Label": "Jailed", "Color": JAIL_COLOR},
    ]
)

model_params = dict(
    height=40,
    width=40,
    citizen_density = mesa.visualization.Slider("Citizen Density", 0.7, 0.1, 0.7, 0.1),
    cop_density= mesa.visualization.Slider("Cop Density", 0.074, 0.00, 0.3, 0.01),
    citizen_vision=mesa.visualization.Slider("Citizen Vision", 7, 3, 10, 1),
    cop_vision=mesa.visualization.Slider("Cop Vision", 7, 3, 10, 1),
    legitimacy=mesa.visualization.Slider("Legitimacy", 0.8, 0.5, 1, 0.1),
    max_jail_term=1000,
)

canvas_element = mesa.visualization.CanvasGrid(citizen_cop_portrayal, 40, 40, 480, 480)
server = mesa.visualization.ModularServer(
    EpsteinCivilViolence, [canvas_element, chart_element], "Epstein Civil Violence", model_params
)

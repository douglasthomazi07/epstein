from unittest import result
from epstein_civil_violence.model import EpsteinCivilViolence
from mesa import batch_run
from datetime import datetime
import numpy as np
import pandas as pd

params={"height":30, "width":30, "citizen_density": np.arange(0.3, 0.7, 0.2), "cop_density": np.arange(0.1, 0.4, 0.1),"citizen_vision":7,
        "cop_vision":7,
        "legitimacy":np.arange(0.2, 0.9, 0.3), "max_jail_term":1000}

results=batch_run(EpsteinCivilViolence, parameters=params, iterations=20, max_steps=40, number_processes=1, data_collection_period=-1, display_progress=True)

results_csv = pd.DataFrame(results)

results_csv.to_csv(datetime.now().strftime("%d-%m-%Y-%H:%M" + "experimento.csv"))

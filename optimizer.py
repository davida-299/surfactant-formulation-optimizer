# Surfactant Formulation Optimizer
# Uses industrial experience to suggest greener formulations

import pandas as pd

def suggest_formulation(target="biodegradable_dishwash"):
    formulations = {
        "biodegradable_dishwash": {
            "surfactant": "Alkyl Polyglucoside 15%",
            "co-surfactant": "Cocamidopropyl Betaine 5%",
            "solvent": "Water 78%",
            "note": "100% plant-based, low LogP"
        },
        "low_cost_industrial": {
            "surfactant": "SLES 20%",
            "co-surfactant": "LABSA 5%",
            "solvent": "Water 73%",
            "note": "Cost-effective but check biodegradability"
        }
    }
    return formulations.get(target, "Formulation not found")

print(suggest_formulation("biodegradable_dishwash"))

import pandas as pd

def summarize_driver_stats(results_df):
    results_df["position"] = results_df["position"].astype(str) 
    results_df["grid"] = results_df["grid"].astype(str)

    wins = len(results_df[results_df["position"] == "1"])
    podiums = len(results_df[results_df["position"].isin(["1", "2", "3"])])
    poles = len(results_df[results_df["grid"] == "1"])
    dnfs = len(results_df[~results_df["status"].str.contains("Finished")])

    return {
        "Wins": wins,
        "Podiums": podiums,
        "Pole Positions": poles,
        "DNFs": dnfs
    }

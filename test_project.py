from analysis import summarize_driver_stats
import pandas as pd

def test_summarize_driver_stats():
    data = {
        "position": ["1", "2", "3", "4", "1", "DNF", "DNF"],
        "grid": ["1", "2", "3", "4", "1", "5", "6"],
        "status": ["Finished", "Finished", "Finished", "Finished", "Finished", "Accident", "Gearbox"]
    }
    df = pd.DataFrame(data)
    stats = summarize_driver_stats(df)

    assert stats["Wins"] == 2
    assert stats["Podiums"] == 4
    assert stats["Pole Positions"] == 2
    assert stats["DNFs"] == 2
    print("All tests passed.")

if __name__ == "__main__":
    test_summarize_driver_stats()

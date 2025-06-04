from api import get_driver_results, get_driver_standings
from analysis import summarize_driver_stats
from plot import plot_driver_points
from prettytable import PrettyTable

def validate_input(prompt, valid_type):
    while True:
        user_input = input(prompt)
        try:
            return valid_type(user_input)
        except ValueError:
            print("Invalid input. Please enter a valid format.")

def get_driver_data(driver_id, start_year, end_year):
    results = get_driver_results(driver_id, start_year, end_year)
    standings = get_driver_standings(driver_id, start_year, end_year)
    return results, standings

def compare_driver_stats(driver1, driver2, stats1, stats2):
    """Create and display a head-to-head comparison table."""
    table = PrettyTable()
    table.field_names = ["Metric", driver1.title(), driver2.title()]
    for key in stats1:
        table.add_row([key, stats1[key], stats2[key]])

    print("\nHead-to-Head Comparison:")
    print(table)

def plot_comparison_graph(driver1, driver2, df1_points, df2_points):
    if df1_points.empty or df2_points.empty:
        print("Error: Points data unavailable. Skipping graph.")
    else:
        plot_driver_points(df1_points, df2_points, driver1.title(), driver2.title())

def main():
    d1 = input("Enter first driver ID (e.g., hamilton): ").lower().strip()
    d2 = input("Enter second driver ID (e.g., max_verstappen): ").lower().strip()
    start = validate_input("Start year: ", int)
    end = validate_input("End year: ", int)

    results1, df1_points = get_driver_data(d1, start, end)
    results2, df2_points = get_driver_data(d2, start, end)

    if results1.empty or results2.empty:
        print("Error: Could not retrieve data for one or both drivers. Please check your inputs.")
        return

    stats1 = summarize_driver_stats(results1)
    stats2 = summarize_driver_stats(results2)

    compare_driver_stats(d1, d2, stats1, stats2)
    plot_comparison_graph(d1, d2, df1_points, df2_points)

if __name__ == "__main__":
    main()

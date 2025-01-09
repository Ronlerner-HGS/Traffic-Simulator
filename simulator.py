import pandas as pd

# Load the data from the Excel file
df = pd.read_excel("traffic_data.xlsx")


# Function to simulate traffic for a given time interval
def simulate_traffic_for_interval(cars_at_start, arriving_rate, passing_rate, red_light_duration=30,
                                  green_light_duration=30):
    """
    Simulate traffic flow for multiple red-green traffic light cycle.

    Args:
        cars_at_start (int): The number of cars waiting at the start of the cycle.
        arriving_rate (float): The rate at which cars arrive per minute during the red light.
        passing_rate (int): The rate at which cars can pass through the intersection per minute during the green light.
        red_light_duration (int, optional): The duration of the red light in seconds. Defaults to 30 seconds.
        green_light_duration (int, optional): The duration of the green light in seconds. Defaults to 30 seconds.

    Returns:
        dict: A dictionary with the following keys:
            - "Cars stopping at red" (float): Total cars stopped at the red light.
            - "Cars passing through" (int): Total cars that passed the intersection during the green light.
            - "Cars arriving" (float): Cars arriving during the red light.
            - "Cars remaining after cycle" (float): Cars left waiting after the red and green light cycle.    """
    # Cars arriving during red light (rate is per minute, so adjusting for seconds)
    cars_arriving = arriving_rate * (red_light_duration / 60)
    # Cars stopping at red
    cars_stopping = cars_at_start + cars_arriving

    # Calculate how many cars can pass during green light
    green_time_in_minutes = green_light_duration / 60
    cars_passed = min(cars_stopping, int(passing_rate * green_time_in_minutes))
    cars_remaining = cars_stopping - cars_passed  # Cars remaining after green ends

    return {
        "Cars stopping at red": cars_stopping,
        "Cars passing through": cars_passed,
        "Cars arriving": cars_arriving,
        "Cars remaining after cycle": cars_remaining
    }


# Loop through the data and simulate traffic for each time interval
time_intervals = df['Time Interval'].unique()
for interval in time_intervals:
    # Filter data for the current time interval
    interval_data = df[df['Time Interval'] == interval]

    total_cars_arriving = interval_data['Count'].sum()

    # Assume an initial number of cars waiting (e.g., start with 0 or some other baseline)
    initial_cars = 0
    passing_rate = 10  # This will be adjusted with more data

    # Simulate the traffic for this time interval
    result = simulate_traffic_for_interval(initial_cars, total_cars_arriving, passing_rate)

    print(f"Simulation for Time Interval: {interval}")
    for label, value in result.items():
        print(f"{label}: {value}")
    print("\n")

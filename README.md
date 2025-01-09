# Traffic Simulation System
## Overview
This project provides a traffic simulation system that models the flow of vehicles through a red-green traffic light cycle for one or more time intervals. It is implemented using **Python** and leverages the **pandas** library to handle the input dataset containing traffic data.
The script analyzes traffic flow based on configurable parameters, such as:
- **Red light duration**: Time during which cars stop at the traffic signal.
- **Green light duration**: Time during which cars are allowed to pass through.
- **Car arrival rate**: Number of cars arriving at the intersection per minute.
- **Car passing rate**: Number of cars passing through the traffic light during the green light.

This simulation helps identify traffic bottlenecks, efficiently manage traffic flow, and optimize traffic light timing.
## Features
1. **Data-Driven Traffic Analysis**:
    - The system uses real-world traffic data stored in an Excel sheet (`traffic_data.xlsx`) to perform simulations for user-defined time intervals.

2. **Configurable Parameters**:
    - The simulation allows customization of red/green light durations, arrival rates, and passing rates for flexible modeling.

3. **Output Metrics**:
    - For each time interval, the program provides insights into:
        - Cars arriving during the red light.
        - Cars stopping at the red light.
        - Cars passing through during the green light.
        - Cars remaining after the complete cycle.

4. **Scalable Design**:
    - The program is designed to loop efficiently through multiple time intervals, scaling easily for larger datasets.

## Justification of the Code
The approach taken in the traffic simulation script ensures accuracy, simplicity, and extensibility. Here are key aspects and justifications:
1. **Separation of Responsibilities**:
    - The simulation logic is encapsulated in the function `simulate_traffic_for_interval`. This allows easy reuse and testing of the simulation model independently of the data processing logic.

2. **Realistic Traffic Modeling**:
    - By incorporating both red and green light durations, the function realistically mimics the way vehicles arrive, stop, and pass through an intersection at different times.

3. **Data-Driven Analysis**:
    - By sourcing input from an external Excel file using **pandas**, the solution integrates seamlessly with traffic datasets and produces time-interval-based insights.

4. **Customizable Parameters**:
    - The ability to vary parameters like passing rate, arrival rate, and signal timings empowers users to simulate a wide range of traffic conditions and scenarios.

5. **Focus on Usability**:
    - The program prints human-readable outputs for each time interval, making it easy for stakeholders (e.g., traffic engineers) to interpret results without additional processing.

6. **Scalable Framework**:
    - The loop that processes individual time intervals ensures that the system can scale to handle large datasets efficiently.

## Installation
1. **Python Version**: Ensure Python 3.13 or higher is installed on your system.
2. **Install Dependencies**: Install required packages using pip:
``` bash
   pip install pandas openpyxl
```
## Usage
1. **Prepare the Dataset**:
    - Save traffic data in an Excel file named `traffic_data.xlsx`. The file should consist of columns like:
        - `Time Interval`: Indicates time segments (e.g., "08:00-08:15").
        - `Count`: Number of cars arriving within the time segment.

2. **Run the Simulation**:
    - Execute the script:
``` bash
     python simulator.py
```
- The program will:
    - Extract unique time intervals from your dataset.
    - Simulate traffic flow for each interval.
    - Print results for each interval, including key traffic flow metrics.

1. **Example Output**: Example printed result for one time interval:
``` 
   Simulation for Time Interval: 08:00-08:15
   Cars stopping at red: 15.0
   Cars passing through: 10
   Cars arriving: 10.0
   Cars remaining after cycle: 5.0
```
## Output Details
Each time interval produces the following metrics:
- **Cars stopping at red**: Total cars waiting due to the red light.
- **Cars passing through**: Cars able to pass during the green light.
- **Cars arriving**: Cars that arrived during the red light.
- **Cars remaining after cycle**: Cars left waiting when the signal cycle ends.

## Future Enhancements
1. **Integration with Real-Time Traffic Data**:
    - The system could be expanded to fetch real-time updates from IoT sensors or traffic APIs for dynamic traffic management.

2. **Visualization**:
    - Add graphical output (e.g., bar charts, plots) to visually represent traffic flow at intersections.

3. **Machine Learning**:
    - Incorporate predictive models to optimize traffic light timings based on historical data.

4. **Multi-Lane Simulations**:
    - Extend the model to handle multi-lane intersections for more complex simulations.

## License
This project is open-source and available under the [[CC0 License](https://github.com/Ronlerner-HGS/Traffic-Simulator/tree/main?tab=CC0-1.0-1-ov-file#CC0-1.0-1-ov-file)]().

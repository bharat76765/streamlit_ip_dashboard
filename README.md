# IPL Analysis Dashboard
## Overview

The IPL Analysis Dashboard is a data analysis and visualization tool built using Python and Streamlit. It allows users to explore and analyze IPL (Indian Premier League) cricket data from matches and deliveries datasets.

## Features

- **Team Analysis:**
  - Individual Team Analysis: Analyze statistics for a specific IPL team including matches played, matches won, win percentage, average runs per match, and highest team total. View detailed match-by-match statistics.
![Screenshot 2024-07-21 092638](https://github.com/user-attachments/assets/2494d0f4-658b-4e5d-888c-8f2d60e44f22)
  - Team vs Team Analysis: Compare two IPL teams based on total matches played, win percentage, and average scores against each other.
![Screenshot 2024-07-21 095518](https://github.com/user-attachments/assets/7fda4266-c0fc-41d0-a8bf-c01413333b81)
- **Player Analysis:**
  - Batting Analysis: Analyze batting performance for a selected player including total runs scored, average runs per match, strike rate, number of fifties and hundreds scored. View detailed match-wise batting performance.
  - Bowling Analysis: Analyze bowling performance for a selected player including total wickets taken, average runs conceded per wicket, and economy rate. View detailed match-wise bowling statistics.
![Screenshot 2024-07-21 094706](https://github.com/user-attachments/assets/c5c1ed72-10bd-4a8a-9bc4-00abf79bcade)


## Installation

1. Clone the repository:
   ```
   git clone <repository-url>
   cd IPL-Analysis-Dashboard
   ```

2. Install dependencies:
   ```
   pip install -r requirements.txt
   ```

3. Run the application:
   ```
   streamlit run app.py
   ```

## Data Sources

- **Matches Dataset:** Contains information about IPL matches including teams, venues, dates, and match results.
- **Deliveries Dataset:** Contains ball-by-ball data for each match including runs scored, wickets taken, extras conceded, and more.

## Technologies Used

- Python
- Pandas
- NumPy
- Streamlit

## Usage

1. Launch the application using Streamlit.
2. Use the sidebar to navigate between Team Analysis and Player Analysis sections.
3. Select options and filters to view specific team or player statistics.
4. Interactive visualizations and metrics are displayed for deeper analysis.

## Contributing

Contributions are welcome! If you find any issues or have suggestions for improvements, please open an issue or submit a pull request.

## License

This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments

- Data sourced from [IPL](https://www.iplt20.com/)
- Built as part of learning and exploration in data analysis and visualization.

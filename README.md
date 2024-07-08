# IPL Analysis Dashboard
## Overview

The IPL Analysis Dashboard is a data analysis and visualization tool built using Python and Streamlit. It allows users to explore and analyze IPL (Indian Premier League) cricket data from matches and deliveries datasets.

## Features

- **Team Analysis:**
  - Individual Team Analysis: Analyze statistics for a specific IPL team including matches played, matches won, win percentage, average runs per match, and highest team total. View detailed match-by-match statistics.
  - Team vs Team Analysis: Compare two IPL teams based on total matches played, win percentage, and average scores against each other.

- **Player Analysis:**
  - Batting Analysis: Analyze batting performance for a selected player including total runs scored, average runs per match, strike rate, number of fifties and hundreds scored. View detailed match-wise batting performance.
  - Bowling Analysis: Analyze bowling performance for a selected player including total wickets taken, average runs conceded per wicket, and economy rate. View detailed match-wise bowling statistics.

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

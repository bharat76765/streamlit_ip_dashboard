import streamlit as st
import pandas as pd
import numpy as np
import function as f

# Load datasets
matches = pd.read_csv('resources/matches.csv')
delivery = pd.read_csv('resources/deliveries.csv')

# Title of the app
st.title("IPL Analysis Dashboard")

# Sidebar for navigation
st.sidebar.title("Navigation")
options = st.sidebar.selectbox("Select an option:", ["Team Analysis", "Player Analysis"])

if options == "Team Analysis":
    st.sidebar.subheader("Team Analysis Options")
    team_analysis_option = st.sidebar.selectbox("Choose Analysis Type:",
                                                ["Individual Team Analysis", "Team vs Team Analysis"])

    if team_analysis_option == "Individual Team Analysis":
        st.header("Individual Team Analysis")
        selected_team = st.sidebar.selectbox("Select Team", f.teamlist())

        # Display team analysis results
        matches_played, matches_won, win_percentage, average_runs_per_match, highest_team_total = f.team_analysis(
            selected_team)
        col1,col2,col3=st.columns(3)
        col4,col5=st.columns(2)
        team_stats = f.get_team_statistics(selected_team)
        st.dataframe(team_stats)

        col1.metric("Matches Played",matches_played)
        col2.metric("Matches Won",matches_won)
        col3.metric("Win Percentage%",win_percentage)
        col4.metric("Average Runs per Match",average_runs_per_match)
        col5.metric("Highest Team Total",highest_team_total)

        team_match_details = f.get_team_match_details(selected_team)
        st.dataframe(team_match_details)

    elif team_analysis_option == "Team vs Team Analysis":
        st.header("Team vs Team Analysis")
        team1 = st.sidebar.selectbox("Select Team 1", f.teamlist())
        team2 = st.sidebar.selectbox("Select Team 2", f.teamlist())
        comp=f.compare_teams(team1, team2)

        if team1 != team2:
            total_h2h_matches, team1_win_percentage, team2_win_percentage, team1_average_score, team2_average_score = f.t2t(
                team1, team2)
            col11,col22,col33=st.columns(3)
            col44,col55=st.columns(2)

            col11.metric("Total Matches Played",total_h2h_matches)
            col22.metric(f"{team1} Win Percentage",team1_win_percentage)
            col33.metric(f"{team2} Win Percentage",team2_win_percentage)
            col44.metric(f"{team1} Average Score against {team2}", team1_average_score)
            col55.metric(f"{team2} Average Score against {team1}",team2_average_score)
            st.dataframe(comp)
        else:
            st.write("Please select two different teams for comparison.")

elif options == "Player Analysis":
    st.sidebar.subheader("Player Analysis")
    player_list = f.playerlist()  # Replace with your actual player list function
    selected_player = st.sidebar.selectbox("Choose a player:", player_list)

    # Display player analysis results
    total_runs, average_runs, strike_rate, fifties, hundreds , data ,bowlerdata= f.individual_player_batting(selected_player)

    cola1,colb1,colc1=st.columns(3)
    cold1,cole1=st.columns(2)

    st.header(f"Analysis for {selected_player}")
    st.subheader(f"batting Analysis for {selected_player}")
    cola1.metric(f"Total Runs",total_runs)
    colb1.metric(f"Average Runs",average_runs)
    colc1.metric(f"Strike Rate",strike_rate)
    cold1.metric(f"Fifties",fifties)
    cole1.metric(f"Hundreds",hundreds)
    st.dataframe(data)
    total_wickets, average_runs_per_wicket, economy_rate=f.individual_bowler(selected_player)
    st.subheader(f"bowling Analysis for {selected_player}")
    cola11,colb11,colc11=st.columns(3)
    cola11.metric("total_wickets",total_wickets)
    colb11.metric(f"Average Runs per wicket",average_runs_per_wicket)
    colc11.metric(f"economy Rate",economy_rate)
    st.dataframe(bowlerdata)



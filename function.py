import pandas as pd
import numpy as np

matches=pd.read_csv('resources/matches.csv')
delivery=pd.read_csv("resources/deliveries.csv")
def playerlist():
    players = pd.DataFrame(delivery["batter"].value_counts() + delivery["bowler"].value_counts())
    return players.index.tolist()
def teamlist():
    df = pd.DataFrame(matches['team1'].value_counts() + matches['team2'].value_counts())
    listofteams = df.index.tolist()
    return listofteams
def individual_player_batting(player_name):
    # Total runs scored by the player
    total_runs = delivery[delivery['batter'] == player_name]['total_runs'].sum() - delivery[delivery['batter'] == player_name]['extra_runs'].sum()

    # Average runs per match
    matches_played = delivery[delivery['batter'] == player_name]['match_id'].nunique()
    average_runs = total_runs // matches_played

    # Strike rate (runs per 100 balls)
    balls_faced = delivery[delivery['batter'] == player_name].shape[0]
    strike_rate = (total_runs // balls_faced) * 100

    # Number of 50s and 100s
    player_scores = delivery[delivery['batter'] == player_name].groupby('match_id')['batsman_runs'].sum()
    fifties = (player_scores >= 50).sum()
    hundreds = (player_scores >= 100).sum()

    rec = delivery[(delivery['batter'] == player_name)].groupby('match_id')[['total_runs']].sum()
    rec2 = pd.DataFrame(delivery[(delivery['batter'] == player_name)].groupby('match_id')[['total_runs']].size())
    rec2.columns = ['balls']
    rec1 = pd.DataFrame(delivery[(delivery['batter'] == player_name)].groupby('match_id')[['extra_runs']].sum())
    rec2["balls"] = rec2["balls"] - rec1["extra_runs"]
    rec = pd.merge(rec, rec2, on='match_id')
    rec['strike_rate'] = (rec['total_runs'] // rec['balls']) * 100
    rec["team"] = delivery[(delivery['batter'] == player_name)].groupby('match_id')[['batting_team']].first()
    rec["against"] = delivery[(delivery['batter'] == player_name)].groupby('match_id')[['bowling_team']].first()
    rec["innings"] = delivery[(delivery['batter'] == player_name)].groupby('match_id')[['inning']].first()
    data=rec

    bowler_name = player_name
    rec0 = delivery[(delivery['bowler'] == bowler_name)].groupby('match_id')[['total_runs']].sum()
    rec0.columns = ['runs_conceded']
    rec22 = pd.DataFrame(delivery[(delivery['bowler'] == bowler_name)].groupby('match_id').size())
    rec22.columns = ['balls']
    rec33 = pd.DataFrame(
        delivery[(delivery['bowler'] == bowler_name) & (delivery['is_wicket'] == 1)].groupby('match_id').size())
    rec33.columns = ['wickets']

    # Merge the dataframes
    rec0 = pd.merge(rec0, rec22, on='match_id')
    rec0 = pd.merge(rec0, rec33, on='match_id', how='left').fillna(0)

    # Calculate economy rate and average
    rec0['economy_rate'] = rec0['runs_conceded'] // (rec0['balls'] / 6)
    rec0['average'] = rec0['runs_conceded'] // rec0['wickets'].replace(0, np.nan)  # Avoid division by zero

    # Add team and opposition information
    rec0["team"] = delivery[(delivery['bowler'] == bowler_name)].groupby('match_id')[['bowling_team']].first()
    rec0["against"] = delivery[(delivery['bowler'] == bowler_name)].groupby('match_id')[['batting_team']].first()
    rec0["innings"] = delivery[(delivery['bowler'] == bowler_name)].groupby('match_id')[['inning']].first()
    bowlerdata=rec0

    return total_runs,average_runs,strike_rate,fifties,hundreds,data,bowlerdata
def individual_bowler(bowler_name):
    # Total wickets taken by the bowler
    total_wickets = delivery[(delivery['bowler'] == bowler_name) & (delivery['is_wicket'] == 1)].shape[0]

    # Average runs per wicket
    total_runs_conceded = delivery[delivery['bowler'] == bowler_name]['total_runs'].sum()
    average_runs_per_wicket = total_runs_conceded // total_wickets

    # Economy rate (runs given per over)
    overs_bowled = delivery[delivery['bowler'] == bowler_name].groupby('match_id')['over'].nunique().sum()
    economy_rate = total_runs_conceded // overs_bowled

    return total_wickets, average_runs_per_wicket, economy_rate

def team_analysis(team_name):
    # Total matches played by the team
    matches_played = matches[(matches['team1'] == team_name) | (matches['team2'] == team_name)].shape[0]

    # Total matches won by the team
    matches_won = matches[matches['winner'] == team_name].shape[0]

    # Win percentage
    if matches_played > 0:
        win_percentage = round((matches_won / matches_played) * 100)
    else:
        win_percentage = 0

    # Average runs scored per match
    total_runs_scored = delivery[delivery['batting_team'] == team_name]['total_runs'].sum()
    average_runs_per_match = total_runs_scored // matches_played

    # Highest team total
    highest_team_total = delivery[delivery['batting_team'] == team_name].groupby('match_id')['total_runs'].sum().max()

    return matches_played, matches_won, win_percentage, average_runs_per_match,highest_team_total

def t2t(team1,team2):
    # Head-to-head matches
    head_to_head_matches = matches[((matches['team1'] == team1) & (matches['team2'] == team2)) |
                                   ((matches['team1'] == team2) & (matches['team2'] == team1))]

    # Total matches played between the teams
    total_h2h_matches = head_to_head_matches.shape[0]

    # Matches won by each team
    team1_wins = head_to_head_matches[head_to_head_matches['winner'] == team1].shape[0]
    team2_wins = head_to_head_matches[head_to_head_matches['winner'] == team2].shape[0]

    # Win percentage for each team
    team1_win_percentage = round((team1_wins / total_h2h_matches) * 100)
    team2_win_percentage = round((team2_wins / total_h2h_matches) * 100)

    # Average scores of each team
    team1_average_score = delivery[(delivery['batting_team'] == team1) & (delivery['bowling_team'] == team2)].groupby('match_id')[
        'total_runs'].sum().mean()
    team2_average_score = delivery[(delivery['batting_team'] == team2) & (delivery['bowling_team'] == team1)].groupby('match_id')[
        'total_runs'].sum().mean()

    return total_h2h_matches, team1_win_percentage, team2_win_percentage , round(team1_average_score), round(team2_average_score)

# Function to get team statistics
def get_team_statistics(team_name):
    # Filtering matches involving the team
    team_matches = matches[(matches['team1'] == team_name) | (matches['team2'] == team_name)]

    # Total matches played by the team
    matches_played = team_matches.shape[0]

    # Total matches won by the team
    matches_won = team_matches[team_matches['winner'] == team_name].shape[0]

    # Win percentage
    win_percentage = (matches_won / matches_played) * 100 if matches_played > 0 else 0

    # Total runs scored by the team
    total_runs_scored = delivery[delivery['batting_team'] == team_name]['total_runs'].sum()

    # Average runs per match
    average_runs_per_match = total_runs_scored // matches_played if matches_played > 0 else 0

    # Highest team total
    highest_team_total = delivery[delivery['batting_team'] == team_name].groupby('match_id')['total_runs'].sum().max()

    # Summary DataFrame
    summary_df = pd.DataFrame({
        'matches_played': [matches_played],
        'matches_won': [matches_won],
        'win_percentage': [win_percentage],
        'total_runs_scored': [total_runs_scored],
        'average_runs_per_match': [average_runs_per_match],
        'highest_team_total': [highest_team_total]
    })

    return summary_df


# Function to get individual team match details
def get_team_match_details(team_name):
    # Filtering matches involving the team
    team_matches = matches[(matches['team1'] == team_name) | (matches['team2'] == team_name)]

    # Adding match details
    team_matches['team1_runs'] = team_matches.apply(
        lambda x: delivery[(delivery['match_id'] == x['id']) & (delivery['batting_team'] == x['team1'])][
            'total_runs'].sum(), axis=1)
    team_matches['team2_runs'] = team_matches.apply(
        lambda x: delivery[(delivery['match_id'] == x['id']) & (delivery['batting_team'] == x['team2'])][
            'total_runs'].sum(), axis=1)
    team_matches['winner_runs'] = team_matches.apply(
        lambda x: x['team1_runs'] if x['winner'] == x['team1'] else x['team2_runs'], axis=1)

    # Relevant columns
    match_details = team_matches[
        ['season', 'date', 'city', 'venue', 'team1', 'team2', 'team1_runs', 'team2_runs', 'winner', 'winner_runs',
         'result', 'result_margin']]

    return match_details


def compare_teams(team1_name, team2_name):
    # Filter matches involving both teams
    team1_matches = matches[(matches['team1'] == team1_name) & (matches['team2'] == team2_name)]
    team2_matches = matches[(matches['team1'] == team2_name) & (matches['team2'] == team1_name)]

    # Total matches played between the teams
    total_matches = team1_matches.shape[0] + team2_matches.shape[0]

    # Matches won by each team
    team1_wins = team1_matches[team1_matches['winner'] == team1_name].shape[0]
    team2_wins = team2_matches[team2_matches['winner'] == team2_name].shape[0]

    # Win percentage for each team
    team1_win_percentage = round((team1_wins / total_matches) * 100) if total_matches > 0 else 0
    team2_win_percentage = round((team2_wins / total_matches) * 100) if total_matches > 0 else 0

    # Average scores of each team against the other
    team1_average_score = round(delivery[(delivery['batting_team'] == team1_name) & (delivery['bowling_team'] == team2_name)].groupby('match_id')[
        'total_runs'].sum().mean())
    team2_average_score = round(delivery[(delivery['batting_team'] == team2_name) & (delivery['bowling_team'] == team1_name)].groupby('match_id')[
        'total_runs'].sum().mean())

    # Summary DataFrame
    summary_df = pd.DataFrame({
        'total_matches': [total_matches],
        f'{team1_name} wins': [team1_wins],
        f'{team2_name} wins': [team2_wins],
        f'{team1_name} win percentage': [team1_win_percentage],
        f'{team2_name} win percentage': [team2_win_percentage],
        f'{team1_name} average score against {team2_name}': [team1_average_score],
        f'{team2_name} average score against {team1_name}': [team2_average_score]
    })

    return summary_df


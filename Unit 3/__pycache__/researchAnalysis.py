from helperLogic import get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, get_player_stats_by_name
import matplotlib.pyplot as plt

'1. Which divisin had the strongest defense based on yards allowed per game in 2024'
advanceStates = get_advanced_team_records(2024)
print(advanceStates)

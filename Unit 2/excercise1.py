import pandas as pd
import nfl_data_py as nfl
from helperfunctions import get_team_records

schedules = nfl.import_schedules([2024])
print(schedules.columns.tolist())

    
records = get_team_records(2025)

print(records[['team', 'wins', 'losses', 'points_for', 'points_against']])
print(records[['wins']].mean())

#2022 - 8.4 wins
#2020 - 7.9 wins
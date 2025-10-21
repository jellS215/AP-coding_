import pandas as pd
import nfl_data_py as nfl
from helperfunctions import get_season_Results_By_team, get_team_records

schedules = nfl.import_schedules([2025])
print(schedules.columns.tolist())

records = get_team_records(2025)

top6Teams = ['TB', 'IND', 'LA', 'BUF', 'SF', 'SEA',]
#which team has the best point differential
team_1 = get_season_Results_By_team(2025, 'TB')
team_2 = get_season_Results_By_team(2025, 'IND')
team_3 = get_season_Results_By_team(2025, 'LA')
team_4 = get_season_Results_By_team(2025, 'BUF')
team_5 = get_season_Results_By_team(2025, 'SF')
team_6 = get_season_Results_By_team(2025, 'SEA')
print(team_1)
print(team_2)
print(team_3)
print(team_4)
print(team_5)
print(team_6)

#the team with the best point differential 
'The best point differential is indianapolis of 78'


#which team has the worst point differential
'the team with the worst point differential is SF of -3'

# which theam has the best home point differential
'The best point differential is indianapolis of 36 points'

# which team has the best away point differential
'is Los angeles by -58 points'

# def pdCheck():
#     print("Here is your sum and count of numbers you entered")
    
# number = input("please enter a number another number or type 'stop' to finish:")
# values = []

# while number != 'stop':
#     values.append(int(number))
#     print(values)
#     print(number + "Enter another number or type 'stop' to finish:")
#     number = input()
#     series = pd.Series(values)
# else:
#     print('doing calculation')
#     total=series.sum()
#     count=series.count()
#     print(f'The total is {total}')
#     print(f'The count is {count}')
    

# pdCheck()


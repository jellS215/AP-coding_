import pandas as pd
import nfl_data_py as nfl
from helperfunctions import get_season_Results_By_team, get_team_records

# schedules = nfl.import_schedules([2025])
# print(schedules.columns.tolist())

# records = get_team_records(2025)

# top6Teams = ['TB', 'IND', 'LA', 'BUF', 'SF', 'SEA',]
# #which team has the best point differential
# team_1 = get_season_Results_By_team(2025, 'TB')
# team_2 = get_season_Results_By_team(2025, 'IND')
# team_3 = get_season_Results_By_team(2025, 'LA')
# team_4 = get_season_Results_By_team(2025, 'BUF')
# team_5 = get_season_Results_By_team(2025, 'SF')
# team_6 = get_season_Results_By_team(2025, 'SEA')
# print(team_1)
# print(team_2)
# print(team_3)
# print(team_4)
# print(team_5)
# print(team_6)

def weeklyPlayerStats(year, position, week=None):
    """
    Get season or single-week stats by player for a position.

    Args:
        year (int): NFL season (e.g., 2024)
        position (str): 'QB', 'RB', 'FB', 'WR', 'TE', etc.
        week (int|list[int]|None): specific week or list of weeks; None = all weeks

    Returns:
        pandas.DataFrame: aggregated stats sorted by the primary yardage stat for that position
    """
    weekly = nfl.import_weekly_data([year])
    
    pos = str(position).upper()

    # --- optional week filter ---
    if week is not None:
        if isinstance(week, (list, tuple, set)):
            weekly = weekly[weekly["week"].isin(list(week))]
        else:
            weekly = weekly[weekly["week"] == int(week)]

    # --- filter by position (handle NaN) ---
    filtered = weekly[weekly["position"].fillna("").str.upper() == pos].copy()

    # --- choose team column (keep your output as 'recent_team') ---
    team_col = "recent_team" if "recent_team" in filtered.columns else ("team" if "team" in filtered.columns else None)
    if team_col is None:
        team_col = "recent_team"
        filtered[team_col] = pd.NA

    # --- alias map: pick whatever exists in the data safely ---
aliases = {
        "pass_yards":      ["passing_yards", "pass_yards"],
        "pass_tds":        ["passing_tds", "pass_tds", "pass_td"],
        "pass_att":        ["pass_attempts", "passing_attempts", "attempts"],
        "pass_cmp":        ["completions", "pass_completions", "passing_completions"],
        "interceptions":   ["interceptions", "pass_interceptions", "int"],
        "rush_yards":      ["rushing_yards", "rush_yards"],
        "rush_tds":        ["rushing_tds", "rush_tds"],
        "rush_att":        ["rushing_attempts", "rush_att", "carries"],
        "rec_yards":       ["receiving_yards", "rec_yards"],
        "rec_tds":         ["receiving_tds", "rec_tds"],
        "receptions":      ["receptions", "rec"],
        "targets":         ["targets", "tar"],
        "fantasy_points":  ["fantasy_points", "fantasy_points_ppr", "fantasy_points_half_ppr"],
}

# Who are the top 5 qbs by passng yards in 2024
exampleData = weeklyPlayerStats(2024, 'QB')
print(exampleData)

'Joe burrow, Jared Goff, Baker Mayfield, Geno Smith, Sam darnold are the top 5 qbs by passing yards in 2024'

#what does a high completion percentage mean about a qb
"A high completion percentage indicates that a quarterback is accurate and efficient in completing passes to receivers."

# Which RB had the highest rushing yards in 2024
exampleData = weeklyPlayerStats(2024, 'RB')

'The RB with the highest rushing yards in 2024 is Saquon barkley.'
'The RB with the best yards per carry in 2024 is derrick henry'

#If a RB has a low yards per carry average but high yards what does that indicate about the player
"A low yards per carry average but high total yards indicates that the running back is getting a lot of carries, suggesting they are heavily relied upon in the offense."

# Which WR had the highest receiving yards in 2024 on the fewest pass attempts
exampleData = weeklyPlayerStats(2024, 'WR')

'Justin Jefferson, AJ Brown, Drake London, Trey Mcbride, George Kittle are the top 5 wr by receiving yards but lowest passing attempts in 2024'








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


from helperLogic import get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, get_player_stats_by_name
import matplotlib.pyplot as plt

'1. Which divisin had the strongest defense based on yards allowed per game in 2024'
advanceStates = get_advanced_team_records(2024)
#print(advanceStates)

'Answer: the NFC east had the strongest defense based on yards allowed per game in 2024, allowing 326.6 yards per game on average.'

'2. Which wr had the most targets vs receptions in 2024?'

wr_stats = weeklyPlayerStats(2024, 'WR')
#print(wr_stats)
playerStat= get_player_stats_by_name(2024,'J.Chase','WR')
#print(playerStat)

'Answer: This is a descriptive and clear question, it tells what specific year and position to look for. The wide reciever with the most targets vs receptions in 2024 was JaMarr chase, with 175 targets and 127 receptions.'

'3. Does time of possession correlate with winning games in 2024?'

advanceStates = get_advanced_team_records(2024)
#print(advanceStates)

'Answer: This is a relational and a researchable question. No, time of possession does not correlate with winning games in 2024. The team with the highest time of possession, the Cleveland browns had a record of 3-14 in 2024.'

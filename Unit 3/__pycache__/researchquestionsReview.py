from helperLogic import get_team_records, get_advanced_team_records, get_position_columns, get_season_Results_By_team , weeklyPlayerStats, get_player_stats_by_name
import matplotlib.pyplot as plt

# Columns available to research based on year and position
# columnData = get_position_columns(2024, "QB")

'1. How much does QB pass accuracy influence team wins ? '
teamRecord = get_team_records(2024)
#print(teamRecord)

dbData = weeklyPlayerStats(2024, 'DB')
#print(dbData)

# 'J.Allen'
# 'J.Hurts'

# playerStat= get_player_stats_by_name(2024,'J.Hurts','QB')
# print(playerStat)

'Answer: Yes, there is a relationship. based on the average qb completion %, anything above 60 % is considered a good completion number'
"also based on team records, the top 10- top teams all have had qbs that have over 65% completion percentages."

'2. Does defensive turnovers contribute to a teams win percentage ? '

# advanceStates = get_advanced_team_records(2024)
# # print(advanceStates)

'Answer: Yes, this is a relationship question, the question is also clear. No, based on the data collected, there is no correlation between defensive turnovers and team win percentage. Teams with high turnovers do not necessarily have higher win percentages, and the higher win percentage teams do not necessarily have lower turnovers.'


'3. Who has the most passing yards of all time ? '
# allTimePassingYards = get_season_Results_By_team(2024, 'passingYards')
# # print(allTimePassingYards)

stats = weeklyPlayerStats(2024, "QB")  
print(stats)
passingYards = {}

"This question is descriptive, but is pretty vague. The due to the limitations of the data set, we can only look at a single season, not all time. The player with the highest all time passing yards is tom brady, with 89,214 yards. However, based on the data set for 2024, the player with the most passing yards is Jared Goff with 4,891 yards."
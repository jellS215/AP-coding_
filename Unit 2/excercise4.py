from helperfunctions import weeklyPlayerStats, plot_weekly_player_stats, plot_player_stat
import matplotlib.pyplot as plt

# 1) Using an existing stats dataframe:
stats = weeklyPlayerStats(2024, "RB")  
print(stats)
plot_player_stat(stats, stat="rushing_tds", top_n=15, title="WR rushing TDs (2024)", save_path="rb_rushing_tds_2024.png"  )
#plot_player_stat(stats, stat="passing_yards", top_n=20, title="QB Passing Yards (2024)", save_path="qb_passing_yards_2024.png"  )

# 2) One-liner wrapper:




plot_weekly_player_stats(2024, "RB", stat="rushing_tds", top_n=15, week=[1,2,3], save_path="rb_rush_tds_2024.png")

# Use the new plot_player_stat() and plot_weekly_player_stats() to visualize the data into bar graphs and answer the following questions.

# 1. Use each helper function to find your own metric to visualize. use the weeklyPlayerStats function to find positions and stat columns by name
 
# 2. Find the player with the most touchdowns in 2024?
"the player with the most tds in 2024 is Derrick Henry with 21 tds."
# 3. find the player with the highest total passing yards in 2024.
"the player with the highest total passing yards in 2024 is Jared Goff with 4942 yards."
# 4. which player had the highest rushing yards in week 1 and in week 17?
"the player with the highest rushing yards in week 1 is Joe Mixon with 159 yards. the player with the highest rushing yards in week 17 is Saquon Barkley with 167 yards."
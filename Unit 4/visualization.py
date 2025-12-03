import nfl_data_py as nfl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from helperfunctions import get_season_totals_by_position, get_player_stats, dataframe_to_png, plot_player_stat_by_week, plot_position_stat_bar, get_team_season_data, get_team_game_stats

positonStats = plot_position_stat_bar(2024, "QB", "passing_yards", save_path="qb_passing_2024.png", top_n=20)
print(positonStats)
 
qb_2024_totals_top5 = get_season_totals_by_position(2024, "QB")
print(qb_2024_totals_top5.head())

The getPlayerData_png code was messing up my entire code without me knowing and i just figured it out can i get more
time to answer
import nfl_data_py as nfl
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np
from helperfunctions import get_season_totals_by_position, get_player_stats, dataframe_to_png, plot_player_stat_by_week, plot_position_stat_bar, get_team_season_data, get_team_game_stats

# rbpositionStats = plot_position_stat_bar(2024, "RB", "rushing_yards", save_path="rb_rushing_2024.png", top_n=20)
# print(rbpositionStats)
# rb_2024 = get_season_totals_by_position(2024, "RB")
# print(rb_2024.head())

# rbpositionStats = plot_position_stat_bar(2023, "RB", "rushing_yards", save_path="rb_rushing_2023.png", top_n=20)
# print(rbpositionStats)

# rbpositionStats = plot_position_stat_bar(2022, "RB", "rushing_yards", save_path="rb_rushing_2022.png", top_n=20)
# print(rbpositionStats)

'1. derrick henry had the most rushing yards overall throughout 2022-2024 out of all running backs.'

jalenStats1 = plot_player_stat_by_week(2024, "Jalen", "Hurts", "passing_yards", save_path="Jalen_Hurts_2024_passing_yards.png")

jalenStats2 = plot_player_stat_by_week(2023, "Jalen", "Hurts", "passing_yards", save_path="Jalen_Hurts_2023_passing_yards.png")

jalenStats3 = plot_player_stat_by_week(2022, "Jalen", "Hurts", "passing_yards", save_path="Jalen_Hurts_2022_passing_yards.png")

print(jalenStats1)
print(jalenStats2)
print(jalenStats3)

# qbpositonStats = plot_position_stat_bar(2024, "QB", "passing_yards", save_path="qb_passing_2024.png", top_n=20)
# print(positonStats)
 
# qb_2024_totals_top5 = get_season_totals_by_position(2024, "QB")
# print(qb_2024_totals_top5.head())


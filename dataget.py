import soccerdata as sd 
import pandas as pd

#create scraper class instance 
fbref = sd.FBref( leagues=['Big 5 European Leagues Combined','ENG-Premier League','ESP-La Liga',
 'FRA-Ligue 1',
 'GER-Bundesliga',
 'ITA-Serie A'])

season_stats = fbref.read_team_season_stats(stat_type='shooting')


#do the same for player stats
player_stats = fbref.read_player_season_stats(stat_type='shooting')
player_stats = fbref.read_player_season_stats(stat_type='passing')
player_stats = fbref.read_player_season_stats(stat_type='passing_types')
player_stats = fbref.read_player_season_stats(stat_type='goal_shot_creation')
player_stats = fbref.read_player_season_stats(stat_type='defense')
player_stats = fbref.read_player_season_stats(stat_type='possession')
player_stats = fbref.read_player_season_stats(stat_type='playing_time')
player_stats = fbref.read_player_season_stats(stat_type='misc')
player_stats = fbref.read_player_season_stats(stat_type='possession')
player_stats = fbref.read_player_season_stats(stat_type='keeper')
player_stats = fbref.read_player_season_stats(stat_type='keeper_adv')






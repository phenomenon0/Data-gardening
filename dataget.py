import soccerdata as sd 
import pandas as pd

#create scraper class instance 
fbref = sd.FBref( leagues='Big 5 European Leagues Combined')

season_stats = fbref.read_team_season_stats(stat_type='shooting')


#do the same for player stats
player_stats = fbref.read_player_season_stats()





from lodes_star.fetch import fetch_geo
from lodes_star.state_codes import Geographies


Geographies.list()
block_df = fetch_geo(state='ma', geography='TABBLOCK', year='2019')
bg_df = fetch_geo(state='ma', geography='BG', year='2019')
tract_df = fetch_geo(state='ma', geography='TRACT', year='2019')



tract_df[['INTPTLAT', 'INTPTLON']] = tract_df[['INTPTLAT', 'INTPTLON']].astype(float)

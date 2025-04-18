import pandas as pd

air = pd.read_csv('air.csv')
air.head()

air['london_mg_per_cubic'] = air['station_london'] * 1.882
air.head()

air['ratio_paris_antwerp'] = (
    air['station_paris'] / air['station_antwerp']
)
air.head()

air_quality_renamed = air.rename(
    columns= {
        "station_antwerp": "BETR801",
        "station_paris": "FR04014",
        "station_london": "London Westminster",
    }
)
air.head()

air_quality_renamed.head()
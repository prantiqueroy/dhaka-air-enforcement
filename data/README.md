# Data

## dhaka_pm25_2016_2025.csv
Hourly PM2.5 (µg/m³) from the US consulate monitor, Baridhara, Dhaka.
- Source: OpenAQ API v3, downloaded 13 Oct 2026
- Combines two OpenAQ records of the same monitor:
  sensor 4680 (StateAir, 11 Mar 2016 – 9 Nov 2016) and
  sensor 24434 (AirNow, 10 Nov 2016 – 24 Mar 2025)
- 72,035 hourly readings, about 91% of all hours in the period
- Times are Dhaka local time (UTC+6), start of each hour
- Columns: time, pm25, sensor
- Not yet cleaned (negative or stuck values not removed)

## dhaka_weather_2016_2025.csv
Hourly weather at 23.80°N, 90.42°E (Baridhara, Dhaka).
- Source: Open-Meteo historical weather API (ERA5 reanalysis), downloaded 13 Oct 2026
- 87,672 hours, 1 Jan 2016 – 31 Dec 2025
- Times are Dhaka local time (UTC+6)
- Columns: time, temperature_2m (°C), relative_humidity_2m (%),
  precipitation (mm), wind_speed_10m (km/h), wind_direction_10m (degrees)

## Code
Download code is in notebooks/01_weather_download.ipynb and notebooks/02_pm25_download.ipynb

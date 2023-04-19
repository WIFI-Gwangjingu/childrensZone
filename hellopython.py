import csv
import geopy

geo = geopy.Nominatim(user_agent="South Korea")

with open("서울시광진구학교기본정보.csv") as file:
    reader = csv.DictReader(file)
    i = 1
    for row in reader:
        tmp = geo.geocode(row["도로명주소"])
        print(i, row["학교명"], row["도로명주소"], tmp.latitude, tmp.longitude)
        i += 1
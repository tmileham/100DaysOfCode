# capitals = {
#     "european": ["London","Paris","Warsaw"],
#     "asian": ["Tokyo","Bangkok"]

# }


# travel_log = {
#     "France": {
#         "cities_visited":["Paris","Lille","Dijon"], "total_visits":12
#     },

#     "UK": {
#         "cities_visted": ["London","Cornwall","Manchester","Liverpool"], "total_visits":23
#     }
# }

# print(travel_log["France"]["total_visits"])

#Nesting Dictionary in a List

# travel_log2 = [
#     {"country": "France", "cities_visited":["Paris","Normandy","Lille","Dijon"],"total_visits":12,},
#     {"country": "UK", "cities_visited": ["London","Cornwall","Manchester","Liverpool"], "total_visits":23},
# ]

# print(travel_log2[1]["cities_visited"])

travel_log = [
    {
        "country": "France",
        "visits": 12,
        "cities": ["Paris", "Lille", "Dijon"],
    },
    {
        "country": "Germany",
        "visits": 5,
        "cities": ["Berlin", "Hamburg", "Stuttgart"],
    }
]



def add_new_country(country,times_visited,list_of_cities):
    tempdict = {
        "country": country,
        "visits" : times_visited,
        "cities" : list_of_cities

    }
    travel_log.append(tempdict)

add_new_country("Russia",2,["Moscow", "Saint Petersberg"])

print(travel_log)


# for city in travel_log2[1]["cities_visited"]:
#     print(city)


# for key, values in travel_log.items():
#     for city in values:
#         if key == "UK":
#             print(city)
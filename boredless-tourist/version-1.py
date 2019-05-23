import json

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]
destinations = []

with open('destinations.json') as file:
    data = json.load(file)
    for d in data['destinations']:
        destinations.append(d)


attractions = []

with open('attractions.json') as file:
    data = json.load(file)
    for d in data['attractions']:
        attractions.append(d)


attractions_with_interest = []


def get_dest_index(destination):
    return destinations.index(destination)


def get_traveler_location(traveler):
    traveler_dest = traveler[1]
    dest_index = get_dest_index(traveler_dest)
    return dest_index


def find_attractions(destination, interests):
    dest_index = get_dest_index(destination)
    attractions_in_city = attractions[dest_index]
    for possible_attraction in attractions_in_city:
        attraction_tags = possible_attraction[1]
        for interest in interests:
            if interest in attraction_tags:
                attractions_with_interest.append(possible_attraction[0])
    return attractions_with_interest


def get_attractions_for_traveler(traveler):
    traveler_destination = traveler[1]
    traveler_interest = traveler[2]
    traveler_attractions = find_attractions(
        traveler_destination, traveler_interest)
    interests_string = f"Hi {traveler[0]}, we think you'll like these places around {traveler_destination}: "
    for attraction in traveler_attractions:
        interests_string += f"{attraction}"
    return interests_string


test = get_attractions_for_traveler(test_traveler)
print(test)

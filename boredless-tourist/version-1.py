destinations = ['Paris, France', 'Shanghai, China',
                'Los Angeles, USA', 'São Paulo, Brazil', 'Cairo, Egypt']

test_traveler = ['Erin Wilkes', 'Shanghai, China', ['historical site', 'art']]

attractions = [[] for i in destinations]


def get_dest_index(destination):
    return destinations.index(destination)


def get_traveler_location(traveler):
    traveler_dest = traveler[1]
    dest_index = get_dest_index(traveler_dest)
    return dest_index


def add_attraction(destination, attraction):
    try:
        dest_index = get_dest_index(destination)
    except SyntaxError:
        print("Error caught!")
    attraction.

test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

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
        attractions_for_destination = attractions[dest_index]
        attractions_for_destination.append(attraction)
    except SyntaxError:
        return


test_destination_index = get_traveler_location(test_traveler)
print(test_destination_index)

add_attraction("Paris, France", ["the Louvre", ["art", "museum"]])
add_attraction("Paris, France", ["Arc de Triomphe", [
               "historical site", "monument"]])
add_attraction("Shanghai, China", ["Yu Garden", [
               "garden", "historcical site"]])
add_attraction("Shanghai, China", ["Yuz Museum", ["art", "museum"]])
add_attraction("Shanghai, China", ["Oriental Pearl Tower", [
               "skyscraper", "viewing deck"]])
add_attraction("Los Angeles, USA", ["LACMA", ["art", "museum"]])
add_attraction("São Paulo, Brazil", ["São Paulo Zoo", ["zoo"]])
add_attraction("São Paulo, Brazil", ["Pátio do Colégio", ["historical site"]])
add_attraction("Cairo, Egypt", ["Pyramids of Giza", [
               "monument", "historical site"]])
add_attraction("Cairo, Egypt", ["Egyptian Museum", ["museum"]])
print(attractions)

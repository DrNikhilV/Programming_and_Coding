Hotel = {
    'Hotel_1': {'cuisine': 'Italian', 'location': 'Downtown', 'rating': 4.7},
    'Hotel_2': {'cuisine': 'Mexican', 'location': 'Suburb', 'rating': 4.2},
    'Hotel_3': {'cuisine': 'Italian', 'location': 'Downtown', 'rating': 4.8},
    'Hotel_4': {'cuisine': 'Indian', 'location': 'Suburb', 'rating': 4.1},
    'Hotel_5': {'cuisine': 'French', 'location': 'Downtown', 'rating': 4.6},
    'Hotel_6': {'cuisine': 'Italian', 'location': 'Suburb', 'rating': 4.4},
}

user = {'cuisine': 'Italian', 'location': 'Downtown'}

fav_hotel = [
    (Hotel, attributes['rating'])
    for Hotel, attributes in Hotel.items()
    if attributes['cuisine'] == user['cuisine']
    and attributes['location'] == user['location']
]

if fav_hotel:
    recommended_Hotel, highest_rating = max(fav_hotel, key=lambda x: x[1])
    print(f"The recommended Hotel is {recommended_Hotel} with a rating of {highest_rating}.")
else:
    print("No suitable Hotel found based on your preferences.")

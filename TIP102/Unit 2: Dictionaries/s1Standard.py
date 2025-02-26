# Problem 1: Festival Lineup

def lineup(artists, set_times):
    # zipped = zip(artists,set_times)
    # return {key: value for key,value in zipped}
    dict = {}
    for i in range(len(artists)):
        dict[artists[i]] = set_times[i]
    return dict

# artists1 = ["Kendrick Lamar", "Chappell Roan", "Mitski", "Rosalia"]
# set_times1 = ["9:30 PM", "5:00 PM", "2:00 PM", "7:30 PM"]

# artists2 = []
# set_times2 = []

# print(lineup(artists1, set_times1))
# print(lineup(artists2, set_times2))

def get_artist_info(artist, festival_schedule):
    for i in range(len(festival_schedule)):
        return festival_schedule.get(artist, {'message': 'Artist not found'})

festival_schedule = {
    "Blood Orange": {"day": "Friday", "time": "9:00 PM", "stage": "Main Stage"},
    "Metallica": {"day": "Saturday", "time": "8:00 PM", "stage": "Main Stage"},
    "Kali Uchis": {"day": "Sunday", "time": "7:00 PM", "stage": "Second Stage"},
    "Lawrence": {"day": "Friday", "time": "6:00 PM", "stage": "Main Stage"}
}

# print(get_artist_info("Blood Orange", festival_schedule)) 
# print(get_artist_info("Taylor Swift", festival_schedule))  

# Problem 3: Ticket Sales

def total_sales(ticket_sales):
    total = 0
    for key in ticket_sales:
        total += ticket_sales[key]
    return total

# ticket_sales = {"Friday": 200, "Saturday": 1000, "Sunday": 800, "3-Day Pass": 2500}
# print(total_sales(ticket_sales))


def identify_conflicts(venue1_schedule, venue2_schedule):
    result = {}
    for key, value in venue1_schedule.items():
        if key is None and value is None or key == "" or value == "":
            continue
        if key in venue2_schedule and value == venue2_schedule[key]:
                result[key] = value
    return result
            
venue1_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "8:00 PM",
    "HARDY": "7:00 PM",
    "Bruce Springsteen": "6:00 PM"
}

venue2_schedule = {
    "Stromae": "9:00 PM",
    "Janelle Monáe": "10:30 PM",
    "HARDY": "7:00 PM",
    "Wizkid": "6:00 PM"
}

print(identify_conflicts(venue1_schedule, venue2_schedule)) #{"Stromae": "9:00 PM", "HARDY": "7:00 PM"}



def get_event_date(event):  # Because you want to know the date and time of each interaction.
    return event.date  # Gives you back the desired date and time of action.


def current_users(events):
    events.sort(key=get_event_date)
    machines = {}  # Dictionaty where you will store names of users and machines.
    for event in events:  # itirate through the list of events.
        if event.machine not in machines:  # check if machine affected is in the dictionary. e
            machines[event.machine] = set()  # adds the value if it is not affected into an empty set.
        if event.type == "login":
            machines[event.machine].add(event.user)  # records any login attempts and adds
        elif event.type == "logout":
            machines[event.machine].remove(event.user)  # records any logout attempts and removes
    return machines  # returns the value


def generate_report(machines):  # will generate the report of users
    for machine, users in machines.items():  # this ensures that it gives you the iteration of the key and the value
        if len(users) > 0:  # sets it to print only when there is more than zero elements.
            user_list = ", ".join(users)  # machine name joined with the user of that machine separated by commas.
            print("{}: {}".format(machine, user_list))  # This gives you the desired str in a format method.


class Event:
    def _init_(self, event_date, event_type, machine_name, user):
        self.date = event_date
        self.type = event_type
        self.machine = machine_name
        self.user = user


events = [
    Event('2020-01-21 12:45:56', 'login', 'myworkstation.local', 'jordan'),
    Event('2020-01-22 15:53:42', 'logout', 'webserver.local', 'jordan'),
    Event('2020-01-21 18:53:21', 'login', 'webserver.local', 'lane'),
    Event('2020-01-22 10:25:34', 'logout', 'myworkstation.local', 'jordan'),
    Event('2020-01-21 08:20:01', 'login', 'webserver.local', 'jordan'),
    Event('2020-01-23 11:24:35', 'logout', 'mailserver.local', 'chris'),
]

users = current_users(events)
print(users)

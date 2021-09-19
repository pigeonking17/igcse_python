from random import randint

WEEKS = 4

def main():
    # Initialize the empty repository of bus times, then fill it up.

    rand_or_man = input("Use random numbers or manual? (empty for random): ")

    bus_times = []
    for week_num in range(WEEKS):
        for day_num in range(5):
            bus_times.append(list(map(int, get_bus_times(week_num, day_num, rand_or_man))))

    # Print the bus times.
    print_buses(bus_times)

    # Print the statistics of the bus times.
    print_statistics(bus_times)

    # Ask for a day to show the average.
    get_average_for_day_input(bus_times)

def get_bus_times(week_num, day_num, rand_or_man):
    if rand_or_man == "":
        bus_times = [randint(-10, 10) for i in range(6)]
        return bus_times

    # Used to check whether the bus times are valid.
    bus_times_valid = False

    while bus_times_valid != True:
        # Get bus times and split them based on whitespace.
        bus_times = input(f"Enter week {week_num+1} day {day_num+1} of bus times, seperated by spaces: ")
        bus_times = bus_times.split()

        # Assert that the number of times entered is right.
        if len(bus_times) == 6:
            bus_times_valid = True
        else:
            bus_times_valid = False
            print("Enter 6 bus times.")
            continue

        # Assert that all the elements are integers.
        try:
            map(int, bus_times)
            bus_times_valid = True
        except ValueError:
            print("Enter integers only.")
            bus_times_valid = False

    return bus_times

def print_buses(bus_times):
    # Print table header.
    print("Day\tBus A\tBus B\tBus C\tBus D\tBus E\tBus F")

    # Empty list to hold days and list of day names.
    days = []
    day_names = ["Mon", "Tue", "Wed", "Thu", "Fri"]

    # Get day numbers and names and combine them.
    for day_num in range(WEEKS):
        for day_name in day_names:
            days.append(f"{day_name} {day_num+1}")

    # Assign each number a day, in order.
    bus_times = list(zip(bus_times, days))

    # Print each row of the table with day and bus time.
    for (bus_time, day) in bus_times:
        print(f"{day}\t", end="")
        print(*bus_time, sep="\t")

def print_statistics(bus_times):
    # Variables to hold statistics
    bus_times_late = 0
    bus_times_on_time = 0
    bus_times_early = 0

    # Check whether each bus time was what and update the corresponding values.
    for x in bus_times:
        for bus_time in x:
            if bus_time == 0:
                bus_times_on_time += 1
            elif bus_time > 0:
                bus_times_early += 1
            elif bus_time < 0:
                bus_times_late += 1

    # Print the statistics.
    print(f"The bus was late {bus_times_late} time(s).")
    print(f"The bus was early {bus_times_early} time(s).")
    print(f"The bus was on time {bus_times_on_time} time(s).")

def get_average_for_day_input(bus_times):
    # Variable to check the input day.
    input_day = ""

    # While the user doesn't quit, ask for a day to check the average.
    while input_day != "q":
        # Input the day.
        input_day = input("Enter a day code to check times for (q to quit): ")
        # Check the first 3 lowercase letters, which allows for "mon", "Mon", "Monday", "mOnDDAy"
        # And check the number.
        try:
            if input_day.lower().strip()[0:3] == "mon" and int(input_day[3]) in range(1,WEEKS+1):
                # Call the get_average_for_day function with the times and the day number.
                get_average_for_day(bus_times, 0, int(input_day[3]))
            elif input_day.lower().strip()[0:3] == "tue" and int(input_day[3]) in range(1,WEEKS+1):
                get_average_for_day(bus_times, 1, int(input_day[3]))
            elif input_day.lower().strip()[0:3] == "wed" and int(input_day[3]) in range(1,WEEKS+1):
                get_average_for_day(bus_times, 2, int(input_day[3]))
            elif input_day.lower().strip()[0:3] == "thu" and int(input_day[3]) in range(1,WEEKS+1):
                get_average_for_day(bus_times, 3, int(input_day[3]))
            elif input_day.lower().strip()[0:3] == "fri" and int(input_day[3]) in range(1,WEEKS+1):
                get_average_for_day(bus_times, 4, int(input_day[3]))
        except IndexError:
            print("Enter a correct day code.")
        except ValueError:
            print("Enter a correct day code.")

def get_average_for_day(bus_times, day, day_code):
    # Get the bus times for that day.
    bus_times_for_day = bus_times[day::5][day_code-1]

    bus_names = ["Bus A", "Bus B", "Bus C", "Bus D", "Bus E", "Bus F"]

    bus_times_for_day = list(zip(bus_names, bus_times_for_day))

    print("Buses late on that day:")

    for bus_time in bus_times_for_day:
        if bus_time[1] < 0:
            print(f"{bus_time[0]}: {abs(bus_time[1])} minute(s) late")

if __name__ == "__main__":
    # Run the program.
    main()

WEEKS = 4

def main():
    # Initialize the empty repository of bus times, then fill it up.
    bus_times = []
    for i in range(WEEKS):
        for bus_time in get_bus_times(i):
            bus_times.append(int(bus_time))
    
    # Print the bus times.
    print_buses(bus_times)
    
    # Print the statistics of the bus times.
    print_statistics(bus_times)
    
    # Ask for a day to show the average.
    get_average_for_day_input(bus_times)

def get_bus_times(week_num):
    # Used to check whether the bus times are valid.
    bus_times_valid = False
    
    while bus_times_valid != True:
        # Get bus times and split them based on whitespace.
        bus_times = input(f"Enter week {week_num+1} of bus times, seperated by spaces: ")
        bus_times = bus_times.split()
        
        # Assert that the number of times entered is right.
        if len(bus_times) == 5:
            bus_times_valid = True
        else:
            bus_times_valid = False
            print("Enter 5 bus times.")
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
    print("Day\tBus A")
    
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
        print(f"{day}\t{bus_time}")

def print_statistics(bus_times):
    # Variables to hold statistics
    bus_times_late = 0
    bus_times_on_time = 0
    bus_times_early = 0
    
    # Check whether each bus time was what and update the corresponding values.
    for bus_time in bus_times:
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
        input_day = input("Enter a day to check average times for (q to quit): ")
        # Check the first 3 lowercase letters, which allows for "mon", "Mon", "Monday", "mOnDDAy"
        if input_day.lower().strip()[0:3] == "mon":
            # Call the get_average_for_day function with the times and the day number.
            get_average_for_day(bus_times, 0)
        elif input_day.lower().strip()[0:3] == "tue":
            get_average_for_day(bus_times, 1)
        elif input_day.lower().strip()[0:3] == "wed":
            get_average_for_day(bus_times, 2)
        elif input_day.lower().strip()[0:3] == "thu":
            get_average_for_day(bus_times, 3)
        elif input_day.lower().strip()[0:3] == "fri":
            get_average_for_day(bus_times, 4)

def get_average_for_day(bus_times, day):
    # Get the bus times for that day.
    bus_times_for_day = bus_times[day::5]
    
    # Get the average time for that day.
    sum_of_times = sum(bus_times_for_day) / len(bus_times_for_day)
    
    # Check whether it is negative or positive or zero and outputs a suitable message.
    if sum_of_times == 0:
        print("It was on time, on average, for that day.")
    elif sum_of_times > 0:
        print(f"It was {sum_of_times} minute(s) early, on average, for that day.")
    elif sum_of_times < 0:
        print(f"It was {abs(sum_of_times)} minute(s) late, on average, for that day.")
    

if __name__ == "__main__":
    # Run the program.
    main()
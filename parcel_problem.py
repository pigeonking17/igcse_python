def main():
    input = get_input()
    results = check_parcel(input)

    while results[0] == False:
        print(results[1])
        input = get_input()
        results = check_parcel(input)

def get_input():
    """
    Gets and parses input from the user

    :returns: a list of 4 numbers
    """

    dimensions = []
    dimensions_are_checked = False
    weight_is_checked = False

    while dimensions_are_checked == False:
        dimensions = input("Dimensions (cm.cm.cm): ")

        dimensions = "".join(dimensions.split())
        dimensions = dimensions.split('.')

        if len(dimensions) != 3:
            print("Please enter 3 integers.")
            continue

        try:
            dimensions = list(map(int, dimensions))
        except ValueError:
            print("Please enter integers only.")
            continue

        for i in range(0, 3):
            if dimensions[i] > 80:
                print("Each dimension should be less than 80")
                break
            continue

        if sum(dimensions[:]) > 200:
            print("The sum of the dimensions must be less than 200")
            continue

        dimensions_are_checked = True

    while weight_is_checked == False:
        weight = input("Weight (kg): ")

        try:
            weight = int(weight)
        except ValueError:
            print("Please enter integers only.")
            continue

        dimensions = list(map(int, dimensions))

        dimensions.append(weight)

        if dimensions[3] > 10 or dimensions[3] < 1:
            print("Weight must be between 1 and 10.")
            continue

        weight_is_checked = True


    return dimensions

def check_input(list):
    """
    Checks whether the input is correct.

    :list: TODO
    :returns: bool

    """
    for element in list:
        if isinstance(element, int) == False:
            return False

    return True

def check_parcel(parcel_specs):
    """
    Takes a list which contains 3 dimensions and 1 weight

    :parcel_specs: TODO
    :returns: TODO

    """
    for i in range(0, 3):
        if parcel_specs[i] > 80:
            return (False, "Each dimension must be less than 80")

    if sum(parcel_specs[0:3]) > 200:
        return (False, "The sum of the dimensions must be less than 200")

    if parcel_specs[3] > 10 or parcel_specs[3] < 1:
        return (False, "Weight must be between 1 and 10.")

    return (True, "All Good")

if __name__ == "__main__":
    main()

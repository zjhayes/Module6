#asks the user for a name (string), hours worked (int) and an hourly pay rate (float) and prints a string including the information.


def hourly_employee_input():
    try:
        name = input("Enter your name: ")
        hours_worked = int(input("Number of hours worked: "))
        pay_rate = float(input("Enter payrate (hourly): "))
        total_earned = hours_worked * pay_rate
        print("Name: " + name)
        print("Hours worked: " + str(hours_worked))
        print("Hourly pay rate: $%.2f" % pay_rate)
        print("Total earnings: $%.2f" % total_earned)
    except ValueError as err:
        print("Incorrect value entered, try again.")
        hourly_employee_input()

if __name__ == '__main__':
    try:  # check for ValueError
        hourly_employee_input()
    except ValueError as err:
        print("ValueError encountered!")
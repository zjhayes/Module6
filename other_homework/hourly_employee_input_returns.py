#Zachary Hayes


def hourly_employee_input():
    """Takes employee input and prints data to console."""
    try:
        name = input("Enter your name: ")
        total_earned = weeky_pay()
        print("Name: " + name)
        print("Total earnings: " + total_earned)
    except ValueError as err:
        print("Incorrect value entered, try again.")
        hourly_employee_input()


def weeky_pay():
    """Takes employee weekly pay as input and returns weekly pay cal"""
    hours_worked = int(input("Number of hours worked: "))
    pay_rate = float(input("Enter payrate (hourly): "))
    total_earned = hours_worked * pay_rate
    return "$%.2f" % total_earned


if __name__ == '__main__':
    try:  # check for ValueError
        hourly_employee_input()
    except ValueError as err:
        print("ValueError encountered!")

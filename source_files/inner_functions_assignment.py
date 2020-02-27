#Zachary Hayes


def measurements(measurements_list):
    def area(a_list):
        if len(a_list) == 1:
            return a_list[0] * a_list[0]
        elif len(a_list) == 2:
            return a_list[0] * a_list[1]
        else:
            raise ValueError

    def perimeter(a_list):
        if len(a_list) == 1:
            return a_list[0] * 4
        elif len(a_list) == 2:
            return a_list[0] * 2 + a_list[1] * 2
        else:
            raise ValueError
    try:
        perimeter_result = perimeter(measurements_list)
        area_result = area(measurements_list)
        return "Perimeter = %.1f Area = %.2f" % (perimeter_result, area_result)
    except ValueError:
        return "Invalid input."

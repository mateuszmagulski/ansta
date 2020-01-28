# ZADANIE 1

def postcode_generator(start = "79-900", stop = "80-155"):

    start_XX = int(start.split('-')[0])
    stop_XX = int(stop.split('-')[0])

    start_YYY = int(start.split('-')[1])
    stop_YYY = int(stop.split('-')[1])

    postcodes_list = []

    for xx in range(start_XX, stop_XX +1):        
        start_yyy = 0
        stop_yyy = 1000
        if xx == start_XX:
            start_yyy = start_YYY
        if xx == stop_XX:
            stop_yyy = stop_YYY
        if xx < 10:
            xx = "0{}".format(xx)

        for yyy in range(start_yyy+1, stop_yyy):

            if yyy < 10:
                yyy = "00{}".format(yyy)
            elif yyy < 100:
                yyy = "0{}".format(yyy)

            postcodes_list.append("{}-{}".format(xx,yyy))

    return postcodes_list

postcode_generator()

# ZADANIE 2

def n_check(values,n):
    missing_values = []

    for value in range(1,n + 1):
        if not value in values:
            missing_values.append(value)
    return(missing_values)

n_check([2,3,7,4,9],10)

# ZADANIE 3

from decimal import Decimal

def list_generator(start=2, stop=5.5):

    step = 0.5
    value = start

    values = []

    while value <= stop:
        values.append(Decimal(value))
        value += step

    return(values)

list_generator()


print("choose mode  \nA-calculate availability \nB-check minutes for availability ")
user_mode = input("choose mode:")
if user_mode == "A":
    print("input total runtime and total downtime ")
    runtime = input("total rum-time in hours:")
    downtime = input("total down-time in hours:")
    total_time = float(runtime)+float(downtime)
    print("total runtime is",total_time)
    availability = float(runtime)/float(total_time)*100
    formatted_availability = "{:.4f}".format(availability)
    print(formatted_availability,"%")
elif user_mode == "B":
    print("choose a time period : a day or a hour   ")
    user_choice = input("choose time period :..")

    minutes_day = 1440
    minutes_hour = 60
    if user_choice == "day":
        availability = input("choose availability : 95%, 99.5%, 99.99%, 99.995%, 99.999% ")
        if availability == "95%":
            result = minutes_day * 0.5 / 100
            print(result, "minutes per day down-time if availability is 95%")
        elif availability == "99%":
            result = minutes_day * 0.1 / 100
            print(result, "minutes per day down-time if availability is 99%")
        elif availability == "99.99%":
            result = minutes_day * 0.01 / 100
            print(result, "minutes per day down-time if availability is 99.99%")
        elif availability == "99.995%":
            result = minutes_day * 0.005 / 100
            print(result, "minutes per day down-time if availability is 99.995%")
        elif availability == "99.999%":
            result = minutes_day * 0.0001 / 100
            print(result, "minutes per day down-time if availability is 99.999%")

    if user_choice == "hour":
        availability = input("choose availability : 95%, 99.5%, 99.99%, 99.995%, 99.999% ")
        if availability == "95%":
            result = minutes_hour * 0.5 / 100
            print(result*60, "seconds per hour down-time if availability is 95%")
        elif availability == "99%":
            result = minutes_hour * 0.1 / 100
            print(result*60, "seconds per hour down-time if availability is 99%")
        elif availability == "99.99%":
            result = minutes_hour * 0.01 / 100
            print(result*60, "seconds per hour down-time if availability is 99.99%")
        elif availability == "99.995%":
            result = minutes_hour * 0.005 / 100
            print(result*60, "seconds per hour down-time if availability is 99.995%")
        elif availability == "99.999%":
            result = minutes_hour * 0.0001 / 100
            print(result*60, "seconds per hour down-time if availability is 99.999%")
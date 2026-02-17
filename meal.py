def main():
    time_str = input("What's the time? ")
    try:
        time = convert(time_str)

        if 7 <= time <= 8:
            print("Breakfast time")
        elif 12 <= time <= 13:
            print("Lunch time")
        elif 18 <= time <= 19:
            print("dinner time")
        else:
            print(" ")


    except (ValueError, IndexError):
            print("Invalid time")


def convert(time):
    time = time.lower().strip()


    suffix = None
    if "am" in time or "a.m." in time:
        suffix = "AM"
        time = time.replace("a.m.", "").replace("am", "").strip()
    elif "pm" in time or "p.m." in time:
        suffix = "PM"
        time = time.replace("p.m.", "").replace("pm", "").strip()


    hours, minutes = time.split(":")
    hours = float(hours)
    minutes = float(minutes)

    if suffix == "pm" and hours != 12:
        hours += 12
    elif suffix == "AM" and hours == 12:
        hours = 0

    return hours + minutes / 60


if __name__ == "__main__":
    main()
def main():
    pace= get_pace(miles=26.3, minutes=0)
    print(f"You need to run each miles in {round(pace, 2)} minutes.")

def get_pace(miles,minutes):
    if not minutes>0:
        raise ValueError("minutes should be greater than 0.")

    return miles / minutes

main()
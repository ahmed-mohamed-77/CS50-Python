

def main():
meal_time = input("Enter times in HH:MM\n").split()

for time in alltimes:
     hour, min = [int(i) for i in time.split(":")]
     print(hour, "hours and", min, "minutes")

def convert(time):
    if time <=

if __name__ == "__main__":
    main()

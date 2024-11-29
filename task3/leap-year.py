for year in range(2000, 2025):
    if year % 400 == 0 or year % 4 == 0:
        print(f"{year} is a leap year")
    elif year % 100 == 0:
        print(f"{year}  is not a leap year")
    else:
        print(f"{year}  is not a leap year")


year = int(input("entrer year"))

if year % 400 == 0 or year % 4 == 0:
    print(f"{year} is a leap year")
elif year % 100 == 0:
    print(f"{year}  is not a leap year")
else:
    print(f"{year}  is not a leap year")




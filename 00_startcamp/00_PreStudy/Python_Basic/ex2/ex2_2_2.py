year = int(input("What year were you born? "))
if year <= 1924:
    print("The Greatest Generation")
elif year <= 1945:
    print("The Silent Generation")
elif year <= 1964:
    print("baby boomer")
elif year <= 1980:
    print("Generation X")
elif year <= 1996:
    print("millennial")
else:
    print("Generation Z")
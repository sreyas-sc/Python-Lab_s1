def character_freq():
    str=input("enter the string ")
    length=len(str)
    if "ing" in str:
        str=str+"ly"
    elif "ing" not in str:
        str=str+"ing"
    print(str)
character_freq()
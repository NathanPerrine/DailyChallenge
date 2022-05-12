def timeConversion(s):
    """
    Converts 12 hour AM/PM time to Military 24 hour time.
    "12:00:00PM" -> 24:00:00
    """
    s = s.split(":")

    if s[-1][2:] == "PM":
        if s[0] != '12':
            s[0] = str(int(s[0]) + 12)
        s[-1] = s[-1][:2]
        s = ":".join(s)
    else:
        if s[0] == '12':
            s[0] = '00'
        s[-1] = s[-1][:2]
        s = ":".join(s)

    print(s)


t1 = '12:01:00PM'
timeConversion(t1)
t2 = '12:02:00AM'
timeConversion(t2)
t3 = '12:45:54PM'
timeConversion(t3)

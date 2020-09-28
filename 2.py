# 2
seconds = int(input("Put your number here "))

hours = seconds // 3600
if hours < 10:
    hours = f"0{hours}"
minutes = seconds // 60
if minutes > 60:
    minutes %= 60
if minutes < 10:
    minutes = f"0{minutes}"
seconds %= 60
if seconds < 10:
    seconds = f"0{seconds}"

print(f"{hours}:{minutes}:{seconds}")



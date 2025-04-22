for h in range(24):
    if h == 0:
        print("12 Midnight")
    elif h == 12:
        print("12 Noon")
    elif h < 12:
        print(f"{h} AM")
    else:
        print(f"{h-12} PM")

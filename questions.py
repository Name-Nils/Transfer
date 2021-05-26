
maxmove = int(250)

def duration():
    dur = int(0)
    dur = input("How long do you want your timelapse? (mins)")
    return dur

def movement():
    move = int(0)
    move = input("How far do you want the camera to move? (mm)")
    while int(move) > maxmove:
        print("\nCan't move that far")
        move = input("How far do you want the camera to move? (mm)")
    return move
    

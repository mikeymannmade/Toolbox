def get_modifier(stat):
    modifier = 0
    stat = int(stat)
    if stat == 0:
        modifier = -3
    elif stat >= 1 and stat < 3:
        modifier = -2
    elif stat >= 3 and stat < 6:
        modifier = -1
    elif stat >= 6 and stat < 9:
        modifier = 0
    elif stat >= 9 and stat < 12:
        modifier = 1
    elif stat >= 12 and stat < 15:
        modifier = 2
    elif stat >= 15:
        modifier = 3
    return modifier
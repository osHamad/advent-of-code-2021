def main():
    with open('input.txt') as data:
        data = list(data)
        data = [i.split() for i in data]

    aim=0
    hori=0
    verti=0
    for i in data:
        if i[0] == 'up':
            aim-=int(i[1])
        elif i[0] == 'down':
            aim+=int(i[1])
        elif i[0] == 'forward':
            hori+=int(i[1])
            verti+=int(i[1])*aim
    print(hori*verti)

main()

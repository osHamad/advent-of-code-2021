def main():
    with open('input.txt') as data:
        data = list(data)
        data = [i.split() for i in data]

    up = 0
    down = 0
    forward = 0
    for i in data:
        if i[0] == 'up':
            up+=int(i[1])
        elif i[0] == 'down':
            down+=int(i[1])
        elif i[0] == 'forward':
            forward+=int(i[1])
    print((down-up)*forward)

main()

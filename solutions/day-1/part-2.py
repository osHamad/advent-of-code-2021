def main():
    with open('data.txt') as data:
        data = list(data)

    # brute force method
    x = 0
    increase = 0
    try:
        while True:
            a = int(data[3*x])+int(data[3*x+1])+int(data[3*x+2])
            x+=1
            b = int(data[3*x])+int(data[3*x+1])+int(data[3*x+2])
            if a<b:
                increase+=1
    except IndexError:
        print(increase)

main()

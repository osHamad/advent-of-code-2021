def main():
    with open('data.txt') as data:
        data = list(data)

    # brute force method
    curr_num = 0
    increase = 0

    for i in data[:len(data)-1]:
        if int(data[curr_num])<int(data[curr_num+1]):
            increase+=1
        curr_num+=1

    print(increase)

main()

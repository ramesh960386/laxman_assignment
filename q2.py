
def counter(limit, div):
    # data = [x for x in range(1, limit) if (x % div) == 0]
    data = []
    for x in range(1, limit):
        if (x % div) == 0:
            data.append(x)
    return data

        
if __name__ == '__main__':
    result = counter(1000, 11)
    print("Results: ", result)


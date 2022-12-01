

def counter(fname, length):
    num_lines = 0
    num_words = 0
    with open(fname, 'r') as f:
        for line in f:
            for word in line.split():
                if len(word) >= length:
                    num_words += 1
            num_lines += 1
    return num_lines, num_words


if __name__ == '__main__':
    fname = 'data.txt'
    try:
        num_lines, num_words = counter(fname, 5)
        print("Number of lines in text file: ", num_lines)
        print("Number of words in text file: ", num_words)
    except:
        print('File not found')
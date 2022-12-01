
def counter(string, char):
    return string.count(char)

        
if __name__ == '__main__':
    string = 'the quick brown fox jumps over the lazy dog'
    result = counter(string, 'o')
    print("Results: ", result)


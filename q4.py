list_sent = ["hello world", "i love python"]
our_dict = {}

for sent in list_sent:
    for letter in sent:
        if letter.isalpha():
            if letter in our_dict.keys():
                our_dict[letter] += 1
            else:
                 our_dict[letter] = 1


def print_hist(our_dict):
    for letter in sorted(our_dict.keys()):
        print(letter +" = "+"*"*our_dict[letter])


if __name__ == '__main__':
    print(our_dict)
    print_hist(our_dict)


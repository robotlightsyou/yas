''' this is yas's edits'''
someword = "howdy"

def main(data):
    print_some_word(data)
    data = 'test'
    print_some_word(data)

print(main)

def print_some_word(word):
    print(word)

if __name__ == "__main__":
    main(someword)

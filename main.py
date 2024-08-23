def main():
    with open('books/frankenstein.txt') as file:
        contents = file.read()
        words = contents.split()
        frequency_list = {}
        for word in words:
            splitted_word = list(word.lower())

            for char in splitted_word:
                if not char.isalpha():
                    continue

                if char in frequency_list:
                    frequency_list[char] += 1
                else:
                    frequency_list[char] = 1

        descending_frequencies = sorted(frequency_list.items(), reverse=True, key=lambda item: item[1])
        print('--- Report Start ---')
        print(f"{len(words)} words found in the book \n")
        for char, freq in descending_frequencies:
            print(f"The '{char}' character was found {freq} times")
        print('\n--- Report End ---')

if __name__ == '__main__':
    main()


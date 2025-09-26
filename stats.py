def count_words(text):
    return len(text.split())

def count_all_letters(text):
    letter_dict = {}
    for char in text:
        char = char.lower()
        if char.isalpha() == False: continue
        if char in letter_dict:
            letter_dict[char] += 1
        else: letter_dict[char] = 1

    return(letter_dict)

def numKey(e):
    print(e["num"])
    return e["num"]


def print_report(letters):
    report_dict = []
    for letter in letters:
        letter_dict = {
            "char": letter,
            "num": letters[letter]
        }
        report_dict.append(letter_dict)
    report_dict.sort(reverse=True, key=numKey)
    return(report_dict)

        

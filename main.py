text_to_morse_dict = {
    'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.',
    'g': '--.', 'h': '....', 'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..',
    'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 'q': '--.-', 'r': '.-.', 's': '...',
    't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 'y': '-.--', 'z': '--.',
    '1': '.----', '2': '..---', '3': '...--', '4': '....-', '5': '.....',
    '6': '-....', '7': '--...', '8': '---..', '9': '----.', '0': '-----', ' ': '/'
}

morse_to_text_dict = {value: key for key, value in text_to_morse_dict.items()}


def text_to_morse():
    text = input('Text: ').lower()
    morse_list = [text_to_morse_dict[t] for t in text]
    print(f'Morse: {" ".join(morse_list)}')


def morse_to_text():
    morse = input('Morse: ').lower().split()
    text_list = [morse_to_text_dict[word] for word in morse]

    text = ''
    for letter in text_list:
        text += letter

    print(text)


project_start = True
while project_start:
    user_choice = input('''
Welcome to text-morse converter.
press m to text -> morse
press t to morse -> text
press any other key to quit

answer:''')

    if user_choice.lower() == 'm':
        text_to_morse()
    elif user_choice.lower() == 't':
        morse_to_text()
    else:
        project_start = False

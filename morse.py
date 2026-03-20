#MANUAL 15
MORSE = {
    'A': '.-', 'B': '-...', 'C': '-.-.', 'D': '-..', 'E': '.',
    'F': '..-.', 'G': '--.', 'H': '....', 'I': '..', 'J': '.---',
    'K': '-.-', 'L': '.-..', 'M': '--', 'N': '-.', 'O': '---',
    'P': '.--.', 'Q': '--.-', 'R': '.-.', 'S': '...', 'T': '-',
    'U': '..-', 'V': '...-', 'W': '.--', 'X': '-..-', 'Y': '-.--',
    'Z': '--..',
    '0': '-----', '1': '.----', '2': '..---', '3': '...--',
    '4': '....-', '5': '.....', '6': '-....', '7': '--...',
    '8': '---..', '9': '----.',
    '.': '.-.-.-', ',': '--..--', '?': '..--..', "'": '.----.',
    '!': '-.-.--', '/': '-..-.', '(': '-.--.', ')': '-.--.-',
    '&': '.-...', ':': '---...', ';': '-.-.-.', '=': '-...-',
    '+': '.-.-.', '-': '-....-', '_': '..--.-', '"': '.-..-.',
    '$': '...-..-', '@': '.--.-.', ' ': '/'
}

REVERSE ={v:k for k,v in MORSE.items()}


def encode(text):
    text = text.upper()
    output = []
    for ch in text:
        output.append(MORSE.get(ch, '?'))
    return " ".join(output)+

def decode(text):
    output = []
    for ch in text.split(" "):
        output.append(REVERSE.get(ch, '?'))
    return "".join(output)



def main():
    while True:
        print("\n===== MORSE CODE CONSOLE =====")
        print("1. Encode text → Morse")
        print("2. Decode Morse → Text")
        print("3. Exit")
        choice = input("Enter choice: ")

        if choice == '1':
            text = input("Enter text: ")
            print("Morse:", encode(text))
        
        elif choice == '2':
            text = input("Enter morse code seperate by space: ")
            print("Text:", decode(text))

        elif choice == '3':
            print("Goodbye!")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()
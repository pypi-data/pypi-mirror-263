import sys
from .utils import count_words, reverse_text

def main():
    if len(sys.argv) < 2:
        print("Usage: craeved <command> <args>")
        sys.exit(1)

    command = sys.argv[1]
    if command == 'count_words':
        text = ' '.join(sys.argv[2:])
        print(f"Number of words: {count_words(text)}")
    elif command == 'reverse_text':
        text = ' '.join(sys.argv[2:])
        print(f"Reversed text: {reverse_text(text)}")
    else:
        print("Invalid command")
        sys.exit(1)

if __name__ == "__main__":
    main()

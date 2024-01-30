#Welcome to Aaryan's Python word counter.
#Enter any sentance or paragraph and the program will return the number of w used in it.
def word_counter(input_text):
    w = input_text.split()
    return len(w)


def main():
    print("Welcome to Aaryan's Python Word Counter")

    while True:
        user_input = input("Enter a sentence or paragraph: ").strip()

        if user_input:
            break
        else:
            print("Error: Please enter a non-empty input.")

    word_count = word_counter(user_input)
    print(f"Word Count: {word_count}")


if __name__ == "__main__":
    main()

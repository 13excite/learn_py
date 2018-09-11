ANSWER_DICT = {
    "How are you?": "Fine!",
    "What's sub?": "OK",
    "What do you do?": "I'am dummy",
    "What's are you doing?": "I'am working",
}
STOP_WORD = "RAZDVA"


def ask_user():
    answer = None
    while answer != STOP_WORD:
        answer = input("Enter your question:\n")
        if answer in ANSWER_DICT:
            print(ANSWER_DICT.get(answer))
        elif  answer == STOP_WORD:
            print('stopping')
        else:
            print("Have not answer")


def main():
    ask_user()


if __name__ == '__main__':
    main()
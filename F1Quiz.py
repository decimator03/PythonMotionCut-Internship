#Aaryan Rane here, welcome to my Formula 1 quiz for Python internship project...
def ask_question(question, options, correct_answer):
    print(question)
    for option in options:
        print(option)

    user_answer = input("Your answer (Enter A, B, C, or D): ").upper()

    if user_answer == correct_answer:
        print("Correct!\n")
        return 1
    else:
        print(f"Incorrect. The correct answer is '{correct_answer}'.\n")
        return 0


def f1_quiz():
    print("Welcome to Aaryan's racing quiz!\n")
    print("Note - Answer all in CAPS \n")

    questions = [
        {"question": "1. Which Formula 1 team is known for its red color?",
         "options": ["A. Mercedes", "B. Ferrari", "C. Red Bull", "D. McLaren"],
         "answer": "B"},

        {"question": "2. In which country is the famous Monaco Grand Prix held?",
         "options": ["A. Italy", "B. Monaco", "C. France", "D. Spain"],
         "answer": "B"},

        {"question": "3. Who holds the record for the most Formula 1 World Championships?",
         "options": ["A. Ayrton Senna", "B. Michael Schumacher", "C. Lewis Hamilton", "D. Sebastian Vettel"],
         "answer": "B"},

        {"question": "4. What is the name of the Indian F1 Track?",
         "options": ["A. Madras motor race track", "B. Hyderabad Street Circuit (FIA)", "C. Budhh International Circuit",
                     "D. Kari Motor Speedway"],
         "answer": "C"},

        {"question": "5. Which Indian Race driver is going to Drive an F1 car in 2024 ?",
         "options": ["A. Karun Chandhok", "B. Jehan Daruvala", "C. Kush Maini", "D. Narain Karthikeyan"],
         "answer": "C"}
    ]

    score = 0
    for i, q in enumerate(questions, 1):
        score += ask_question(q["question"], q["options"], q["answer"])

    print(f"Quiz completed! Your score: {score}/{len(questions)}")
    print("All the best for your RACING LIFE !!!")


if __name__ == "__main__":
    f1_quiz()

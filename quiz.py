
import question
import random


def main():
    q1 = question.Question("What was the first planet that the covenant invaded?", "Harvest", "Earth",
                           "Reach", "Onyx", "A")
    q2 = question.Question("What year did the Human-Covenant war start?", "2020", "2457", "2525", "2552", "C")
    q3 = question.Question("What was the way the Covenant destroyed human worlds?", "Infection", "Glassing",
                           "Overwhelming Forces", "Both B and C", "D")
    q4 = question.Question("What was the name of the Spartan that saved humanity?", "Kat-B320", "Lucy-B901",
                           "John-117", "Jorge-052", "C")
    q5 = question.Question("What event was the beginning of the end for the Covenant empire?", "The Great Break",
                           "The Great Schism", "The Grunt Rebellion", "The Great Journey", "B")
    q6 = question.Question("What was the name of the forces of Humanity?", "UNSC", "USMC", "UEDF", "EDFC", "A")
    q7 = question.Question("What species of alien lead the Covenant?", "Prophets", "Elites", "Brutes", "Grunts", "A")
    q8 = question.Question("What was the name of the AI(Artificial intelligence) that helped saved humanity?",
                           "Linda", "Henry", "Cortana", "Jessamine", "C")
    q9 = question.Question("What alien super-weapon was the Covenant going to fire to wipe all life out in the galaxy?",
                           "Ring", "Halo", "Journey", "Laser", "B")
    q10 = question.Question("What was the name of the installation that Humanity defeated the Covenant at?", "Installation 00",
                            "Installation 01", "Installation 04", "Installation 07", "A")

    all_the_questions = (q1, q2, q3, q4, q5, q6, q7, q8, q9, q10)
    print("---Player 1---")
    player_1 = ask(all_the_questions)
    print("---Player 2---")
    player_2 = ask(all_the_questions)

    if player_1 == player_2:
        print("It's a tie!!")
    elif player_1 > player_2:
        print("Player one wins!!")
    else:
        print("Player two wins!!")


def ask(all_questions):
    correct = 0
    for item in range(5):
        player_questions = random.choice(all_questions)
        print(player_questions.get_question())
        print("A. " + player_questions.get_answer1())
        print("B. " + player_questions.get_answer2())
        print("C. " + player_questions.get_answer3())
        print("D. " + player_questions.get_answer4())
        player_response = input("What is the answer?: ")

        if player_response.upper() == player_questions.get_correct_answer():
            print("\n Nice job, you got that one right!\n\n")
            correct += 1
        else:
            print("Didn't get that one right\n\n")

    return correct


main()

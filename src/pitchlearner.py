from random import randint, shuffle
import sys
import pygame
import pygame.sndarray
import time

from test.test_data import QuizQuestions, answer_key
from src.pitchlearner_types import *


def get_question(index: int) -> Union[QuizQuestion, None]:

    try:
        return QuizQuestions[index]
    except IndexError:
        return None


def generate_quiz(quiz_length: int, num_answers: int) -> PitchQuiz:
    quiz = []
    for index in range(0, quiz_length):
        quiz.append(generate_quiz_question(num_answers))
    return quiz


def get_random_answer():
    random_int = randint(0, len(QuizQuestions) - 1)
    random_question = get_question(random_int)
    return answer_key[random_question]


def is_list_unique(loa: List[Any]) -> bool:
    return is_list_unique_acc(loa, [])


def is_list_unique_acc(loa: List[Any], acc: List[Any]):
    if len(loa) == 0:
        return True
    else:
        first = loa[0]
        rest = loa[1:]
        return first not in acc and is_list_unique_acc(rest, acc + [first])


def get_n_random_other_answers(num_answers: int, right_answer: Answer) -> List[Answer]:
    rand_answers = [right_answer]
    for i in range(0, num_answers):
        random_answer = get_random_answer()
        while random_answer in rand_answers:
            random_answer = get_random_answer()
        rand_answers.append(random_answer)
    return rand_answers


def generate_quiz_question(num_answers: int) -> QuizQuestion:
    rand_int_index = randint(0, len(QuizQuestions) - 1)
    random_question = get_question(rand_int_index)
    correct_answer = random_question[1]

    answers = get_n_random_other_answers(num_answers - 1, correct_answer)

    shuffle(answers)

    return QuizQuestion((random_question, answers, correct_answer))


def generate_prompt(question: QuizQuestion) -> str:
    question_prompt = question[0][0]
    frequency = question[0][1]
    prompt = question_prompt + '\n'
    potential_answers = question[1]
    answer_number = 1
    for pot_ans in potential_answers:
        prompt += str(answer_number) + ") " + str(pot_ans) + "\n"
        answer_number += 1
    return prompt


def play_sound(sound_file: str, ms: int) -> ():
    pygame.mixer.music.load(sound_file)
    pygame.mixer.music.play(-1)
    time.sleep(ms)
    pygame.mixer.music.stop()


def is_correct_answer(chosen_answer_index: int, question: QuizQuestion) -> bool:
    correct_answer = question[2]
    potential_answers = question[1]
    chosen_answer = potential_answers[chosen_answer_index - 1]
    return chosen_answer == correct_answer


def main():
    quiz_length = int(sys.argv[1])
    answer_length = int(sys.argv[2])

    questions = generate_quiz(quiz_length, answer_length)

    for question in questions:
        user_has_chosen_correctly = False
        # Present Question and play sound
        prompt = generate_prompt(question)
        play_sound(question[0][2], 5)
        # Prompt user for answer

        while not user_has_chosen_correctly:
            chosen_answer_index = int(input(prompt))
            user_has_chosen_correctly = is_correct_answer(chosen_answer_index, question)


if __name__ == "__main__":
    pygame.mixer.init()
    main()

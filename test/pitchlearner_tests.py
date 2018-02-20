import unittest

from src.pitchlearner import *
from test.test_data import *
import pygame

class TestPitchLearner(unittest.TestCase):

    def setUp(self):
        pygame.mixer.init()
        self.simple_quiz_question = QuizQuestion((question_a, [440, 320, 799], 440))

    def test_get_question(self):
        self.assertEquals(None, get_question(100000000))
        self.assertEquals(question_c, get_question(0))

    def test_generate_quiz(self):
        pass

    def test_get_n_random_other_answers(self):
        correct_answer = get_random_answer()
        three_random_answers = get_n_random_other_answers(2, correct_answer)
        self.assertEquals(3, len(three_random_answers))
        self.assertTrue(is_list_unique(three_random_answers))

    def test_generate_prompt(self):
        expected_prompt = """What pitch is this?\n1) 440\n2) 320\n3) 799\n"""
        self.assertEquals(expected_prompt, generate_prompt(self.simple_quiz_question))

    def test_generate_quiz_question(self):
        quiz_q = generate_quiz_question()
        question = quiz_q[0]
        correct_answer = answer_key[question]
        self.assertEquals(correct_answer, quiz_q[2])
        self.assertEquals(3, len(quiz_q[1]))
        self.assertTrue(correct_answer in quiz_q[1])
        self.assertTrue(is_list_unique(quiz_q[1]))

    def test_integration(self):
        pass

    def test_list_unique(self):
        unique_list = [1, 2, 3]
        empty_list = []
        not_unique_list = [1, 2, 1]
        self.assertTrue(is_list_unique(empty_list))
        self.assertTrue(is_list_unique(unique_list))
        self.assertFalse(is_list_unique(not_unique_list))

    def test_play_sound(self):
        play_sound(question_c[2], 5)
        self.assertTrue(True)

    def test_is_correct_answer(self):
        self.assertTrue(is_correct_answer(440, self.simple_quiz_question))
        self.assertFalse(is_correct_answer("34234", self.simple_quiz_question))
        self.assertFalse(is_correct_answer(320, self.simple_quiz_question))

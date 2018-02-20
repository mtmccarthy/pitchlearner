from typing import NewType, List, Tuple, Any, Dict, Union

StrAnswer = NewType('StrAnswer', str)
IntAnswer = NewType('IntAnswer', int)

Answer = Union[StrAnswer, IntAnswer]

PitchQuestion = Tuple[str, int]  # (Path to sound file, frequency)

Question = Union[PitchQuestion]

AnswerKey = Dict[Question, Answer]

QuizQuestion = NewType("QuizQuestion", Tuple[Question, List[Answer], Answer])

PitchQuiz = NewType("PitchQuiz", List[QuizQuestion])

num_answers = 3

Quiz = Tuple[List[Question], int, List[Answer]]  # (List of questions, current index, current answers to questions)

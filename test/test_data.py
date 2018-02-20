from src.pitchlearner_types import *



pitch_question_str = "What pitch is this?"

question_c = (pitch_question_str, 262, "../notes/Piano.ff.C4.aiff")
question_c_sharp = (pitch_question_str, 277, "../notes/Piano.ff.Db4.aiff")
question_d = (pitch_question_str, 294, "../notes/Piano.ff.D4.aiff")
question_d_sharp = (pitch_question_str, 311, "../notes/Piano.ff.Eb4.aiff")
question_e = (pitch_question_str, 330, "../notes/Piano.ff.E4.aiff")
question_f = (pitch_question_str, 349, "../notes/Piano.ff.F4.aiff")
question_f_sharp = (pitch_question_str, 370, "../notes/Piano.ff.Gb4.aiff")
question_g = (pitch_question_str, 392, "../notes/Piano.ff.G4.aiff")
question_g_sharp = (pitch_question_str, 415, "../notes/Piano.ff.Ab4.aiff")
question_a = (pitch_question_str, 440, "../notes/Piano.ff.A4.aiff")
question_a_sharp = (pitch_question_str, 466, "../notes/Piano.ff.Bb4.aiff")
question_b = (pitch_question_str, 494, "../notes/Piano.ff.B4.aiff")

QuizQuestions = [question_c,
                 question_c_sharp,
                 question_d,
                 question_d_sharp,
                 question_e,
                 question_f,
                 question_f_sharp,
                 question_g,
                 question_g_sharp,
                 question_a,
                 question_a_sharp,
                 question_b]

answer_key = {}
for quiz_question in QuizQuestions:
    answer_key[quiz_question] = IntAnswer(quiz_question[1])

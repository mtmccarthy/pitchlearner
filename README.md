# pitchlearner
An application to help people learn to hear notes by their pitch

## How to Use this Application

### Clone && Install Requirements
```git clone https://github.com/mtmccarthy/pitchlearner.git```

```pip install -r requirements.txt```

### Run Application
```python pitchlearner/src/pitchlearner.py <quiz_length> <num_answers>```

This application takes two arguments, both integers. The first is interpreted as the length of the quiz the user wishes to complete. The second argument is interpreted as the number of answers to prompt the user with.

#### Answer a Quiz Question
Currently the application plays a note between the ranges of C4-B4 inclusive. After playing the sound for five seconds the application displays a given number of possible frequencies of the note that was just played. Example:
```
  What is the frequency?
  1) 440
  2) 262
  3) 494
```
The application then prompt the user for their answer. The answer is interpreted as the number left of the frequency. So if the user believes the frequency played was an A4 they would input "1".

##### Correct Answer
If the user enters the correct answer the following question will be prompted until there are no more questions to display.

##### Wrong Answer
If the user enters an incorrect answer, the application will continue prompting for another answer until a correct answer is given.

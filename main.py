import requests
from quiz_brain import QuizBrain
from ui import Interface

ADDRESS = 'https://opentdb.com/api.php'
parameters = {'amount': 10, 'type': 'boolean'}

data = requests.get(url=ADDRESS, params=parameters)
questions = data.json()['results']

brain = QuizBrain(q_list=questions)
interface = Interface(brain)

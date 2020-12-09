import random

random_responses = ['ha ha scrub!', 'nice', 'good', 'too bad']
ran_num_response = random.randint(0, len(random_responses))

person_question = (input('Are you in school? '))

if (person_question != ""):
	print (random_responses[ran_num_response])

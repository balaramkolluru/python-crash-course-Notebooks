from survey import AnonymusSurvey

#Define a question, make a survey.
question = 'What language did you first learn to speak?'
my_survey = AnonymusSurvey(question)

#Show the question and store responses to the question..
my_survey.show_question()
print("Enter 'q' at any time to quit.\n")
while True:
	response = input("Language:")
	if response == 'q':
		break
	my_survey.store_response(response)

#Show survey results
print("\nThankyou every one who participated in the survey!")
my_survey.show_results()
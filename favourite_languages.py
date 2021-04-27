favourite_languages = {
	'jen' : ['python', 'ruby'],
	'sarah' : ['c'],
	'edward' : ['ruby', 'go'],
	'phil' : ['go', 'pascal'],
}

for name, languages in favourite_languages.items():
	print(f"{name.title()}'s, favourite languages are:")

	for language in languages:
		print(f"\t{language.title()}")
#if 'edward' not in favourite_languages:
	#print(f"edward, please take our poll!")

#friends = ['phil', 'sarah']
#for name in favourite_languages:
	#print(name.title())

	#if name in friends:
		#language = favourite_languages[name].title()
		#print(f"\t{name.title()} I see you love {language}!")

#for name , language in favourite_languages.items():
	#print(f"{name.title()}'s favourite language is {language.title()}.")

#language = favourite_languages['sarah'].title()
#print(f"Sarah's favourite lannguage is {language}!")
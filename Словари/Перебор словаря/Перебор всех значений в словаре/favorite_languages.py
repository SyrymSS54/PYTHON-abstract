favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

#print("Sarah's favorite language is " + favorite_languages['sarah'].title() + ".")

print("The following languages have been mentioned:")
for language in favorite_languages.values():
    print(language.title() + "\n")

print("The following languages have been mentioned:")
for language in set(favorite_languages.values()):
    print(language.title())   
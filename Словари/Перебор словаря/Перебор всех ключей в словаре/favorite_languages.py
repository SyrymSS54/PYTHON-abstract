favorite_languages = {
    'jen':'python',
    'sarah':'c',
    'edward':'ruby',
    'phil':'python',
}

friends = ['phil', 'sarah']

for name in favorite_languages.keys():
    
    if name not in friends:
        print(name.title())

    elif name in friends:
        print("Hi " + name.title() + ", I see your favorite language is " + favorite_languages[name].title() + "!")

if 'erin' not in favorite_languages.keys():
    print("\nErin, please take our poll!")        
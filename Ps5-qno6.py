# If names of 2 freinds are same, what will to the program in problem5 .. .  



favorite_languages = {
    'Manish': 'python',
    'Abhishek': 'c',
    'Manish': 'ruby',
    'Prateek': 'python',
    }

for name, language in favorite_languages.items():
    print(name.title() + "'s favorite language is " +
        language.title() + ".")

print("\n")

coders = ['Abhishek', 'Rohan', 'Prateek', 'Manish', 'Rohit', 'Sudeep', 'Ravi']
for coder in coders:
    if coder in favorite_languages.keys():
        print("Thank you for taking the poll, " + coder.title() + "!")
    else:
        print(coder.title() + ", what's your favorite programming language?")
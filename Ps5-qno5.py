# Create a dictionary . allow 4 friends to enter their favourite language as values and use keys as their names. Assume that the names are unique........ 



favorite_languages = {
    'Manish': 'python',
    'Abhishek': 'c',
    'Rohan': 'ruby',
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
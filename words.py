import random
print('welkome....')
print('...enter yo question!w')

while True:


    question = input('> ')

    answers = [
        'no.','maybe','dont ask',
        'i am going to come to yo house in a cow suit',
        'the cow says moooo','milky'
    ]


    answer = random.choice(answers)
    print(answer)

import random
print('welkome....')
print('...type yo question!')

while True:


    question = input('> ')

    answers = [
        'no.','maybe','dont ask',
        'i am going to come to yo house in a cow suit',
        'the cow says moooo','milky','yaa buddy',
        'welkom to the dark side   we have cookies'
    ]


    answer = random.choice(answers)
    print(answer)

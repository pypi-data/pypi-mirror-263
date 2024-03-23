import random
list_of_words = ['hello','ball','there','movie','train','escape','timer','beginning','song','answer']
def random_word():
    rand = random.randrange(0,len(list_of_words)+1)
    return list_of_words[rand]
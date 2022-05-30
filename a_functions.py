import random
from re import A 

#Reading the txt file
def file_reader(file):
    new_list = []
    with open(file, 'r') as text:
        reader  = text.readlines()
        for line in reader:
            new_list.append(line.rstrip())
    return new_list

#picking three random words from a txt file
def three_options(file):
    new_list = file_reader(file)
    new_random = random.sample(new_list,3)
    for count, anime in enumerate(new_random, start=1):
        print(count, anime)

def answer(file):
    new_list = file_reader(file)
    correct = random.choice(new_list)
    return correct


#selecting the word from the random list
def pick_choice():
    selected = random.choice(three_options())
    return selected

#Hint Giver
def hint_giver(file):
    a = answer(file)
    b = list(a)
    c = b[0:3]
    print(''.join(c),'...')

    

    

if __name__ == "__main__":
    #file_reader('anime_names.txt')
    #three_options('anime_names.txt')
    #answer('anime_names.txt')
    hint_giver('anime_names.txt')


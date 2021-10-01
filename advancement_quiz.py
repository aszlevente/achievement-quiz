import json
import random

def game() :
    questionN = 5
    score = 0

    with open('advancements.txt') as file :
        advancements = json.load(file)

    #list(advancements.keys())

    while True :
        reply = input('Gamemode:  (all, category) ').lower()
        if reply in ['all', 'category'] :
            break
        else :
            print('Na ezt most nem értettem!')

    if reply == 'category' :
        while True :
            reply = input('Category: '+', '.join(list(advancements.keys())).lower()+' ').lower()
            if reply in [i.lower() for i in advancements.keys()] :
                break
            else :
                print('Na ezt most nem értettem!')
                

    print('\n\n\n')

    adv = {}
    if reply == 'all' :
        for i in advancements :
            for l in advancements[i] :
                adv[l] = advancements[i][l]

    else :
        adv = advancements[reply.title()]

    for i in range(questionN) :
        choice = random.randint(0, len(adv)-1)
        question = adv[list(adv.keys())[choice]]
        print(question+'\n')
        answer = list(adv.keys())[list(adv.values()).index(question)]
        playerAns = input('Na erre mit lépsz? ')
        if playerAns.lower() == answer.lower() :
            print('GG Ezt eltaláltad!\n')
            score += 1
        else :
            print('Hát ez nem talált!')
            print('Megoldás: '+answer+'\n')
        adv.pop(answer)

    print('A pontszámod: '+str(score))

while True:
    game()
    if input("Egy replay? (y/n) " == 'n'):
        break

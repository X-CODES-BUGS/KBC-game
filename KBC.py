import question_printer as q
import user
from playsound import playsound



kbc = 'Kaun Banega Crorepati'
kbc1 = "KBC"
active = True
i = 1
n = 1
rupees = '₹'
a = user.User()
b= q.Question()
li = a.l1+a.l2+a.l3+a.l4
print('\n'+kbc1.center(110))
print(kbc.center(110))
# playsound('kbc2.mp3')
a = user.Rules()
a.all_rules()
a.user_account()
start = input('\nEnter START to begen the game or CLOSE to stop the program: ')
# start = start.lower()
if start.lower().strip() == 'start':
    # with open
    # print(f'{first_name} you currently owe {rupees}{first_name.money}')
    for x in range(1,18):
        if b.flag==1:
            if (x==1) or(x==6) or(x==11) or(x==16):
                print(f'\nLets begin th LEVEl {n}')
                n=n+1
        if b.flag==1:
            print(f'Question {x} - {rupees}{li[x-1]}')
            print(f'Q{x}.',end=' ')
            b.all_in_one()
            print('')
        elif b.flag==0:
            print('\nYou lose...')
            print(f'Prize money won: {rupees}{a.money}')
            # for i in range(6):
            #     if ','in a.money:
            #         a.money=a.money.replace(',','')
            # a.i_dont_know(a.money)
            i=i-1
            break
        if (x == 5) or (x == 10) or (x == 15)or(x == 17):
            if b.flag==1:
                print(f'Congratulations, you completed the level-{i} and won {rupees}{li[x-1]}')
                i = i+1
                a.money= (li[x-1])
    else:
        print(f'Congratulations, you compeleted the game and won {rupees}{li[-1]}.')        
# b.save_record()
print('\nThank you for playing the game.')       
print('The END...')
a.i_dont_know(a.money)


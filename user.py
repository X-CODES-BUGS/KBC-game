# import question_printer as d
class User:
    name=''
    password= ''
    highest_score=0
    file_line = ''
    content=''
    # sname=''
    # location=''
    l1 = ['1,000', '2,000', '3,000', '5,000', '10,000']
    l2 = ['20,000', '40,000', '80,000', '1,60,000', '3,20,000']
    l3 = ['6,40,000', '12,50,000', '25,00,000', '50,00,000' , '75,00,000']
    l4 = ['1,00,00,000', '7,00,00,000']
    enter_help = {'Change The Question' : 'enter CHANGE',
           '50:50': 'enter 50',
            'Double Tip' : 'enter DOUBLE',
            'Ask The Expert': 'enter EXPERT'
            }
    def __init__(self):
        self.money = 0
        self.question = 1
        self.fifty = 1
        self.tip = 1
        self.expert = 1
        self.lf = {'Change The Question' : 'It changes the Question',
           '50:50': 'It removes 2 wrong option',
            'Double Tip' : 'It let you take two chance in a question',
            'Ask The Expert': 'You will be suggest an answer by an expert'
            }
    
    def user_info(self):

        self.name= input('Enter your name: ')

        # self.fname= input('Enter your first name: ')
        # self.sname= input('Enter your second name: ')
        self.password = input('Create a easly password name: ')
        # self.location= input('Enter your location: ')         
        for i in range(6):
            if ' 'in self.name:
                self.name=self.name.replace(' ',"")
            if ' 'in self.password:
                self.password=self.password.replace(' ',"")
        self.name = self.name.strip()
        self.password = self.password.strip()
        self.name  =  self.name.lower()
    def signup(self):
        self.user_info()
        with open('E:\\Xcode\\python\\projects\\KBC\\players.txt','a') as f:
            # f.write(f'{self.name}')
            # f.write(f'{self.password}')
            f.write(f'\n{self.name.lower()}\n')
            f.write(f'{self.password.lower()}\n')
            f.write(f'{self.money}\n')

    def login(self):
        a = input('Enter you name: ')
        a=a.lower()
        a=a.strip()
        b = input('Enter you password: ')
        # b=b.lower()
        b=b.strip()
        a = a+'\n'
        b = b+'\n'
        with open('players.txt','r+') as f:
            content = f.readlines()
            # con = f.read()
        # con = con.split('\n')
            # content=content.lower()
        if (a in content) and (b in content):
            # print(content)
            a=a[:-1]
            # print(a)
            print('\nWelcome back', a+'!!')
            # print(a)
            # self.file_line= a
            # self.file_line=int(self.file_line)
            self.content=content
            das=self.update(content,a)
            print(f'Last time you won: ₹{das}')
        elif (a not in content) or (b not in content):
            print('\nAccount not founded\nMaking a new account...')
            self.signup()
        else:
            print('Invaid input\nYou are playing as GUEST')
    def update(self,content,a):
        com = a+'\n'
        # print(content)
        content = list(content)
        ind= content.index(com)
        ind = int(ind)
            # print(ind)
        self.file_line=int(ind+3)
        with open('players.txt','r+') as f:
            for i in range(ind+5):
                    das =f.readline()
            print(das)
        self.highest_score=int(das)
        return das
    def i_dont_know(self,n):
        print(self.money)
        print(type(self.money))
        print(n)
        print(type(n))
        try:
            self.money=str(self.money)
            n = str(n)
            for i in range(6):
                if ','in self.money:
                        self.money=self.money.replace(',','')
                if ','in n:
                        n=n.replace(',','')
            # print(n)
            n = int(n)
            if n>self.highest_score:
                # print(self.content)
                # a = self.content.split('\n')
                a=[]
                a[:]=self.content[:]
                d= str(n)
                # print('hello')
                # print(d)
                # print(self.file_line)
                a[self.file_line-1]=d
                a=str(a)
                # print(a)
                # print(type(a))
                for i in range(20):
                    if ('[' in a) or (']' in a) or ("'" in a)or ('\\n' in a)or (' ' in a):
                    # c = a[i]+'\n'
                        # print(i)
                        a = a.replace('[','')
                        a = a.replace(']','')
                        a = a.replace(',','')
                        a = a.replace("'",'')
                        a = a.replace("\\n",'\n')
                        a = a.replace(" ",'\n')
                with open('players.txt','w') as f:
                    f.write(a)
                # print(a)
                # print(type(a))

                    
                # with open('players.txt','r+') as f:
                    # for i in range(self.file_line)
        except :
            print('Error in saving score.')
            print('The problem will be fixed as soon as possible')

        
    def user_account(self):
        print('\nYou need to have an account to save your highest score in the game')
        acc=input('LOGIN or SIGNUP or GUEST: ' )
        acc = acc.lower()
        acc = acc.strip()
        if acc=='login':
            self.login()
        elif acc == 'signup':
            self.signup()
        elif acc == 'guest':
            print('You are playing as GUEST')
        else:
            print('Invaid input\nYou are playing as GUEST')  
    
class Life_line(User):
    ask = 1
    fifty = 1
    dou = 1
    exp = 1
    def __init__(self):
        super().__init__()   

    def use_life(self):
        i=1
        for x in self.lf.keys():
            print(f'Enter {i} for {x}')
            i=i+1
        en  = int(input(('Enter the life line: ')))
        return en
    def ask_a(self):
        if self.ask==1:
            pass




class Rules(User):
    rule = '**********RULES**********'

    def logo_rule(self):
        print('\n\n'+self.rule.center(110))

    def rule_1(self):
        prize = ['1,000', '2,000', '3,000', '5,000', '10,000', '20,000', '40,000', '80,000', '1,60,000', '3,20,000', '6,40,000', '12,50,000', '25,00,000', '50,00,000', '75,00,000','1,00,00,000', '7,00,00,000']

        print('1. There will 17 question with 4 options and the value is as follows:')
        for i in range(1,18):
            if (i==1) :
                print(f'\nLEVEL {i}')
            elif (i==6):
                print(f'LEVEL {2}')
            elif (i==11):
                print(f'LEVEL {3}')
            elif (i==16):
                print(f'LEVEL {4}')
            print(f'\tQ.{i}. ₹{prize[i-1]}')

    def rule2(self):
        i = 1
        print('2.',end='')
        print('There are 4 life line(helping hands):')
        for k,v in self.lf.items():
            print(f'\t{i}. {k}: {v}')
            i=i+1
        print('\nYou can use them only ones in the game by entering HELP.')

    def rule3(self):
        print('3. You will win the final amount of the levels you have completed.')
        # print('For example, if t')
    def rule4(self):
        print('4. Enter RULES for see this rules again.')

    def all_rules(self):
        self.logo_rule()
        self.rule_1()
        print('')
        self.rule2()
        print('')
        self.rule3()
        print('')
        self.rule4()
        # print('')
        
# a = Life_line()
# # a.use_life()
# b = a.use_life()
# print(b)



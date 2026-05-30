import random
import user
# def lev(level):
#     if level==1:
#         fi = 'L1.txt'
#         no = list(range(1,361,6))
#         x = random.randint(1,361,6)
#     elif level==2:
#         x = random.randint(4,5)
#     elif level==3:
#         x = random.randint(4,5)
#     elif level==4:
#         x = random.randint(4,5)
#     else:
#         print('No level enter')
#         x = random.randint(4,5)
#     return x,fi

# def quest(level):
    # t = lev(level)
    # with open(t[1]) as q:
        # for i in range(t[0]):
    #         content = q.readlines()
    # return (content)

# def mcq():
#     a = quest()

# def ans(content):
    # content = str(content)
    # content = content.strip()
    
class Question(user.Life_line,user.Rules):
    file = ['chat_gbt.txt','chat_gbt.txt','chat_gbt.txt','chat_gbt.txt']
    all_quest = []
    all_quest_num = []     #store q
    all_quest_file_order = []      #store file name of every questions
    all_quest_mcq=[]
    print_quest = ''
    user_answer = ""
    right_answer= ''
    suspence = ''
    flag = 1
    file_name = 'E:\Xcode\python\projects\KBC\chat_gbt.txt'    #temp. store lastest file name
    file_name = 'chat_gbt.txt'    #temp. store lastest file name
    option = ['a','b','c','d']
    b= []
    on=0
    def num_line(self,f):
        with open(f) as g:
            con = len(g.readlines())
        return con
    def fil(self):
        a = random.choice(self.file)
        if a == 'chat_gbt.txt':
            self.on=0
        elif a == 'questions.txt':
            self.on=1
        self.all_quest_file_order.append(a)
        return a
    def quest_select(self):
        # self.file_name = self.fil()
        last_num =self.num_line(self.file_name)
        li = list(range(1,last_num,6))
        q= random.choice(li)
        # self.all_quest_num.append(q)
        return q
    def quest_print(self,manu=None,manu_num=None):
        q = self.quest_select()
        # print(q)
        if manu:
            # print(manu)
            self.file_name=manu
        if manu_num:
            # print(manu_num)
            # manu_num = manu_num+1
            q=manu_num
            # print(f'q=')
        self.all_quest_num.append(q)
        with open(self.file_name) as f:
            for i in range(1,q+1):
                question = f.readline()          
            m1 = f.readline()
            m2 = f.readline()
            m3 = f.readline()
            m4 = f.readline()
            ans = f.readline()
        question = question.strip()
        m1 = m1.strip()
        m2 = m2.strip()
        m3 = m3.strip()
        m4 = m4.strip()
        ans = ans.strip()
        ans = ans.lower()
        if manu_num:
            # print(self.all_quest_num)
            self.right_answer = ans[-1:]
            if self.file_name== 'chat_gbt.txt':
                self.right_answer = ans[8:9]
            self.print_quest = (f'{question}\n{m1}\n{m2}\n{m3}\n{m4}')
            # print(manu_num)
            # print(self.right_answer)
        else:
            if question in self.all_quest: 
                self.quest_print()
            else:
                self.all_quest.append(question)
                self.right_answer = ans[-1:]
                if self.file_name== 'chat_gbt.txt':
                    self.right_answer = ans[8:9]
                self.print_quest = (f'{question}\n{m1}\n{m2}\n{m3}\n{m4}')
            # print(manu_num)
            # print(self.right_answer)
        # print(self.all_quest)
    def ans_input(self):
        print('[Note:Enter answer in options: A, B, C or D]')
        a = input('Enter your answer:')
        a=a.lower()
        a=a.strip()
        self.user_answer = a
    def asd(self,a):
        self.b[:]= self.option[:]
        self.b.remove(a)
        d= random.choice(self.b)
        self.b.remove(d)
        return self.b

    def else_help(self):
            print('\n**************\nYou have already used it.\nTry again or cancel.\n**************\n')
            self.help()
    def call_same_question(self):
        li = str(self.all_quest_file_order[-1:])
        li = li[2:-2]
        li1 = str(self.all_quest_num[-1:])
        li1 = li1[1:-1]
        li1 = int(li1)
        self.all_in_one(li,li1)
    def store_question_mcq_in_list(self,inj):
        ss = self.asd(inj)   #list of wrong ans
        self.all_quest_mcq.append(self.print_quest)
        a = self.all_quest_mcq[-1:]
        # print(a)
        a = str(a) 
        a= a[2:-2]
        # print(a)
        # print(type(a))
        # for i in 10:
            # if '//'
        b = a.split('\\n')
        # print(self.print_quest)
        # print(self.all_quest_mcq)
        print(b[0])
        # print(type(b))
        # print(b)
        # print(a)
        for i in b[1:]:
            # for x in ss:
            if (i.startswith(ss[0]) == False) and (i.startswith(ss[1]) == False):
                    print(i)



    def help(self):
        # if self.user_answer=='help':
            print('')
            intro = 'LIFE-LINE'
            print(intro)
            for k,v in user.User.enter_help.items():
                print(f'To apply life_line {k}, you need to enter {v}.')
            print('\n*****To cancel, you need to enter CANCEL.*****\n')
            a = input('Enter your life-line: ')
            a=a.strip()
            a=a.upper()
            if a == 'CHANGE':
                if user.Life_line.ask ==1:
                    self.user_answer=''
                    user.Life_line.ask =0
                    self.all_in_one()
                else:
                   self.else_help()
            elif a == '50':
                if user.Life_line.fifty ==1:
                    self.user_answer=''
                    user.Life_line.fifty =0
                    if self.right_answer =='a':
                        self.store_question_mcq_in_list('a')
                    elif self.right_answer =='b':
                        self.store_question_mcq_in_list('b')
                    elif self.right_answer =='c':
                        self.store_question_mcq_in_list('c')
                    elif self.right_answer =='d':
                        self.store_question_mcq_in_list('b')
                    else:
                        print('error')
                    a1 = input(f'Enter the answer: ')
                    a1 = a1.strip()
                    a1 = a1.lower()
                    self.user_answer=a1
                    if a1 == 'help':
                        self.help()
                    else:
                        self.ans_check()
                    print(self.suspence)
            #             self.option.remove(a)
            #         elif self.right_answer =='b':
            #         elif self.right_answer =='c':
            #         elif self.right_answer =='d':
                else:
                   self.else_help()
            elif a == 'DOUBLE':
                if user.Life_line.dou ==1:
                    self.user_answer=''
                    user.Life_line.dou =0
                    a1 = input(f'First change, enter the answer: ')
                    a2 = input(f'Second change, enter the answer: ')
                    a1 = a1.strip()
                    a1 = a1.lower()
                    a2 = a2.strip()
                    a2 = a2.lower()
                    if a1== self.right_answer:
                        self.user_answer =  a1
                        self.ans_check()
                        print(f'The correct answer is option {self.right_answer}')
                    elif a2== self.right_answer:
                        self.user_answer =  a2
                        self.ans_check()
                        print(f'The correct answer is option {self.right_answer}')
                    else:
                        self.user_answer =  a2
                        # print('Both are wrong')
                        self.ans_check()
                        self.suspence= f'Your answer is WRONG...\nThe correct answer is option {self.right_answer}'
                        # print(self.suspence)
                    print(self.suspence)

                else:
                   self.else_help()
            elif a == 'EXPERT':
                if user.Life_line.exp ==1:
                    self.user_answer=''
                    user.Life_line.exp =0
                    print(f'\n**********The expert suggest option {self.right_answer.upper()}.**********')
                    # li = str(self.all_quest_file_order[-1:])
                    # li = li[2:-2]
                    # li1 = str(self.all_quest_num[-1:])
                    # li1 = li1[1:-1]
                    # li1 = int(li1)
                        # li1 = li1+1
                        # print(li,li1)
                        # print(type(li1))
                        # print('hello')
                    # self.all_in_one(li,li1)
                    self.call_same_question()
                else:
                   self.else_help()
            elif a=='CANCEL':
                print('')
                self.call_same_question()
            else:
                print('\nInvalid input...\n')
                self.call_same_question()
                

    def ans_check(self):
        if self.user_answer == self.right_answer:
            self.suspence='Your answer is RIGHT!!'
        elif self.user_answer != self.right_answer:
            self.suspence= f'Your answer is WRONG...\nThe correct answer is option {self.right_answer}'
            self.flag = 0
        else:
            self.suspence='ERROR..'
    # def ans_check_gbt(self):
    #     self.user_answer = self.user_answer[8:9]
    #     self.right_answer = self.right_answer[8:9]
    #     if self.user_answer == self.right_answer:
    #         self.suspence='Your answer is RIGHT!!'
    #     elif self.user_answer != self.right_answer:
    #         self.suspence= f'Your answer is WRONG...\nThe correct answer is option {self.right_answer}'
    #         self.flag = 0
    #     else:
    #         self.suspence='ERROR..'
    def save_record(self):
        # print('hello')
        self.money=str(self.money)
        for i in range(6):
                if ','in self.money:
                    self.money=self.money.replace(',','')
        # self.i_dont_know(self.money)
    def all_in_one(self,m1=None,m2=None):
        self.quest_print(m1,m2)
        print(self.print_quest)
        # print(self.right_answer)
        self.ans_input()
        if self.user_answer=='help':
            self.help()
        elif (self.user_answer == 'rule') or (self.user_answer == 'rules'):
            print('')
            user.Rules.all_rules()
        else:
            # if self.on == 1:
                self.ans_check()
            # elif self.on == 0:
                # self.ans_check_gbt()
            # else:
                # print('error')
                print(self.suspence)
        # print(self.user_answer,self.right_answer)


# quest_print()
# a = Question()
# a.all_in_one()

    
    
print('Hello, world! Im funny cmd.. You can enter some dumb commands and see what happened! ')
cmdcom = input('Wait for input... ')

#---------------------------- HELP

if cmdcom == ('/Help'):
    import time
    time.sleep(0.4)
    print(' @: hello! im ur virtual helper!')
    time.sleep(0.7)
    print(' @: here some ellementar commands:')
    time.sleep(0.7)
    print('/Echo - repeating all you enter')
    time.sleep(0.7)
    print('/Calculate - calculator, lol')
    time.sleep(0.7)
    print('/Time - displays currient time')
    time.sleep(0.7)
    print('/Bye - exit')
    time.sleep(0.7)
    print('@: more commands you can find yourself. EXPLORE THEM ALL!!!!')

#---------------------------- SYSTEM

if cmdcom == ('/Syscont'):
    print('WARNING: These option supposed for professional users')
    print('1. Create file 2. Delete file 3. Create a window')
    optionchoose = int(input('Enter few options to control quest OS '))

    if optionchoose == 1:
        dem1 = open("demofile.txt", 'x',)
        dem1.write('Hello, world! this is demo file to demonstrate, how funnycmd can control your system!')
        dem1.write(' Hichgc - How i can have good code')
    if optionchoose == 2:
        import os
        if os.path.exists("demofile.txt"):
            os.remove("demofile.txt")
        else:
            print("The file does not exist")
    if optionchoose == 3:
        from tkinter import *
        root = Tk()
        root.title("FCMD")
        root.minsize(200, 200)
        root.geometry("300x300+50+50")
        text = Label(root, text="We going to be functional OS.")
        text.pack()
        text2 = Label(root, text="How about reverse...")
        text2.pack()
        root.mainloop()

#---------------------------- ECHO

if cmdcom == ('/Echo'):
    echoword = input('what de word? ')
    echoamount = int(input('what de amount? '))
    wordresult = echoword * echoamount
    print(wordresult)
    if echoword == 'Speechless':
        print('Speechless? No way! You unlock new command - /Iwannasay!')
    input('Please, press Enter')

#---------------------------- TIME

if cmdcom ==('/Time'):
    from datetime import date 
    todays_date = date.today()
    import time 
    print('Date todate: ', todays_date)
    input('Please, press Enter')
    
#---------------------------- KILL

if cmdcom == ('/Kill'):
    someobject = input('Which object you want to delete?... ')
    if someobject == ('@'):
        while True:
            import time
            time.sleep(0.2)
            print('HOW YOU DARE!? NO!')

    if someobject == ('System32'):
        print('Its not some Windows admin cmd T_T..')
    if someobject == ('Python'):
            import time
            time.sleep(0.1)
            print('Python deleting: 0%')
            time.sleep(0.1)
            print('Python deleting: 2%')
            time.sleep(0.1)
            print('Python deleting: 17%')
            time.sleep(0.1)
            print('Python deleting: 21%')
            time.sleep(0.1)
            print('Python deleting: 29%')
            time.sleep(0.1)
            print('Python deleting: 34%')
            time.sleep(0.2)
            print('Python deleting: 38%')
            time.sleep(0.2)
            print('Python deleting: 42%')
            time.sleep(0.3)
            print('Python deleting: 56%')
            time.sleep(0.3)
            print('Python deleting: 61%')
            time.sleep(0.4)
            print('Python deleting: 70%')
            time.sleep(0.4)
            print('Python deleting: 78%')
            time.sleep(0.5)
            print('Python deleting: 81%')
            time.sleep(0.6)
            print('Python deleting: 97%')
            time.sleep(0.7)
            print('Python deleting: 98%')
            time.sleep(0.8)
            print('Python deleting: 99%')
            time.sleep(0.9)
            print('Python deleting: 100%')
            time.sleep(1.2)
            print('!Python deleted not very succsesful!')
            time.sleep(3)
            while True:
                print('q3089RDO0jsjcwUtjfg0cmw8JSF30')
                time.sleep(0.03)
                print('P08AWREPVUJ9YCP9EALLYYV6UU6PR')
                time.sleep(0.03)
    input('Please, press Enter')

    if someobject == ('funnycmd.py'):
        import time
        time.sleep(1)
        print('Very very smart.')
        time.sleep(2)
        print('But you cant delete me.')
        time.sleep(1)

    if someobject == ('2009'):
        print('2009 - deleted succsesful!')
    input('Please, press Enter')

#---------------------------- RUN

if cmdcom == ('/Run_sentenrator'):
    
    print('Welcome to sentenrator!')
    print('This program can create sentences by three prompts!')
    firstw = input('Enter first word.. ')
    seconw = input('Enter second word... ')
    thirdw = input('Enter third word.... ')
    senresult = firstw + " " + seconw + " " + thirdw
    
    print(senresult)
    if senresult == ('I am steve'):
        import time
        time.sleep(2)
        print('steve')
        time.sleep(2)
        print('steve')
        time.sleep(1)
        print('wait, what?')
        time.sleep(0.7)
        while True:
            print('STEVE')
    if senresult == ('How about reverse'):
        print('You unlock new command - /Rev!')

    print('Your sentence!!!')
    input('Please, press Enter')

if cmdcom == ('/Run_pythoner'):
    
    print('I pythoner, watch at me how i can waveing!')
    import time
    time.sleep(0.8)
    while True:
        import time
        time.sleep(0.08)
        print(' ' + ' ' + '@')
        time.sleep(0.09)
        print(' ' + '@' + ' ')
        time.sleep(0.1)
        print('@' + ' ' + ' ')
        time.sleep(0.09)
        print(' ' + '@' + ' ')
input('Please, press Enter')

#----------------------------- CALC

if cmdcom == ('/Calc'):
    try:
        one = int(input('Enter first number '))
        two = int(input('Enter second number '))
        calcresult = one + two 
        print(calcresult)
        if calcresult == 666:
            while True: 
                import time
                time.sleep(0.07)
                print('IM DEMON')
        if calcresult == 1985:
            print('You unlock new command - /Draw!')
        if calcresult == 2009:
            print('Try to say my birthday!')
    except (ValueError):
        print('ERROR DETECTED! reason:')
        print('Only numbers, bro, try again! (ValueError)')
    input('Please, press Enter')

#----------------------------- DRAW

if cmdcom == ('/Draw'):
    print('What do u wanna draw?')

    drawchoose = input('Wait for input... ')
    if drawchoose == 'Wavetube':
         while True:
             import time
             print(' ' + ' ' + ' ' + ' ' + '8')
             time.sleep(0.1)
             print(' ' + '.' + '8' + 'o' + ' ')
             time.sleep(0.1)
             print('8' + ' ' + ' ' + '.' + ' ')
             time.sleep(0.1)
             print(' ' + 'o' + '8' + ' ' + ' ')
             time.sleep(0.1)
             print(' ' + ' ' + '[]' + ' ' + ' ')

    if drawchoose == 'GETall':
        import time
        time.sleep(0.6)
        print(' ' + ' ' + ' ' + ' ' + ' ')
        time.sleep(0.6)
        print(' ' + '0' + ' ' + '0' + ' ')
        time.sleep(0.6)
        print(' ' + ' ' + 'o' + ' ' + ' ')
        time.sleep(0.6)
        print('*' + ' ' + ' ' + ' ' + '*')
        time.sleep(0.6)
        print(' ' + '*' + '*' + '*' + ' ')
        time.sleep(0.6)
        print(' ' + ' ' + ' ' + ' ' + ' ')
        time.sleep(0.6)
        print('N' + 'O' + ' W' + 'A' + 'Y')
        time.sleep(0.6)
        print('Draw complete!')

    if drawchoose == 'Python':
        import time
        time.sleep(0.6)
        print('  ___')
        time.sleep(0.6)
        print('  | |')
        time.sleep(0.6)
        print('   | |')
        time.sleep(0.6)
        print('    | |')
        time.sleep(0.6)
        print('   | |')
        time.sleep(0.6)
        print('  | |')
        time.sleep(0.6)
        print('   | |')
        time.sleep(0.5)
        print('  | |')
        time.sleep(0.5)
        print('  ---')
        time.sleep(0.5)
        print(' |   | ')
        time.sleep(0.4)
        print('| . . |')
        time.sleep(0.4)
        print('-_____-')
        time.sleep(0.3)
        print('   ||')
        time.sleep(0.2)
        print('   W ')
        time.sleep(0.1)
        print('Draw complete!')

    if drawchoose == 'C++':
        import time
        time.sleep(0.4)
        print(' ' + ' ' + ' '  + '*' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ')
        time.sleep(0.4)
        print(' ' + '*' + ' '  + ' ' + ' ' + '*' + ' ' + ' ' + '*' + ' ' + ' ' + ' ' + '*' + ' ')
        time.sleep(0.4)
        print(' ' + '*' + ' '  + ' ' + ' ' + ' ' + ' ' + '*' + '*' + '*' + ' ' + '*' + '*' + '*')
        time.sleep(0.4)
        print(' ' + '*' + ' '  + ' ' + ' ' + '*' + ' ' + ' ' + '*' + ' ' + ' ' + ' ' + '*' + ' ')
        time.sleep(0.4)
        print(' ' + ' ' + ' '  + '*' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ' + ' ')
        time.sleep(0.1)
        print('Draw complete!')

    if drawchoose == 'Glider':
        import time
        time.sleep(0.2)
        print(' ' + '0' + ' ')
        time.sleep(0.2)
        print('0' + ' ' + ' ')
        time.sleep(0.2)
        print('0' + '0' + '0')
        time.sleep(0.1)
        print('Draw complete!')
    input('Please, press Enter')
            
#----------------------------- RANDOM

if cmdcom == ('/Rand'):
    import random
    random_number = random.randint(0, 2024)
    print(random_number)

    if random_number == 666:
        while True:
            print('IM DEMON')
    if random_number == 1995:
        import time
        while True:
            time.sleep(0.2)
            print('_-*WINDOWS 95*-_')
            time.sleep(0.2)
            print('--*WINDOWS 95*--')
            time.sleep(0.2)
            print('*-_WINDOWS 95_-*')
    if random_number == 1985:
        print('Microsoft Windows')
    if random_number == 1111:
        print('You unlock new command - /Countto!')
    if random_number == 1:
        print('You lucky!')
    input('Please, press Enter')

if cmdcom == ('/Randname'):
        import string 
        import random 
        stLogin = random.sample((string.ascii_lowercase), 6)
        
        Login = ''.join(stLogin)
        
        if Login == ('stalin'):
            while True:
                print('HOW!?!?!?')
        
        print(f'Name: {Login}')
        input('Please, press Enter')

#----------------------------- REV

if cmdcom == ('/Rev'):
    reverse = input('Wait for input... ')
    for revword in reverse[ : : -1]:
        print(revword)
    input('Please, press Enter')

#----------------------------- COUNTER

if cmdcom == ('/Countto'):
    try:
        numtto = int(input('Count from?.. '))
        numtto2 = int(input('Count to?.. '))
        
        while numtto < numtto2 + 1:
            import time
            time.sleep(0.03)
            print(numtto)
            numtto += 1
            
            if numtto == 666 or numtto2 == 666:
                while True:
                    print('IM DEMON')
            if numtto == 42 or numtto2 == 42:
                print('Right answer!')
            if numtto == 1985 or numtto2 == 1985:
                print('Microsoft Windows')
    except ValueError:
        print('ERROR DETECTED! reason:')
        print('Only numbers, bro, try again! (ValueError)')
    input('Please, press Enter')

#----------------------------- SAY

if cmdcom ==('/Iwannasay'):
    print('What do u wanna say?')
    
    saidword = input('Wait for input... ')
    if saidword == 'Emojies':
        import time
        print(':)')
        time.sleep(0.1)
        print(':(')
        time.sleep(0.1)
        print(':0')
        time.sleep(0.1)
        print(':D')
        time.sleep(0.1)
        print('XD')
    
    if saidword == 'C++' or saidword == "C#" or saidword == 'C':
        print('Ha-Ha-Ha. Very funny')
    if saidword == '404':
        print('Page not found')
    if saidword == '1985':
        print('Microsoft')
    if saidword == '2009':
        print('You unlock new command - /Kill!')
    if saidword == 'Windows_XP':
        print('Can you remember something more old?')
    if saidword == 'Windows_Me':
        print('I said MORE old')
    if saidword == 'Windows_95':
        print('Yep, its very old.')

    if saidword == 'Hichgc':
        import time
        time.sleep(1.4)
        print('Analyzing..')
        time.sleep(1.9)
        print('Analyzing..(x2)')
        time.sleep(2)
        print('Analyzing..(x3)')
        time.sleep(1.5)
        print('!NOHOW!')
        time.sleep(1.3)
        while True:
            time.sleep(0.04)
            print('ValueError: invalid literal for int() with base 10: t')
    if saidword == "@-usless":
        print('@: Ya just toxic, man, go drink coffee and calm down ')
    if saidword == 'Iwannagetallcommands!':
        print('Dream more!!!')
    input('Please, press Enter')
            
#----------------------------- END

if cmdcom == ('/Bye'):
    print('Maded by CD-ROMsoft Inc. V.PREalpha.0.0.8 AeroBingo+ (NOW IN GIT-HUB)')

else:
    print('!Wrong command!')
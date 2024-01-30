
answers = []

def answer_eggs_and_bacon():
        print("====================================================")
        print("How would you like your eggs?")
        a ="Scrambled"
        b ="Medium rare"
        c = "Hard"
        question_a =input(f" a - {a} \n b - {b} \n c - {c} \n")
        if question_a =="a":
            print(f"You got it, {a} it is!")
            answers.append(a)
        elif question_a == "b":
            print(f"You got it, {b} it is!")
            answers.append(b)
        else:
            question_a == "c"
            print(f"You got it, {c} it is!")
            answers.append(c)

def answer_oatmeal():
    print("====================================================")
    question_b = input("Would you like cinnamon? \n")
    yes = "with Cinnamon"
    if question_b == "yes" or question_b == "Yes":
        print("Alright, here's some cinnamon")
        answers.append(yes)
    elif question_b == "no" or  question_b == "No":
        print("No problem!")
    else: 
        quit()


def answer_cereal():
    print("====================================================")
    a = "Fruit Loops"
    b = "Lucky Charms"
    print("Which one do you prefer?")
    question_c = input(f" a - {a} \n b - {b}\n")
    if question_c == "a" or question_c == "A":
        answers.append(a)
        print("That one does not have marshmallow")
    elif question_c == "b" or question_c =="B":
        answers.append(b)
        print("Marshmallow are the best")
    else:
        print("+++=================================================+++")
        print("Sorry those are the only ones that we have for now")
        answer_cereal()
        
def drink():
    print("What do you want to drink?")
    a = "Orange Juice"
    b = "Milk"
    c = "Water"
    d = "Coffee"
    e = "Matcha"
    drink_question = input(f" a - {a}\n b - {b} \n c - {c} \n d - {d} \n e - {e} \n")
    if drink_question == "a":
        answers.append(a)
        print("Here's some OJ")
    elif drink_question == "b":
        answers.append(b)
        milk_question = input("You want chocolate with it? \n")
        with_chocolate = "with Chocolate"
        if milk_question == "yes":
            answers.append(with_chocolate)
        else:
            None
        print("Perfect!")
    elif drink_question == "c":
        answers.append(c)
        a = "Tap water"
        b = "Bottle of water"
        water_question = input(f" a - {a} \n b - {b} \n")
        if water_question == "a":
            answers.append(a)
            print("You got it!")
        elif water_question == "b":
            answers.append(b)
        else:
            None
    elif drink_question == "d":
        answers.append(d)
        a = "with sugar and Milk"
        b = "with just sugar"
        c = "with just milk"
        coffee_question = input(f" a - {a} \n b - {b} \n c - {c} \n")
        if coffee_question == "a":
            answers.append(a)
        elif coffee_question =="b":
            answers.append(b)
        elif coffee_question == "c":
            answers.append(c)
        else:
            None
        print("Coming right up!")
    elif drink_question == "e":
        answers.append(e)
        hot_latte = "Hot latte"
        iced_latte = "Iced Latte"
        matcha_question = input(f" a - {hot_latte} \n b - {iced_latte} \n")
        if matcha_question == "a":
            answers.append(hot_latte)
        elif matcha_question == "b":
            answers.append(iced_latte)
        else:
            None
        oat_milk = " with Oat milk"
        almond_milk = " with Almond Milk"
        regular_milk = " with Regular Milk"
        matcha_milk_question = input(f" a - {oat_milk} \n b - {almond_milk} \n c - {regular_milk} \n")
        if matcha_milk_question == "a":
            answers.append(oat_milk)
        elif matcha_milk_question == "b":
            answers.append(almond_milk)
        elif matcha_milk_question == "c":
            answers.append(regular_milk)
        else:
            None
    else:
        print("No drink? no problem!")
        


def init():
    
    print("====================================================")
    name = input("=========== Good morning ========== \n Welcome! \n Name for the order? \n")
    question_init = print(" What are you eating this morning?")
    a = "Eggs and bacon"
    b = "Oatmeal"
    c = "Cereal"
    first_question = input(f" a - {a} \n b - {b} \n c - {c} \n")
    if first_question == "a":
        answers.append(a)
        answer_eggs_and_bacon()
            
    elif first_question == "b":
        answers.append(b)
        answer_oatmeal()
    elif first_question == "c":
        answers.append(c)
        answer_cereal()
    else:
        print("That's the menu for today, we apologize")
        init()
    drink()
    print(f" Here's your order {name}: \n {answers}")
    
init()
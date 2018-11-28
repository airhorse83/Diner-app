# build out an interactive experience with repl.it
#start with waitress greeting which may require input, hello-- hello welcome to the diner here is our menu....
#show menu options and prices..specifically show the entree option only
#user then selects the food and the waitress responds to the selection "great choice!" etc
# return the price of the selection
# then the waitress repeats the process for the sides, dont mention the entree
# give total cost of meal
total = []

main_course = {
  "surf": 9,
  "turf": 9
}

sides = {
  "corn": 3,
  "potatoes": 5
}

def greeting():
    print("Hey ya'll, welcome to the Bottega diner! Would you like to see the menu?")
    answer = input().lower()
    if answer == "Yes" or answer == "yes":
      print(" The special of the night is surf or turf! 10 oz. filet or an 8 oz. lobster tail with your choice of a side.")
      print("For your side we offer corn or potatoes au gratin.")
      user_choice()
    elif answer == "no" or answer == "no":
      print("then why the hell did you come into our diner?!") 
    else:
      print('im sorry i dont undertand. please try again')
      greeting()  
 

def user_choice():
    print("which meal would you like, Surf or Turf?")
    answer_one = input().lower()

    if answer_one == "Surf" or answer_one == "surf":
      print(f"Great choice! The lobster costs ${main_course[answer_one]}.")
      total.append(main_course[answer_one])
      user_choice_sides()
    elif answer_one == "Turf" or answer_one == "turf":
      print(f"Great choice! The steak costs ${main_course[answer_one]}.")
      total.append(main_course[answer_one])
      user_choice_sides()
    else:
      print('im sorry i dont undertand. please try again')
      user_choice()
    
    

def user_choice_sides():
    print("Would you like corn or potatoes?")
    answer_side = input().lower()
    
    if answer_side == "corn" or answer_side == "Corn":
      print(f"Great choice! The tasty corn costs ${sides[answer_side]}.")
      total.append(sides[answer_side])
      checkout()
    elif answer_side == "Potatoes" or answer_side == "potatoes":
      print(f"Great choice! They are my favorite! The potatoes costs ${sides[answer_side]}.")
      total.append(sides[answer_side])
      checkout()
    else:
      print('im sorry i dont undertand. please try again') 
      user_choice_sides()
      
def checkout():
  print(f'thanks for coming in, your total for the night is ${sum(total)}.  Come back and see us again!') 
  payment()   

def payment():
  print("will you be paying for you meal?")
  answer_pay = input().lower()

  if answer_pay == "yes" or answer_pay == "Yes":
    print("thanks for the tip, have a great night!")
  elif answer_pay == "no" or answer_pay == "No":
    print("OK dirtbag, you are sitting here till the cops come and deal with you!") 
  else:
    print("I didnt catch that...")
    payment() 

        
greeting()    

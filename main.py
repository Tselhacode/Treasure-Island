print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 

#https://www.draw.io/?lightbox=1&highlight=0000ff&edit=_blank&layers=1&nav=1&title=Treasure%20Island%20Conditional.drawio#Uhttps%3A%2F%2Fdrive.google.com%2Fuc%3Fid%3D1oDe4ehjWZipYRsVfeAx2HyB7LCQ8_Fvi%26export%3Ddownload

left_right = input("What is going to be your first step? Left or Right\n").lower()
if left_right == "left":
  swim_wait = input("Great! Left it is! Now, you reached a lake. Do you want to wait for a raft or swim instead to the bank? Swim or Wait\n").lower()
  if swim_wait == "wait":
    red_blue_yellow = input("The raft luckily arrived soon and quickly took you to the bank. Now you are at the steps of three huge doors. The first one is red in color. The second one is blue in color. Finally, the last one is yellow in color. Which one will you pick? Red or Blue or Yellow?\n").lower()
    if red_blue_yellow == "yellow":
      print("Congratulations! You win! You are a millionaire!")
    elif red_blue_yellow == "blue":
      print("Wrong door! You are eaten by a famished beast.Game Over!")
    elif red_blue_yellow == "red":
      print("Sorry to see you burn! This is the room on fire! Game Over!")
    else:
      print("Game Over!")
  else: 
      print("You have been attacked by a gianormous Trout.Game Over!")
else:
  print("Shoot! You fell into a hole! Game Over!")

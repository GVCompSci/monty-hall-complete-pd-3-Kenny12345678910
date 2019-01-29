from random import randint
rounds= int(input("How many rounds would you like to simulate?"))
guess= int(input("What door number is your guess?"))
print("You chose door:#",guess,"!")
contPlay = 1
right = 0
wrong = 0
switch= input("would you like to switch doors?")
while contPlay <= rounds:
  car = randint(1, 4)
  if switch == "Yes" or "yes":
    if guess== 1 and car==2:
      print("The car was not behind door number 1")
      right +=1
      contPlay+=1
    if guess== 2 and car==3:
      print("The car was not behind door number 2")
      right +=1
      contPlay+=1
    if guess==3 and car==1:
      print("The car was not behind door number 3")
      right +=1
      contPlay+=1
    if guess==3  and car==2:
      print("The car was not behind door number 3")
      right +=1
      contPlay+=1
    if guess== 2 and car== 1:
      print("The car was not behind door number 2")
      right +=1
      contPlay+=1
    if guess== 1 and car== 3:
      print("The car was not behind door number 1")
      right +=1
      contPlay+=1
    if guess == car:
      print("The car was behind your door")
      wrong+=1
  if switch == "No" or "no":
    if guess== 1 and car==2:
      print("The car is not behind door number 3")
      wrong+=1
      contPlay+=1
    if guess== 2 and car==3:
      print("The car is not behind door number 1")
      wrong+=1
      contPlay+=1
    if guess==3 and car==1:
      print("The car is not behind door number 2")
      wrong+=1
      contPlay+=1
    if guess==3  and car==2:
      print("The car is not behind door number 1")
      wrong+=1
      contPlay+=1
    if guess== 2 and car== 1:
      print("The car is not behind door number 3")
      wrong+=1
      contPlay+=1
    if guess== 1 and car== 3:
      print("The car is not behind door number 2")
      wrong+=1
      contPlay+=1
    if guess == car:
      right+=1
      print("The car was behind your door")

print("You got",right,"Right and",wrong,"wrong")
percent= right/rounds * 100
print("You got",percent,"% correct")

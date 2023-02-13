print(" Welcome to my computer quiz ")

Conformation = input(" Are sure you want to play my quiz ? - ")

if (Conformation.lower() == "yes"):
    print(" Let's start the game ")
else:
    quit()

Score = 0

Question1 = int(input(" How many states are there in India ? - "))
if (Question1 == 28):
    print(" Your answre is correct ! ")
    Score += 1
else:
    print(" Sorry your answe is wrong ")

Question2 = input(" What is the universal language ? - ")
if (Question2.lower() == "english"):
    print(" Your answre is correct ! ")
    Score += 1
else:
    print(" Sorry your answe is wrong ")

Question3 = int(input(" Which year did India got indipendent ? - "))
if (Question3 == 1947):
    print(" Your answre is correct ! ")
    Score += 1
else:
    print(" Sorry your answe is wrong ")

Question4 = input(" Selam is special for ? - ")
if (Question4.lower() == "mango"):
    print(" Your answre is correct ! ")
    Score += 1
else:
    print(" Sorry your answe is wrong ")

Question5 = int(input("How many districts are there in Tamil Nadu ? - "))
if (Question5 == 32):
    print(" Your answre is correct ! ")
    Score += 1
else:
    print(" Sorry your answe is wrong ")

print("You got ", Score, "out of 5 ")

Percentage = (Score / 5) * 100
print("Your Percentage is : ", Percentage, "%")

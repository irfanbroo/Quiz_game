print("Welcome to my Quizz ")
score = 0
playing = input("You want to play a cool game? ")

if playing.lower() !="yes":
    quit()
answer =  input(("which country is the best in the world? "))
if answer.lower() == "north korea":
    print("You may Live for the next ROUND")
    score +=1
else:
    print("incorrect")
answer = input("who is your supreme commander and leader: ")
if answer.lower()=="kim jon un":
    print("Great")
    score +=1
else:
    print("Your execution will be in 10 minutes....")
print('You have answered  ' + str(score ) + 'right')

extra = score
playing = input("You wish to continue again?: ")
if playing.lower()!= "yes":
    print("ok bye")
    quit()
answer = input("capital of North Korea?: ")
if answer.lower()=="pyongyang":
    print("corect")
    extra +=1
else:
    print("bye from this world ")

print("Total Score as of now is: " + str(extra))    
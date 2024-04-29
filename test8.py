# answer = 8
# guess = int(input("Enter your guess (1-10) : "))
# if guess > answer: 
#     print("wrong guess. try smaller one")
# elif guess < answer:
#     print("wrong guess. try bigger one")
# elif guess == answer:
#     print("Bingo!")

answer = input("""
Enter Weather (sunny, rainy, windy)
""")
if answer == "sunny":
    print("it's sunny let's go for a walk")
elif answer == "rainy":
    print("its rainy that's my fav weather")
elif answer == "windy":
    print("Nya ka Man U ma shone loh")
else:
    print("enter(sunny,rainy,windy) Only Please")

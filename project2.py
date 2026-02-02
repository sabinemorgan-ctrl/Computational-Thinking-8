winter_points = 0
summer_points = 0
spring_points = 0

answer1 = input ("Do you prefer A short sleeves, B long sleeves, or C both?  ")
if answer1 == "A":
    summer_points += 1
elif answer1 == "B":
    winter_points += 1 
elif answer1 == "C":
    spring_points += 1

answer2 = input ("Is your favorite weather A rainy, B snowy, or C sunny?  ")
if answer2 == "A":
    spring_points += 1
    winter_points += 1
elif answer2 == "B":
    winter_points += 2
elif answer2 == "C":
    summer_points += 2

answer3 = input ("Would you rather A snowboard, B ski, or C swim?  ")
if answer3 == "A" or answer3 == "B":
    winter_points += 2
elif answer3 == "C":
    summer_points += 1
    spring_points += 1
    
answer4 = input ("Would you rather A hot chocolate, B iced drink, or C both?  ")
if answer4 == "A" or answer4 == "B":
    winter_points += 2
elif answer3 == "C":
    summer_points += 1
    spring_points += 1

answer5 = input ("Would you rather A travel, B stay in, or C both?  ")
if answer5 == "A" or answer5 == "B":
    winter_points += 2
    
elif answer3 == "C":
    summer_points += 1
    spring_points += 1
         
print (f" You score is {winter_points} winter, {summer_points} summer, and {spring_points} spring")
 
 # End: determine results 
if summer_points > winter_points: 
    print("You are a summer person")
elif winter_points > summer_points: 
    print("you are a winter person")
elif spring_points > summer_points: 
    print("you are a summer person")
elif summer_points == winter_points:
    print("you like all seasons the same")
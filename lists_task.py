
# trainees = ["John", [2, ["James","Mary"]]]
# 1. Display 2 from the list.
# 2. Output James  from the list.
# 3. Using a method add 56 at the end of the list.
# 4. Using a method add the name Mike between James and Mary
# 5. Change the value of 2 to 8
# 6. Remove John and Mary from the list.
# 7. Using a function, determine the length of the list
# Attempt questions in the link below. Whether you get the right answer or not, still read the solution explanation.
# https://realpython.com/quizzes/python-lists-tuples/viewer/

trainees=["John",[2,["James","Mary"]]] 
print(trainees[1][0])
print(trainees[1][1][0])
trainees.append(56)
print(trainees)
trainees[1][1].insert(1,"Mike")
print(trainees)
trainees[1][0]=8
print(trainees)
trainees.remove("John")
print(trainees)
# trainees[0][1].remove("Mary")
trainees[0][1].pop()
print(trainees)
trainees=len(trainees)
print(trainees)
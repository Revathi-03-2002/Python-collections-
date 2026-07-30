#1.Create a list of five fruits and print it.
# fruits=["apple","banana","mango","cherry","pinapple"]
# print(fruits)
#2. Add a new color to the set.
fruits=["apple","banana","mango","cherry","pinapple"]
fruits.append("guva")
print(fruits)
#3.Insert a fruit at the second position. 
fruits.insert(1,"kiwi")
print(fruits)
#4.remove a fruites by its name
fruits.remove("mango")
print(fruits)
#5.print the frist and last elements
print ("frist:",fruits[0])
print("last:",fruits[-1])
#6.find the length the list
print("length:",len(fruits))
#7.sort the list in alphabetical order
fruits.sort()
print (fruits)
#8.reverse the list
fruits.reverse()
print (fruits)
#9.count howmany times a specific number appears in a list
numbers=[10,20,30,10,40,10]
print("count of 10:",numbers .count(10))
#10.find the largest and smallest numbers in the list
print("largest:",max(numbers))
print("smallest:",min(numbers))


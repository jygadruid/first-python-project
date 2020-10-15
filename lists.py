# names = ["jenny" , "alexus"]
# print(names[0] + " " + names[1])

# names_height = [["jenny", 67], ["alexus", 70]]
# print(names_height[0][1])
# print(names_height[0][0] + " is " + str(names_height[0][1]))

# names = ["jenny", "alexus", "sam"] #zip() only includes matching items
# heights = [67, 70]

# names_heights = list(zip(names, heights))
# print(list(names_heights))

#tuples: (x, y) cannot be changed
#lists: [x, y]

# print(names_heights[0][0])

# li = []
# print("Before adding \"sam\": ", li)
# li.append("sam")
# print("After adding \"sam\": ", li)


#range(x)
#start: 0
#stop: 10
#step: 1
new_range = list(range(11))
print(new_range)

#range(x)
#start: 0
#stop: 21
#step: 1
even_range = list(range(0,21,1))
print(even_range)

#range(x)
#start: 0
#stop: 5
#step: 1
zero_to_five = list(range(0,6))
print(zero_to_five)
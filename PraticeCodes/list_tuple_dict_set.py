# marks = [100, 90, 20, 80]
# print(marks.count(90))
# marks.extend([120, 200, 34])
# print(marks)

# # print(Counter(marks))
# marks.reverse()

# marks.sort()
# print(marks)

# marks = marks[::-1]
# print(marks)

# Shallow Copy
# list1 = [10, 20, 40, 90]
# list2 = list1

# list1[1] = 100

# print(list1)
# print(list2)


# tup = (10, "2", 3.5)
# print(tup)

# ls = [20, [22, 23], (32,33, 44), "ash", 2.3, 'a']
# print(ls[1:])


# employee = {"emp1": "ashwin",
#             "emp2": "akhilesh",
#             "emp3": "aravind",
#             "emp4": "ram",
#             "emp5": "vignesh",
#             }

# print(employee) #{'emp1': 'ashwin', 'emp2': 'akhilesh', 'emp3': 'aravind', 'emp4': 'ram', 'emp5': 'vignesh'}
# print(employee.items()) #dict_items([('emp1', 'ashwin'), ('emp2', 'akhilesh'), ('emp3', 'aravind'), ('emp4', 'ram'), ('emp5', 'vignesh')])
# print(employee.keys()) #dict_keys(['emp1', 'emp2', 'emp3', 'emp4', 'emp5'])
# print(employee.values()) #dict_values(['ashwin', 'akhilesh', 'aravind', 'ram', 'vignesh'])

# employee.update({"emp4": "GGG"}) #{'emp1': 'ashwin', 'emp2': 'akhilesh', 'emp3': 'aravind', 'emp4': 'GGG', 'emp5': 'vignesh'}
# employee.pop("emp4") #{'emp1': 'ashwin', 'emp2': 'akhilesh', 'emp3': 'aravind', 'emp5': 'vignesh'}
# employee.popitem() #{'emp1': 'ashwin', 'emp2': 'akhilesh', 'emp3': 'aravind'} -- Pops the last item




# Set operations
set_a = {3, 4, 5, 6, 1,12 }
set_a.add(15) #{3, 4, 5, 6, 1,12, 15 }
set_a.remove(12) #{3, 4, 5, 6, 15}


mark1 = {88, 90, 98, 32, 33}
mark2 = {50, 70, 87, 33, 90}

markU = mark1.union(mark2)  # Or --> markU = mark1 | mark2
print(markU)

markI = mark1.intersection(mark2) # Or --> markI = mark1 & mark2
print(markI)

diff = mark1 - mark2
print(mark1)

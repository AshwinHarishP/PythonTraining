#--KeywordArgument Funcitons

#1) Function with args(keyword)
print("------------ Function with args(keyword) ------------")
def disp(*args):
    print(args)

disp(1, 2, 3)


#-2) Funtion with multiple keword args
print("------------ Funtion with multiple keword args ------------")
def display_kwags(**args):
    print(args)

display_kwags(id=1, name="Ashwin", addr="Pn_palayam")
display_kwags(id=2, name="Aravinf", addr="Pn_palayam", phone=8754018099)

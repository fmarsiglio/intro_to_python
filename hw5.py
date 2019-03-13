#Load the data from a file
row_0 = ["Clean House", "low"]
row_1 = ["Pay Bills", "high"]
dict_0 = {"Task": "Clean House", "Priority": "low"}
dict_1 = {"Task": "Pay Bills", "Priority": "high"}
table_0 = [dict_0, dict_1]

#display a menu of choices to the user
while(True):
    print("Menu of Options: \n"
      "1) Show current data. \n"
      "2) Add a new item. \n"
      "3) Remove an existing item. \n"
      "4) Save Data to File. \n"
      "5) Exit Program.")
    print()
    strChoice = str(input("Which option would you like to perform? [1 to 5]: "))
    print()
#show the current items in the table
    if(strChoice.strip() == '1'):
        for x in table_0:
            print(x)
        print() #added a line
        continue
#add a new item to the list/table
    elif(strChoice.strip() == '2'):
        task_0 = input("What is another task you need to do?: ")
        priority_0 = input(("How high of a priority is it? [high or low]: "))
        dict_2 = {"Task": task_0, "Priority": priority_0}
        table_0.append(dict_2)
        print()
        continue
#remove a new item to the list/table
    elif(strChoice.strip() == '3'):
        table_0.pop()
        print()
        continue
#save tasks to the Todo.txt file
    elif(strChoice.strip() == '4'):
        ToDo_list = open("/Users/frankmarsiglio/PycharmProjects/intro_to_python/Todo.txt", "w")
        ToDo_list.write(str(table_0))
        ToDo_list.close()
#exit the program but save the data from the list/table when the program exits
    elif(strChoice.strip() == '5'):
        ToDo_list = open("/Users/frankmarsiglio/PycharmProjects/intro_to_python/Todo.txt", "w")
        ToDo_list.write(str(table_0))
        ToDo_list.close()
        break
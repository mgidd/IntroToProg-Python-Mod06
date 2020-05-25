# ---------------------------------------------------------------------------- #
# Title: Assignment 06
# Description: Working with functions in a class,
#              When the program starts, load each "row" of data
#              in "ToDoToDoList.txt" into a python Dictionary.
#              Add each dictionary "row" to a python list "table"
# ChangeLog (Who,When,What):
# RRoot,1.1.2030,Created started script
# RRoot,1.1.2030,Added code to complete assignment 5
# MGidd,5.21.2020,Modified code to write data to file
# MGidd,5.24.2020,Modified code to add and remove list data
# MGidd,5.25.2020,Modified code to separate input and processing tasks
# ---------------------------------------------------------------------------- #

# Data ---------------------------------------------------------------------- #
# Declare variables and constants
strFileName = "ToDoFile.txt"  # The name of the data file
objFile = None   # An object that represents a file
dicRow = {}  # A row of data separated into elements of a dictionary {Task,Priority}
lstTable = []  # A list that acts as a 'table' of rows
strChoice = ""  # Captures the user option selection
strTask = ""  # Captures the user task data
strPriority = ""  # Captures the user priority data
strStatus = ""  # Captures the status of processing functions

# Processing  --------------------------------------------------------------- #

class Processor:
    """  Performs Processing tasks """

    @staticmethod
    def read_data_from_file(file_name, list_of_rows):
        """ Reads data from a file into a list of dictionary rows

        :param file_name: (string) with name of file:
        :param list_of_rows: (list) you want filled with file data:
        :return: (list) of dictionary rows
        """
        list_of_rows.clear()  # clear current data
        file = open(file_name, "r")
        for line in file:
            task, priority = line.split(",")
            row = {"Task": task.strip(), "Priority": priority.strip()}
            list_of_rows.append(row)
        file.close()
        return list_of_rows, 'Success'

    @staticmethod
    def add_data_to_list(new_task, new_priority, list_of_rows):
        # Code added to complete assignment 6
        """ Adds data to a list of dictionary rows

        :param new_task: argument to add to list
        :param new_priority: argument to add to list
        :param list_of_rows: (list) you want to add data to:
        :return: (list) of dictionary rows
        """
        row = {"Task": new_task.strip(), "Priority": new_priority.strip()}  # Assign to dictionary 'row'
        list_of_rows.append(row)  # Add row to list(table)
        return list_of_rows, 'Success'  # Return updated list

    @staticmethod
    def remove_data_from_list(remove_task, list_of_rows):
        # Code added to complete assignment 6
        """ Removes data from a list of dictionary rows

        :param remove_task: argument to remove
        :param list_of_rows: (list) you want to remove data from:
        :return: (list) of dictionary rows
        """
        for row in list_of_rows:
            if row["Task"].lower() == remove_task.lower():
                list_of_rows.remove(row)  # Remove row from list(table)
        return list_of_rows, 'Success'  # Return updated list

    @staticmethod
    def write_data_to_file(file_name, list_of_rows):
        # Code added to complete assignment 6
        """ Writes data (as a list of dictionary rows) to a file

        :param file_name: object representing file you want to write to
        :param list_of_rows: (list) of data you want written to file
        :return: (list) of dictionary rows
        """
        file = open(file_name, 'w')
        for row in list_of_rows:
            file.write(str(row["Task"]) + "," + str(row["Priority"]) + "\n")  # Write data to file
        file.close()
        return list_of_rows, 'Success'


# Presentation (Input/Output)  -------------------------------------------- #

class IO:
    """ Performs Input and Output tasks """

    @staticmethod
    def print_menu_tasks():
        """  Display a menu of choices to the user

        :return: nothing
        """
        print('''
        Menu of Options
        1) Add a new Task
        2) Remove an existing Task
        3) Save Data to File        
        4) Reload Data from File
        5) Exit Program
        ''')
        print()  # Add an extra line for looks

    @staticmethod
    def input_menu_choice():
        """ Gets the menu choice from a user

        :return: string
        """
        choice = str(input("Which option would you like to perform? [1 to 5] - ")).strip()
        print()  # Add an extra line for looks
        return choice

    @staticmethod
    def print_current_tasks_in_list(list_of_rows):
        """ Shows the current Tasks in the list of dictionaries rows

        :param list_of_rows: (list) of rows you want to display
        :return: nothing
        """
        print("******* The current Tasks ToDo are: *******")
        for row in list_of_rows:
            print(row["Task"] + " (" + row["Priority"] + ")")
        print("*******************************************")
        print()  # Add an extra line for looks

    @staticmethod
    def input_yes_no_choice(message):
        """ Gets a yes or no choice from the user

        :return: string
        """
        return str(input(message)).strip().lower()

    @staticmethod
    def input_press_to_continue(optional_message=''):
        """ Pause program and show a message before continuing

        :param optional_message:  An optional message you want to display
        :return: nothing
        """
        print(optional_message)
        input('Press the [Enter] key to continue.' + '\n')

    @staticmethod
    def input_new_task_and_priority():
        # Code added to complete assignment 6
        """ Gets input from the user for a new task and priority

        :return: (strings) task and priority
        """
        global strTask
        global strPriority
        print("Enter a task and the level of priority.")
        strTask = input("Task: ")
        strPriority = input("Priority: ")
        return strTask, strPriority  # Return task, priority

    @staticmethod
    def input_task_to_remove():
        # Code added to complete assignment 6
        """ Gets input from the user for a task to remove

        :return: (string) task to be removed
        """
        global strTask
        strTask = input("Task to remove: ")
        return strTask  # Return task


# Main Body of Script  ------------------------------------------------------ #

# Step 1 - When the program starts, Load data from ToDoFile.txt.

Processor.read_data_from_file(strFileName, lstTable)  # read file data

# Step 2 - Display a menu of choices to the user
while(True):
    # Step 3 Show current data
    IO.print_current_tasks_in_list(lstTable)  # Show current data in the list/table
    IO.print_menu_tasks()  # Shows menu
    strChoice = IO.input_menu_choice()  # Get menu option
    
    # Step 4 - Process user's menu choice
    if strChoice.strip() == '1':  # Add a new Task
        # Code added to complete assignment 6
        IO.input_new_task_and_priority()  # Gets input from user
        Processor.add_data_to_list(strTask, strPriority, lstTable)  # Adds data to list
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '2':  # Remove an existing Task
        # Code added to complete assignment 6
        IO.input_task_to_remove()  # Gets input from user
        Processor.remove_data_from_list(strTask, lstTable)  # Removes data from list
        IO.input_press_to_continue(strStatus)
        continue  # to show the menu

    elif strChoice == '3':   # Save Data to File
        strChoice = IO.input_yes_no_choice("Save this data to file? (y/n) - ")
        if strChoice.lower() == "y":
            # Code added to complete assignment 6
            Processor.write_data_to_file(strFileName, lstTable)  # Writes data to file
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("Save Cancelled!")
        continue  # to show the menu

    elif strChoice == '4':  # Reload Data from File
        print("Warning: Unsaved Data Will Be Lost!")
        strChoice = IO.input_yes_no_choice("Are you sure you want to reload data from file? (y/n) -  ")
        if strChoice.lower() == 'y':
            # Code added to complete assignment 6
            Processor.read_data_from_file(strFileName, lstTable)  # Reads(loads) data from file
            IO.input_press_to_continue(strStatus)
        else:
            IO.input_press_to_continue("File Reload Cancelled!")
        continue  # to show the menu

    elif strChoice == '5':  # Exit Program
        print("Goodbye!")
        break   # and Exit

#=====importing libraries===========
import datetime
# from tabulate import tabulate
today = datetime.datetime.now()

    
def read_user_file():
    #   CREATE NEW DICTIONARY FOR USER.TXT
    user_dict = {}
    with open('user.txt', 'r+') as file_user:
        for line in file_user:
            l = line.strip('\n').split(",")
            user_dict[l[0].strip()]=l[1].strip() 
    return user_dict


def read_task_file():
    #   CREATE NEW LIST OF LIST FOR TASKS.TXT
    tasks_list = []
    with open('tasks.txt', 'r+') as file_tasks:
        for line in file_tasks:
            l_tidy = line.strip('\n').split(",")
            tasks_list.append([l.strip() for l in l_tidy])
    return tasks_list


def login(user_dict):
    #   ====LOGIN Section====
    #   Ask user to input Username, check if username is in up_dict (user:password dictionary)
        # If username not in user_dict, show error and ask for username again
        # If username is valid and in user_dict, prompt input for password
        # If password is not in user_dict dictionary, show error, ask for password again
    username = input("Enter your username: \n")
    while username not in user_dict:
        print("Username is not found! Please try again. \n")
        username = input("Enter your username: \n")
        
    password = input("Enter your password: \n")
    while password != user_dict[username]:
        print("Invalid Password! Please try again. \n")
        password = input("Enter your password: \n")
    return username

def register_user(user_dict):
    if username == "admin":    
        n_user = input("Enter a new username: \n")
        while n_user in user_dict:
            n_user = input("User exists. Enter a new username: \n")
    
# Ask user input new password
    n_pwd = input("Enter a new password: \n")
    
# Ask user input password confirmation, check if same, if not, error and retry
    c_pwd = input("Please confirm your password: \n")
    while c_pwd != n_pwd:
        print("Passwords does not match!")
        n_pwd = input("Enter a new password: \n")
        c_pwd = input("Please confirm your password: \n")
        
# If same, write into user.txt in new line.
    with open('user.txt', 'a') as file_user:
        file_user.write(f"\n{n_user}, {c_pwd}")
        
    user_dict[n_user] = n_pwd
    return user_dict

def display_stats():
    #   ==== DISPLAY STATISTICS ====
    # In this block, check if username is "admin"
            # Display total number of tasks
            # Display total number of users
    if username == "admin":
        print(f'''
{"–" * 35}
Number of Tasks:	{len(tasks)}
Number of Users:	{len(user_dict)}
{"–" * 35}
''')
    else:
        print("*** Access unauthorised ***")


def get_and_validate_task_date():
    # Ask for due date of task - Validate format of date and not earlier than today
    
    valid = False
    while not valid:
        t_date = input("Enter due date of the task: Format dd mmm yyyy\n")
        
        try:
            t_date = datetime.datetime.strptime(t_date, "%d %b %Y")
            if today.date() < t_date.date():
                valid = True
            else:
                print("Error: Date cannot be earlier than today!\n")
        except ValueError:
            print("Error: Wrong date format!\n")
    return t_date


def get_and_validate_entry_date():
    # Ask for current date
    valid = False
    while not valid:
        today_input = input("Enter today's date: Format dd mmm yyyy\n")
        try:
            today_input = datetime.datetime.strptime(today_input, "%d %b %Y")
            if today.date() == today_input.date():
                valid = True
            else:
                print("Error: Date cannot be earlier than today!\n")
        except ValueError:
            print("Error: Wrong date format!\n")
    return today_input


# Ask if the task is complete
def isComplete(question):
    
    answer = input(question + " (Yes or No): \n").lower().strip()
    
    while not(answer == "y" or answer == "yes" or \
    answer == "n" or answer == "no"):
        print("Input Yes or No")
        answer = input(question + "(Yes or No): \n").lower().strip()
    return answer


def add_task(tasks):
    # Ask for username of person of task, check if username in dict
    t_user = input("Enter username of person in charge of task: \n")
    while t_user not in user_dict:
        print("Username is not found!")
        t_user = input("Enter username of person in charge of the task: \n")
        
    # Ask for title of task
    t_title = input("Enter title of the task: \n")
    # Ask for descript of task
    t_desc = input("Enter description of the task: \n")
    t_date = get_and_validate_task_date()
    today_date = get_and_validate_entry_date()
    status = isComplete("Is the task completed?")

    # Add task into tasks.txt
    with open('tasks.txt', 'a') as file_tasks:
        newTaskList = [t_user, t_title, t_desc, today_date.strftime("%d %b %Y"), 
            t_date.strftime("%d %b %Y"), status]
        task_list = ', '.join(map(str, newTaskList))
        file_tasks.write(f"\n{task_list}")
        print("The new task has been checked and added.")
    tasks.append(task_list)
    return tasks

def print_task_nicely(task):
    # write code to print it nice
            print("–" * 35)
            print(f'''
    Task:				{task[1]}
    Assigned to:		{task[0]}
    Date Assigned:		{task[3]}
    Due Date:			{task[4]}
    Completed?			{task[5]}
    Task Description:
    {task[2]}
    ''')
            print("–" * 35)
    

def view_all_tasks(tasks):
    for task in tasks:
        print_task_nicely(task)

def view_my_tasks(tasks, username):
    for task in tasks:
        if task[0] == username:
            print_task_nicely(task)

#   ====MENU Section====
#   presenting the menu to the user and 
#   making sure that the user input is converted to lower case.

tasks = read_task_file()
user_dict = read_user_file()
username = login(user_dict)
menu = None
while menu != 'e':
    menu = input('''Select one of the following Options below:
    r - Registering a user (admin only)
    s - Display Statistics (admin only)
    a - Adding a task
    va - View all tasks
    vm - View my task
    e - Exit
    : ''').lower()
    #   ==== REGISTER NEW USER ====
    #   In this block you will write code to add a new user to the user.txt file
    if menu == 'r':
        if username=='admin':
            user_dict = register_user(user_dict)
        else:
            print('*** Access unauthorised ***')
    #   ==== ADD TASK ====
    elif menu == 'a':
        tasks = add_task(tasks)
    
    elif menu == 's':
        display_stats()
    
    elif menu == 'va':
        view_all_tasks(tasks)
    
    elif menu == 'vm':
        view_my_tasks(tasks, username)
        
    elif menu == 'e':
        print('Goodbye!!!')
    
    else:
        print("You have made a wrong choice, Please Try again")

exit()
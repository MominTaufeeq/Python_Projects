def task():
    task = []
    print("-----Welcome to the task Management App -----")
    total_task = int(input("Enter how many task you want to add "))
    for i in range(1, total_task + 1):
        task_name = input(f"Enter your task {i} :-")
        task.append(task_name)

    print(f"Today task are\n{task}")
    while True:
        operation = int(input("Enter 1-Add\n2-Update\n3-Delete\n4-View\n5-Exit/Stop/"))
        if operation == 1:
            add = input("Enter task you want to add = ")
            task.append(add)
            print(f"Task {add} has been successfully added...")
        elif operation == 2:
            update = input("Enter the task name you want update = ")
            if update in task:
                up = input("Enter new task = ")
                ind = task.index(update)
                task[ind] = up
                print(f"Upadated task {up}")

        elif operation == 3:
            delete = input("Enter the task you want to delete :-")
            if delete in task:
                ind = task.index(delete)
                del task[ind]
                print(f"This Task {delete} is delete successfully ")
        elif operation == 4:
            print(f"Total task ={task}")
        elif operation == 5:
            print("Closing the program..")
            break
        else:
            print("Invalid Input")


task()

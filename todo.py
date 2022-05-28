import datetime as dt
import time as t

date = dt.datetime.now().strftime("%y-%m-%d %H:%M:%S")  # date format being year month date hour minute second


def main():
    choice = int(input("Hello, welcome to your to do list!"
                       "\nType 1 to create a task\nType 2 to see your tasks\nType 3 to delete a task\n"
                       "Your choice: "))

    if choice == 1:
        create_task()
    elif choice == 2:
        see_task()
    elif choice == 3:
        delete_task()
    else:
        print("That is not a choice!")
        t.sleep(1)
        print("\n" * 100)
        main()


def create_task():
    task = input("Okay, so you want to make a task! The date will be automatically added\nType your task here: ")

    createtask = open("todolist.txt", "a")  # open the file in add mode
    createtask.write(f"{task}, at: {date}\n")  # write task and date
    createtask.close()  # close

    print("Okay! You're done here! See you later!")


def see_task():
    seetask = open("todolist.txt", "r")  # open file in read mode
    print(seetask.read())  # write all the tasks in console
    seetask.close()  # close

    print("Done, see you later!")


def delete_task():
    deletion = int(input("Please type the line number of your task.\nNumber goes here: "))

    with open("todolist.txt", "r") as f:  # open the file in read mode
        lines = f.readlines()  # read all lines
        pointer = 1  # position

    with open("todolist.txt", "w") as f:  # open the file in write mode
        for line in lines:
            if pointer != deletion:  # remove the specified line
                f.write(line)
            pointer += 1

    print("Done! See you later!")


main()
# start the program

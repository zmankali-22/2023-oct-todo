import csv

def add_todo(file_name):
    print("add to do")
    #  Ask title of todo
    todo_name = input("Enter a todo: ")
    # open the file list.csv
    with open(file_name, "a") as f:
        writer = csv.writer(f)
    # winsert values- title = user entered
                    # - completed = False
        writer.writerow([todo_name, "False"])



def remove_todo(file_name):
    print("remove to do")
    


def mark_todo(file_name):
    print("mark to do")
    


def view_todo(file_name):
    print("view to do")
    
    

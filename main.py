import os

class TodoClass:
    def createATodo(self, todo_title, todo_content, todo_tag, todo_status):
        self.todo_title = todo_title
        self.todo_tag = todo_tag
        self.todo_content = todo_content
        self.todo_status = todo_status
        file = open("todos/logs.todoApp", "a")
        file.write(self.todo_title + "\n")
        file.close()
        os.mkdir(f"todos/{self.todo_title}")
        file = open(f"todos/{self.todo_title}/t-title.txt", "w")
        file.write(self.todo_title)
        file.close()
        file = open(f"todos/{self.todo_title}/t-content.txt", "w")
        file.write(self.todo_content)
        file.close()
        file = open(f"todos/{self.todo_title}/t-tag.txt", "w")
        file.write(self.todo_tag)
        file.close()
        file = open(f"todos/{self.todo_title}/t-status.txt", "w")
        file.write(self.todo_status)
        file.close()

    def showTodos(self):
        file = open("todos/logs.todoApp", "r")
        todos = file.read()
        file.close()
        print(todos)
    
    def showATodo(self, todo_name):
        self.todo_open_name = todo_name
        file = open(f"todos/{self.todo_open_name}/t-title.txt", "r")
        text = file.read()
        print("Title : "+text)
        file.close()
        file = open(f"todos/{self.todo_open_name}/t-content.txt", "r")
        text = file.read()
        print("Content : "+text)
        file.close()
        file = open(f"todos/{self.todo_open_name}/t-tag.txt", "r")
        text = file.read()
        print("Tag : "+text)
        file.close()
        file = open(f"todos/{self.todo_open_name}/t-status.txt", "r")
        text = file.read()
        print("Status : "+text)
        file.close()

    def editATodo(self, tn):
        self.editTodoName = tn
        file = open(f"todos/{self.editTodoName}/t-title.txt", "r")
        text = file.read()
        print("Title : "+text)
        file.close()
        file = open(f"todos/{self.editTodoName}/t-content.txt", "r")
        text = file.read()
        print("Content : "+text)
        file.close()
        file = open(f"todos/{self.editTodoName}/t-tag.txt", "r")
        text = file.read()
        print("Tag : "+text)
        file.close()
        file = open(f"todos/{self.editTodoName}/t-status.txt", "r")
        text = file.read()
        print("Status : "+text)
        file.close()
        tt = input("Pls Enter Todo Title: ")
        tcontent = input("Pls Enter todo content: ")
        ttag = input("Pls Enter a todo tag: ")
        ts= input("Pls Enter a todo status: ")
        os.mkdir(f"todos/{tt}")
        file = open(f"todos/{tt}/t-title.txt", "w")
        file.write(tt)
        file.close()
        file = open(f"todos/{tt}/t-content.txt", "w")
        file.write(tcontent)
        file.close()
        file = open(f"todos/{tt}/t-tag.txt", "w")
        file.write(ttag)
        file.close()
        file = open(f"todos/{tt}/t-status.txt", "w")
        file.write(ts)
        file.close()
        file = open("todos/logs.todoApp", "a")
        file.write(tt + "\n")
        file.close()

if __name__ == "__main__":
    todoManage = TodoClass()
    while True:
        print('''

████████╗░█████╗░██████╗░░█████╗░  ░█████╗░██████╗░██████╗░
╚══██╔══╝██╔══██╗██╔══██╗██╔══██╗  ██╔══██╗██╔══██╗██╔══██╗
░░░██║░░░██║░░██║██║░░██║██║░░██║  ███████║██████╔╝██████╔╝
░░░██║░░░██║░░██║██║░░██║██║░░██║  ██╔══██║██╔═══╝░██╔═══╝░
░░░██║░░░╚█████╔╝██████╔╝╚█████╔╝  ██║░░██║██║░░░░░██║░░░░░
░░░╚═╝░░░░╚════╝░╚═════╝░░╚════╝░  ╚═╝░░╚═╝╚═╝░░░░░╚═╝░░░░░        
        
    Pls Choose One Of The Following Option:-
    1) Create A Todo
    2) See All Todo
    3) Edit A Todo
    4) Exit
        ''')
        text = input("//?-> ")
        if text == "1":
            tt = input("Pls Enter Todo Title: ")
            tcontent = input("Pls Enter todo content: ")
            ttag = input("Pls Enter a todo tag: ")
            ts= input("Pls Enter a todo status: ")
            todoManage.createATodo(tt, tcontent, ttag, ts)
        
        elif text == "2":
            todoManage.showTodos()
            todo_name = input("pls enter the todo you want to see: ")
            todoManage.showATodo(todo_name)
            wait = input("")
        
        elif text == "3":
            todoManage.showTodos()
            edit_todo_name = input("Pls Enter The Todo You Want To Edit: ")
            todoManage.editATodo(edit_todo_name)
        
        elif text == "4":
            break
        
        else:
            print("Error")
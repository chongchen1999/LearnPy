def check_login(func):
    def inner():
        if "admin" != input("Enter username: "):
            print("Access denied")
            return
        
        if "123456" != input("Enter password: "):
            print("Access denied")
            return
        
        if "7788" != input("Enter code: "):
            print("Access denied")
            return
        
        func()
    
    return inner

@check_login
def enter_system():
    print("Access granted")

enter_system()
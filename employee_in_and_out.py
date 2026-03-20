class employee():
    def __init__(self):
        print("employee")
    def __del__(self):
        print("destruction imminent")
def create_obj():
    print("object creates")
    obj=employee()
    print("function gone")
    return obj
obj=create_obj()
print("program end")
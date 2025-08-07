class MyClass:
    def __init__(self,value):
        self.value=value

    def show(self):
        print(f"Value is {self.value}")

    @property
    def ten_value(self):
        return 10*self.value
    
    @ten_value.setter
    def ten_value(self,user_value):
        self.value=user_value/5
if __name__=="__main__":
    obj=MyClass(100)
    obj.ten_value=25
    print(obj.ten_value)
    obj.show()
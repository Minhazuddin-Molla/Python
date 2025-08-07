def greet(fx):
    def mfx():
        print("Good Morning")
        fx()
        print("Thanks for using the function.")
    return mfx
# def hello():
#     print("Hello world")
# greet(hello)()          
#It can also be done in the other way
@greet
def hello():
    print("Hello world")
hello()
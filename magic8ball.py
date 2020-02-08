import random
def get_q():
    question = input("What is your question?: ")
    if question:
        get_advice(str(question))
def get_advice(question):
        rannum = random.randint(1, 7)
        if rannum == 1:
            print("Do it!!!")
        elif rannum == 2:
            print("Forget you ever though of that!!!")
        elif rannum == 3:
            print("No clue") 
        elif rannum == 4:
            print("Solid maybe")
        elif rannum == 5:
            print("Ask again later...")
        elif rannum == 6:
            print("Just have fun with it")   
while( 1 < 2):
    get_q()      
                      

queue =[]
max =5
def enqueue():
    if len(queue)>=max:
        print("queue overflow! parking is full")
    else:
        car=input("Enter car number:")
        queue.append(car)
        print(car, "Entered the parking")
def dequeue():
    if len (queue)==0:
            print("queue underflow!parking is empty")
    else:
        removed_car =queue.pop()
        print(removed_car, "left the parking")
def display():
     if len (queue)==0:
            print("parking is empty")
     else:
        print("\n cars in parking")
        for car in queue:
            print(car)
while True :
    print("\n--- CAR PARKING QUEUE MENU---")
    print("1.inqueue car")
    print("2.dequeue car")
    print("3.display queue")
    print("4.exit")
    choice =int(input("Enter your choice"))
    if choice==1:
     enqueue()
    elif choice==2:
     dequeue()
    elif choice==3:
     display()
    elif choice==4:
     print("Exiting program:")
    else:
        print ("invalid choice")

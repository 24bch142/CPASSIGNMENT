stack = []

while True:
    print("\n1. Push\n2. Pop\n3. Display\n4. Exit")
    choice = int(input("Enter choice: "))

    if choice == 1:
        stack.append(int(input("Enter element to push: ")))
    elif choice == 2:
        if stack:
            print("Popped:", stack.pop())
        else:
            print("Stack is empty")
    elif choice == 3:
        print("Stack:", stack)
    elif choice == 4:
        break
    else:
        print("Invalid choice")

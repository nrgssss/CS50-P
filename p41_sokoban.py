def main():
    history = []

    while True:
        action = input("Action: ")
        if action == "Undo":
            Undone = history.pop()
            print(f"Undone:{Undone}")
        elif action == "Restart":
            history.clear()
        else:
            history.append(action)
            print(history)

main()
words={"HAIR":4,"CHAIR":5,"PAIR":4,"GRAPHIC":7}
def main():
    print("Welcome to spelling bee!")
    print("YOUR LETTERS ARE A B C D")
while len(words)>0:
    print(f"{len(words)}words left.")
    guess=input("Guess a word: ")
    
    if guess =="GRAPHIC":
        words.clear()
        print("you have won!")

    if guess in words.keys():
        points= words.pop(guess)
        print(f"GOOD JOB!YOU SCORED {points} points.")

main()
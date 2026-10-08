words={"PAIR":4 , "CHAIR":5 , "HAIR":4}
def main():
    print("Welcome to the Spelling bee")
    print("Your letters are: A I P C R H G")

    while(len(words)) > 0 :
        print(f"{len(words)} words left!")
        guess=input("Guess a word: ")

        if guess in words.keys():
            points=words.pop(guess)
            print(f"GOOD JOB! YOU SCORED {points} points.")

    print("That's the game!")

main()
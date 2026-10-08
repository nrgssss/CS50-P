def main():
    names=["Maeio", "Luigi","Daisy","Yoshi"]
    for name in names:
        print(write_letter(name, "princess peach"))


def write_letter(reciver,sender):
    return f"""

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
     Dear {reciver}

     You are cordially to a ball at
     Peach's castle this evening , 7:00 PM.

     sincerely,
     {sender}

~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
"""
main()
     

distances={
    "Voyager 1":"163",
    "Voyager 2":"136",
    "Poineer 10" :"80 AU",
    "New Horizons" : "58",
    "Poineer 11" :"44 AU"
}

def main():
    spacecraft = input("Enter a spacecraft: ")
    try:
      au =float(distances[spacecraft])
    except KeyError:
        print(f"{spacecraft} is not in dictionary")
        return
    except ValueError:
        print(f"Can not convert '{distances[spacecraft]}' to a float")
        return

    m = convert(au)
    print (f"{m} m away")

def convert(au):
    return au * 1495978765

main()

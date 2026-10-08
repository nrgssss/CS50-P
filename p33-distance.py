distances={
   "voyager1":16,
   "voyager2":144,
   "pioneer10":80,
   "new horizon":58,
   "pioneer11":40
}
def main():
    for distance in distances.values():
        print(f"{distance} AU is {convert(distance)}m")
def convert(au):
    return au * 149597870700

main()


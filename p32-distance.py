distance={
   "voyager1":16,
   "voyager2":144,
   "pioneer10":80,
   "new horizon":58,
   "pioneer11":44
}

def main():
    for name in distance.keys():
        print(f"{name} is {distance [name]} AU from earth")

main()
def print_range (start:int, end:int):
    for i in range (start,end+1):
        print(i,end="\t")

sn=int(input("Enter start number: "))
en=int(input("Enter end number:"))
if sn>en:
    sn,en=en,sn
print_range (sn,en)
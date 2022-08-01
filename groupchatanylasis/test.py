f = open('majorfordatabase.txt', 'r')


for row in f: 
    row = row.rstrip()
    name = "[Display(Name = \"" + row + "\")]"
    attribute = row.replace(" ","").replace("-","") + ","
    print(name)
    print(attribute)

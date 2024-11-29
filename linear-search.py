MyList = [1,2,3,4,5,6,7,8,9]

def search():
    print("Welcome to linear search")
    print("Please enter your item")
    item = int(input())
    ub = len(MyList) - 1
    found = False
    index = 0
    while found == False and index <= ub:
        if item == MyList[index]:
            found = True
        index = index + 1
    if found == True:
        print(f"Item found at index : {index - 1} and your item is {MyList[index - 1]}")
    else:
        print("Item not found :(")

search()

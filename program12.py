a = [x for x in input().split()] # creating list using user input
print(a)
def create_list(a):
    first_last = []
    first_last.append([a[0],a[-1]])
    print(first_last)

create_list(a)
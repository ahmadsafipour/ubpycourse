b="yes"
s=dict()
while b=="yes" or b=="y" :
    print("Enter:")
    a=input()
    if a in s:
        print("Antonym is:")
        print(s[a])
    else :
        print("Sorry, There Is No Word In Diractory\nDo You Want To Add?")
        b=input()
        if b=="yes" or b=="y":
            print("Add Antonym")
            b=input()
            s[a]=b
    print(s)
    print("\n\n Keep Going?")
    b=input()
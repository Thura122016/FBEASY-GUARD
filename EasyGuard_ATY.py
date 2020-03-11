import os
print("Facebook profile_guard enabler/disabler:3\n\nPls choose 1 or 2\n\n1.Enable\n2.Disable\n")
ed = input("1 or 2  : ")
u = input("Enter email : ")
p = input("Password : ")
if ed=="1":
    pyhton guard.py --user=u --password=p --enable
elif ed=="2":
    pyhton guard.py --user=u --password=p --disable
else:
    print("Error : pls choose 1 or 2.")
input()

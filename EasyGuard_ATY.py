import os
print("Facebook profile_guard enabler/disabler:3\n\nPls choose 1 or 2\n\n1.Enable\n2.Disable\n")
ed = input("1 or 2  : ")
u = input("Enter email : ")
p = input("Password : ")
if ed=="1":
    ed="enable"
elif ed=="2":
    ed = "disable"
else:
    print("Error : pls choose 1 or 2.")
if ed == "enable" or ed == "disable":
    print("py guard.py --user={} --password={} --{}".format(u,p,ed))
    os.system("py guard.py --user={} --password={} --{}".format(u,p,ed))
input()

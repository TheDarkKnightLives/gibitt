import os 


def help():
    print(": help box :")
    print(": main seq : (main)")
    print(":::: does everything including creating repo and pushes ...")
    print(": side seq : (side)")
    print(":::: does pushing and commit and adds all the files ")
    print(": new branch: (newbranch)")
    print(":::: creates a new branch and u set that branch as default ...")
    print(": push to branch :(verabranch)")
    print(":::: this will add files an commit and push to the branch that u specify ...")
    print(": bye or exit  :")
    print(":::: well what do u think it does ... byee duhhhh ")

def main():
    help()
    while True:
        val = input(">>>").replace(" " , "")
        if (val == "main"):
            print("creating repo ... ")
            name = input("name of repo :")
            os.system(f"gh create repo {name}")
            print("initialising ... ")
            os.system("git init ")
            print("adding files ... ")
            os.system("git add . ")
            print("commiting ")
            commit = input("commit message :")
            os.system(f"git commit -m {commit}")
            print("setting origin and pushing ")
            os.system("git branch -M main ")
            os.system("git push -u origin main ")
            inpt = input("wanna continue or nah (type yay or nay ):")
            if (inpt == "nay"):
                print("bye pangu ")
                break 

        elif (val == "side"):
            print("adding files ... \n commiting ... ")
            commit = input("commit msg :")
            os.system("git add . ")
            os.system(f"git commit -m {commit}")
            print("pushing ... ")
            os.system("git push -u origin main ")
            inpt = input("wanna continue or nah (type yay or nay ):")
            if (inpt == "nay"):
                print("bye pangu ")
                break 

        elif (val == "help"):
            print("haha noob ...")
            help()

        elif (val == "newbranch"):
            print("creating new branch ...")
            name = input("name of the new branch :")
            os.system(f"git branch {name}")
            os.system(f"git checkout {name}")
            inpt = input("wanna continue or nah (type yay or nay ):")
            1
            if (inpt == "nay"):
                print("bye pangu ")
                break

        elif (val == "verabranch"):
            print("adding ... \ncommiting ... \n asking ur branch ...")
            name = input("ur branch name:")
            os.system("git add . ")
            commit = input("ur commit msg:")
            os.system(f"git commit -m {commit}")
            os.system(f"git push -u origin {name}")
            inpt = input("wanna continue or nah (type yay or nay ):")
            if (inpt == "nay"):
                print("bye pangu ")
                break 


        elif (val == "exit" or val == "bye"):
            print("bye da ... ")
            break

        else :
            print("thappu thambi ... ")



main()






import os

def main():
    file = open("file.txt", "a")
    file.write("a\n")
    file.close()
    os.system("git add .")
    os.system("git commit -m '[ENHANCEMENT] Secret comimt'")
    os.system("git push origin main")


main()
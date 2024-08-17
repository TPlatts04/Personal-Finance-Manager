import os
import csv
import sys

if __name__ == "__main__":
    if os.path.isfile(FILENAME):
        main()
    else:
        with open(FILENAME, "w") as file:
            file.writelines("name,typeOfSpend,amount\n")
        main()
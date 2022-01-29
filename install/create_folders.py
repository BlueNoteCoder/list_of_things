import os
import time


def is_dir_created(PATH: str):
    return os.path.isdir(PATH)


def main():
    LOGS_PATH = "../logs"
    DATABASE_PATH = "../databases"

    if not is_dir_created(LOGS_PATH):
        print("Creating " + LOGS_PATH + " directory")
        os.mkdir(LOGS_PATH, 0o0775)
    # Check for path
    time.sleep(2)

    print(LOGS_PATH + " directory created")

    time.sleep(4)

    if not is_dir_created(DATABASE_PATH):
        print("Creating " + DATABASE_PATH + " directory")
        os.mkdir(DATABASE_PATH, 0o0775)
        # Check for path
        time.sleep(2)

    print(DATABASE_PATH + " directory created")



if __name__ == "__main__":
    main()

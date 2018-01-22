import os

def main():

    homeDir = os.listdir('/home/')
    return homeDir


if __name__ == '__main__':

    print(main())
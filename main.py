def main():
    mkfile()
    print("This is the main function of the application.")

def test1():
    print("This is test function 1.")   

def test2():
    print("This is test function 2.")

def mkfile():
    import os
    with open("testfile.txt", "w") as f:
        f.write("This is a test file.")

if __name__ == "__main__":
    main()
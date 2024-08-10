def main():
    plate = input("Plate: ")



def is_valid(s):
    ...

def checkFirst(s):
    return True if s[0:2].isalpha() else False 

def checklength(s):
    if 2 < len(s) <= 6:
        return True
    else:
        return False


if __name__ == "__main__":
    main()
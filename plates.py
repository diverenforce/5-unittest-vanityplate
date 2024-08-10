def main():
    plate = input("Plate: ")



def is_valid(s):
    if check_first(s) and check_length(s) and check_end(s):
        for i in range(len(s)):
            if s[i] == '0' and s[i - 1].isalpha():
                break
            
        return True

    else:
        return False


def check_first(s):
    return True if s[0:2].isalpha() else False 

def check_length(s):
    if 2 < len(s) <= 6:
        return True
    else:
        return False

def check_end(s):
    return True if s[-1].isnumeric() else False

if __name__ == "__main__":
    main()
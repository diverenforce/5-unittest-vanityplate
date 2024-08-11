def main():
    plate = input("Plate: ")

    if is_valid(plate):
        print("Valid")
    else:
        print("Invalid")


def is_valid(s):
    if check_first(s) and check_length(s) and check_punct(s):
        for i in range(len(s)):
            if (s[i] == "0" and s[i - 1].isalpha()) or (
                s[i].isnumeric() and s[i] != s[-1] and s[i + 1].isalpha()
            ):
                return False

        return True

    else:
        return False


def check_first(s):
    return True if s[0:2].isalpha() else False


def check_length(s):
    if 2 <= len(s) <= 6:
        return True
    else:
        return False

def check_punct(s):
    return True if s.isalnum() else False



# def check_end(s):
#     return True if s[-1].isnumeric() else False


if __name__ == "__main__":
    main()

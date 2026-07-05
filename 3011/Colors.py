"""Colors"""
def main():
    """Colors"""
    c1 = input()
    c2 = input()
    if c1 == "Red" and c2 == "Red":
        print("Red")
    elif c1 == "Red" and c2 == "Yellow" or c1 == "Yellow" and c2 == "Red":
        print("Orange")
    elif c1 == "Yellow" and c2 == "Yellow":
        print("Yellow")
    elif c1 == "Yellow" and c2 == "Blue" or c1 == "Blue" and c2 == "Yellow":
        print("Green")
    elif c1 == "Blue" and c2 == "Blue":
        print("Blue")
    elif c1 == "Blue" and c2 == "Red" or c1 == "Red" and c2 == "Blue":
        print("Violet")
    else:
        print("Error")
main()

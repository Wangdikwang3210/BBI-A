string="geeks"

def test(string):
    string="geeksforgeeks"
    print("inside function:", string)

# driver's code
test(id(string))
print("outside function:", string)
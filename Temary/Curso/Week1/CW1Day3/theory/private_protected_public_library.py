class ppp2:
    # Public 
    def public_function(self):
        print("public")

    # Protected
    def _protected_function(self):
        print("Protected")

    # Private
    def __private_function(self):
        print("Private")


if __name__ == "__main__":
    p = ppp2()
    print("We are going to test the functions: \n\n\n\n")
    print("--------------------------")
    print("Testing public...")
    p.public_function()
    print("--------------------------")
    print("Testing protected...")
    p._protected_function()
    print("--------------------------")
    print("Testing private...")
    p.__private_function()
    print("--------------------------")
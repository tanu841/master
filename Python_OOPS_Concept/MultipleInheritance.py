from Python_OOPS_Concept.Inheritance import mackbook


class OperatingSystem:
    multi_tasking = True
    name = "Mac OS"

class Apple:
    website = "www.apple.com"
    name = "Apple Inc."

class MacBook(Apple,OperatingSystem):
    def __init__(self):
        if self.multi_tasking is True:
            print("This is a multi-tasking system. Visit {} for more details".format(self.website))
            print("Name: ", self.name)
mackbook=MacBook()

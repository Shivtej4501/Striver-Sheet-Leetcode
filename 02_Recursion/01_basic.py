## Print the Name n times
class NameNtims: 
    n = 0

    def name (self):
        if self.n == 5:
            return
        print("Name ", self.n)
        self.n= self.n +1
        self.name()

if __name__ == '__main__':
    no = NameNtims()
    no.name()



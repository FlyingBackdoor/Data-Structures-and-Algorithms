class hashMap():
    def __init__(self, size):
        super(hashMap, self).__init__()
        self.data = [[None] for i in range(size)]

    def _hashIt(self, key):
        hash = 0
        key = str(key)
        for i in range(len(key)):
            hash = (hash + ord(key[i]) * i) % len(self.data)
        return hash

    def set(self, key, value):
        addr = self._hashIt(key)
        setx = self.data[addr]

        if (setx[0] is None):
            setx[0] = [key, value]
        else:
            setx.append([key, value])

    def get(self, key):
        addr = self._hashIt(key)
        setx = self.data[addr]

        for i in range(len(setx)):
            if setx[i] is None:
                return "Not found"

            if setx[i][0] is key:
                return setx[i][1]

        return "Not Found"


obj = hashMap(50)

obj.set("apple", 5)
obj.set("mango", 10)
obj.set("eggs", "1 dozen")

#print(obj.data)

print(obj.get("eggs"))
print(obj.get('apple'))

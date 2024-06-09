class pg9e2:
    @staticmethod
    def methodTambah(x, y):
        if isinstance(x, int) and isinstance(y, int):
            return pg9e2.methodTambahInt(x, y)
        elif isinstance(x, float) and isinstance(y, float):
            return pg9e2.methodTambahFloat(x, y)
        else:
            raise TypeError("Unsupported types: {} and {}".format(type(x), type(y)))
    
    @staticmethod
    def methodTambahInt(x, y):
        return x + y

    @staticmethod
    def methodTambahFloat(x, y):
        return x + y

myNum1 = pg9e2.methodTambah(8, 5)
myNum2 = pg9e2.methodTambah(4.5, 6.5)

print("int:", myNum1)
print("float:", myNum2)

char_table = {chr(i): f"{i-65:0>2d}" for i in range(65, 91)}
char_table[' '] = '26'

class RSA:
    def __init__(self,p,q,e,data):
        self.p = p
        self.q = q
        self.e = e
        self.d = 0
        self.data = data

    def get_n(self):
        return self.p * self.q

    def get_public_key(self):
        return self.e

    def caculate_d(self):
        self.d = pow(self.e,-1,(self.p-1)*(self.q-1))
        return True

    def encrypt(self):
        n = self.get_n()
        e = self.get_public_key()
        pre_encrypt_data = ""
        encrypt_data = []
        for i in self.data:
            pre_encrypt_data += char_table[i]
        encrypt_data = [int(pre_encrypt_data[i:i+4]) for i in range(0,len(pre_encrypt_data),4)]
        for i in range(len(encrypt_data)):
            encrypt_data[i] = pow(encrypt_data[i],e,n)
        self.encrypt_data = encrypt_data
        return encrypt_data

    def decrypt(self):
        n = self.get_n()
        d = self.d
        decrypt_data = []
        for i in self.encrypt_data:
            decrypt_data.append(pow(i,d,n))
        return " ".join(list(map(str,decrypt_data)))

if __name__ == '__main__':
    data = input("input data: ")
    p = int(input("input p: "))# 素数 1
    q = int(input("input q: "))# 速數 2
    e = int(input("input e: "))# 公鑰
    rsa = RSA(p,q,e,data)
    rsa.caculate_d()
    print("d: ",rsa.d)
    print("n: ",rsa.get_n())
    en = " ".join(list(map(str,rsa.encrypt())))
    print("encrypt data(C): ",en)
    print("decrypt data(M): ",rsa.decrypt())
    

    
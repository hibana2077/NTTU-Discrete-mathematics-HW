import json

char_table = {chr(i): f"{i-65:0>2d}" for i in range(65, 91)}
char_table[' '] = '26'

def read_json_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data

def write_json_file(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)
    return True

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
    total_data = read_json_file("data.json")
    data = total_data['data']
    p = total_data['p']# 素数 1
    q = total_data['q']# 速數 2
    e = total_data['e']# 公鑰
    rsa = RSA(p,q,e,data)
    rsa.caculate_d()
    print(f"data: {data}")
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print("d: ",rsa.d)
    print("n: ",rsa.get_n())
    en = " ".join(list(map(str,rsa.encrypt())))
    print("encrypt data(C): ",en)
    print("decrypt data(M): ",rsa.decrypt())
    save_data = {
        "data": data,
        "p": p,
        "q": q,
        "e": e,
        "d": rsa.d,
        "n": rsa.get_n(),
        "encrypt_data": en,
        "decrypt_data": rsa.decrypt()
    }
    write_json_file("anser.json",save_data)
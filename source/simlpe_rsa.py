char_table = {chr(i): f"{i-65:0>2d}" for i in range(65, 91)}
char_table[' '] = '26'
import json
print('='*50)
print(f"{'🔑RSA 加解密作業🔑':^50}")
print('='*50)
def read_json_file(file_name):
    with open(file_name, 'r') as f:
        data = json.load(f)
        return data

def write_json_file(file_name, data):
    with open(file_name, 'w') as f:
        json.dump(data, f)
    return True

#input data
if input("input data from file? (y/n): ") == 'y':
    temp = read_json_file("data.json")
    p,q,e,data = temp['p'],temp['q'],temp['e'],temp['data']
else:
    p,q,e,data= int(input("input p: ")),int(input("input q: ")),int(input("input e: ")),input("input data: ")
out = "OUTPUT"
print(f"{out:=^50}")
d,n = pow(e,-1,(p-1)*(q-1)),p * q
print(f"d: {d}")
print(f"n: {n}")
data += ' ' if len(data)%2 else ''
pre_encrypt_data = "".join([char_table[i] for i in data])
encrypt_data = [int(pre_encrypt_data[i:i+4]) for i in range(0,len(pre_encrypt_data),4)]
encrypt_data = [pow(i,e,n) for i in encrypt_data]
print(f"encrypt data(C): {' '.join(list(map(str,encrypt_data)))}")
decrypt_data = [pow(i,d,n) for i in encrypt_data]
print(f"decrypt data(M): {' '.join(list(map(str,decrypt_data)))}")
print(f"{out:=^50}")
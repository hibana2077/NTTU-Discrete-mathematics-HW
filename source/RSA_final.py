
#  _     _ _                        _____  _____  ____________
# | |   (_) |                      / __  \|  _  ||___  /___  /
# | |__  _| |__   __ _ _ __   __ _ `' / /'| |/' |   / /   / / 
# | '_ \| | '_ \ / _` | '_ \ / _` |  / /  |  /| |  / /   / /  
# | | | | | |_) | (_| | | | | (_| |./ /___\ |_/ /./ /  ./ /   
# |_| |_|_|_.__/ \__,_|_| |_|\__,_|\_____/ \___/ \_/   \_/    

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

def d_and_n(p,q,e):
    d = pow(e,-1,(p-1)*(q-1))
    n = p * q
    return d,n

def encrypt(data,e,n):
    data += ' ' if len(data)%2 else ''
    pre_encrypt_data = "".join([char_table[i] for i in data])
    encrypt_data = [int(pre_encrypt_data[i:i+4]) for i in range(0,len(pre_encrypt_data),4)]
    encrypt_data = [pow(i,e,n) for i in encrypt_data]
    return encrypt_data

def decrypt(data,d,n):
    return [pow(i,d,n) for i in data]

#input data
if input("input data from file? (y/n): ") == 'y':
    temp = read_json_file("data.json")
    p,q,e,data = temp['p'],temp['q'],temp['e'],temp['data']
    print(f"p: {p}")
    print(f"q: {q}")
    print(f"e: {e}")
    print(f"data: {data}")
else:
    p,q,e,data= int(input("input p: ")),int(input("input q: ")),int(input("input e: ")),input("input data: ")
out = "OUTPUT"
print(f"{out:=^50}")
d,n = d_and_n(p,q,e)
encrypt_data = encrypt(data,e,n)
decrypt_data = decrypt(encrypt_data,d,n)

print(f"d: {d}")
print(f"n: {n}")
print(f"encrypt data(C): {' '.join(list(map(str,encrypt_data)))}")
print(f"decrypt data(M): {' '.join(list(map(str,decrypt_data)))}")
print(f"{out:=^50}")
if input("save data to file? (y/n): ") == 'y':
    write_json_file("data.json",{"p":p,"q":q,"e":e,"data":data})
print('Done!')

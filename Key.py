import secrets
import math

prime = 643528272942127
generator = 21098140734109

class Key:
    def __init__(self, private_key, public_key):
        self.prime = prime
        self.generator = generator
        self.private_key = int(private_key)
        print(private_key)
        self.public_key = int(public_key)
        print(public_key)
        self.shared_key = pow(self.public_key,self.private_key,self.prime)
        print(self.shared_key)
        self.henon = HenonInitial(self.shared_key)
        self.arnold = ArnoldInitial(self.shared_key)

class HenonInitial:
    def __init__(self, k):
        k = str(k)
        if len(k) > 15:
            k = k[-15:]
        self.x = float("0."+k[:math.floor(len(k)/2)])
        self.y = float("0."+k[math.floor(len(k)/2):])
        
        print(self.x)
        print(self.y)

class ArnoldInitial:
    def __init__(self, k):
        k = str(k)
        self.p = int(k[:2])
        self.q = int(k[-2:])
        self.iter = int(k[math.floor(len(k)/2)])
        print(self.p)
        print(self.q)
        print(self.iter)

def genKeyPairs():
    pKey = secrets.randbits(53)
    pub = pow(generator,pKey,prime)
    return pKey, pub
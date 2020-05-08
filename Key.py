import secrets
import math

prime = 359061359866669
generator = 86171140759198

class Key:
    def __init__(self, private_key, public_key):
        self.prime = prime
        self.generator = generator
        self.private_key = int(private_key)
        self.public_key = int(public_key)
        self.shared_key = pow(self.public_key,self.private_key,self.prime)
        self.henon = HenonInitial(self.shared_key)
        self.arnold = ArnoldInitial(self.shared_key)

class HenonInitial:
    def __init__(self, k):
        k = str(k)
        self.x = float("0."+k[:math.floor(len(k)/2)])
        self.y = float("0."+k[math.floor(len(k)/2):])

class ArnoldInitial:
    def __init__(self, k):
        k = str(k)
        self.p = int(k[:2])
        self.q = int(k[-2:])
        self.iter = int(k[math.floor(len(k)/2)])

def genKeyPairs():
    pKey = secrets.randbits(53)
    return pKey, pow(generator,pKey,prime)
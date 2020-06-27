import secrets
import math

prime = 691701709719727733739743751757
generator = 243658791110131217141915231629

class Key:
    def __init__(self, private_key, public_key):
        self.prime = prime
        self.generator = generator
        self.private_key = int(private_key)
        self.public_key = int(public_key)
        self.shared_key = pow(self.public_key,self.private_key,self.prime)
        print(self.shared_key)
        self.henon = HenonInitial(self.shared_key)
        self.arnold = ArnoldInitial(self.shared_key)

# initial values for henon map
class HenonInitial:
    def __init__(self, k):
        k = str(k)
        if len(k) > 28:
            k = k[:28]
        x = float("0."+k[:math.floor(len(k)/2)])
        y = float("0."+k[math.floor(len(k)/2):])
        if(x>0.97):
            x=0.97-(x-0.97)
        if(y>0.97):
            y=0.97-(y-0.97)
        self.x = max(x,y)
        self.y = min(x,y)
        print(self.x)
        print(self.y)

# initial values for arnold cat map
class ArnoldInitial:
    def __init__(self, k):
        k = str(k)
        k_iter = k[-6:]
        self.iter = sum(int(digit) for digit in k_iter)

        self.p = k[:math.floor(len(k)/2)]
        self.q = k[math.floor(len(k)/2):]
        
        print(self.p)
        print(self.q)
        print(self.iter)
        
# generate key pairs
def genKeyPairs():
    pKey = secrets.randbits(100)
    pub = pow(generator,pKey,prime)
    return pKey, pub
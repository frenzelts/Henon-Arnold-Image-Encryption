# Henon-Arnold-Image-Encryption
Chaos-based image encryption for RGB images using combination of Henon map and Arnold cat map as the chaotic maps.
This encryption method needs a shared secret key for the Henon map and Arnold cat map parameters/initial values, which involves Diffie-Hellman algorithm for the key generation.

## How to encrypt
- Run **main.py**
- If you don't have the key pairs, **Generate new key pairs**
- Login with the generated private key
- Select **encrypt** mode
- Add images to be encrypted
- Select output destination path
- Input **receiver's public key**
- Encrypt

## How to decrypt 
- Run **main.py**
- Login with **your public key**
- Select **decrypt** mode
- Add images to be decrypted
- Select output destination path
- Input **sender's public key**
- Decrypt

## Graphical User Interface
Login UI                   |  Encryption UI
:-------------------------:|:-------------------------:
![Login](https://github.com/frenzelts/Henon-Arnold-Image-Encryption/blob/master/UI-Login.png)  |  ![Encryption](https://github.com/frenzelts/Henon-Arnold-Image-Encryption/blob/master/UI-Encryption.png)

## Key to Initial Values Algorithm
<p align="center">
  <img src="https://github.com/frenzelts/Henon-Arnold-Image-Encryption/blob/master/Flow-Key-to-Initial-Values.png">
</p>

## Encryption/Decryption Flow
<p align="center">
  <img src="https://github.com/frenzelts/Henon-Arnold-Image-Encryption/blob/master/Flow-Encryption-Decryption.png">
</p>
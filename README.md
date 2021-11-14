# Henon-Arnold-Image-Encryption
Chaos-based image encryption for RGB images using combination of Henon map and Arnold cat map as the chaotic maps.
This encryption method needs a shared secret key for the Henon map and Arnold cat map parameters/initial values, which involves Diffie-Hellman algorithm for the key generation.

## Dependencies Installation
- Make sure you have Python and PIP installed
- Install Numpy (pip install numpy)
- Install OpenCV (pip install opencv-python)
- Install TkInter (pip install tk)

## How to encrypt
- Run **main.py** (python main.py)
- If you don't have the key pairs, **Generate new key pairs**
- Login with the generated private key
- Select **encrypt** mode
- Add images to be encrypted
- Select output destination path
- Input **receiver's public key**
- Encrypt

## How to decrypt 
- Run **main.py** (python main.py)
- Login with **your private key**
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
  <img src="https://github.com/frenzelts/Henon-Arnold-Image-Encryption/blob/master/Flow-Encryption-and-Decryption.png">
</p>


# License
MIT License

Copyright (c) 2020 Frenzel Timothy Surya

Permission is hereby granted, free of charge, to any person obtaining a copy of this software and associated documentation files (the "Software"), to deal in the Software without restriction, including without limitation the rights to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the Software, and to permit persons to whom the Software is furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY, FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM, OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE SOFTWARE.
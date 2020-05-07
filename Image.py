from enum import Enum
import os
import cv2

class Image:
    def __init__(self, filepath, type, matrix):
        self.filepath = filepath
        self.filename = os.path.basename(filepath)
        self.type = type
        self.matrix = matrix
        self.dimension = self.matrix.shape

class Type(Enum):
    ORIGINAL = 1
    RESHAPED = 2
    CONFUSED = 3
    ENCRYPTED = 4
    UNDIFFUSED = 5
    UNCONFUSED = 6
    DECRYPTED = 7
    
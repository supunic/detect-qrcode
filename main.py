import sys
from pyzbar.pyzbar import decode
from PIL import Image
from typing import Optional

def run() -> None:
    args      = sys.argv
    imagePath = args[1]
    qrResults = QRreade(imagePath)

    for result in qrResults:
        print(result[0].decode('utf-8', 'ignore'))


def QRreade(image: str) -> Optional[list]:
    readResult = decode(Image.open(image))

    if (len(readResult) != 0):
        return readResult
    else:
        exit()

run()

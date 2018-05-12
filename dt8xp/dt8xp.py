"""
Detokenize 8xp program files for ti8x calculators.
"""

import xml.etree.ElementTree as ET


HEADER_LEN = 55 + 17 + 2 # TODO do something with the header, e.g. for filename
CRC_LEN = 2 # TODO check the CRC


def find_token(element, token):
    children = element.findall('{http://merthsoft.com/Tokens}Token')

    if children:
        for child in children:
            byte = int(child.get('byte')[1:], base=16)
            
            if byte == token:
                return child
    return None


def _detokenize(element, data, offset):
    if offset >= len(data):
        return None

    child = find_token(element, data[offset])
    if child is not None:
        result = _detokenize(child, data, offset + 1)

        if result is not None:
            return result
        
        string = child.get('string')
        if string == '\\n':
            string = '\n'
        print(string, end='')
        return offset + 1
    return None


def detokenize(data, xmlfile):
    tree = ET.parse(xmlfile)
    root = tree.getroot()
    i = 0
    while i < len(data):
        i = _detokenize(root, data, i)

def main():
    import argparse


    def bytes_from_file(filename, chunksize=1):
        with open(filename, "rb") as f:
            while True:
                chunk = f.read(chunksize)
                if chunk:
                    for b in chunk:
                        yield b
                else:
                    break


    parser = argparse.ArgumentParser(
        description="Detokenize calculator programs")

    parser.add_argument(
        '-xml', 
        help="XML file containing tokens.", 
        default="/usr/share/dt8xp/tokens/AxeTokens.xml")

    parser.add_argument('filename', help="Input .8xp file.")
    args = parser.parse_args()

    data = list(bytes_from_file(args.filename, chunksize = 1))[HEADER_LEN:-CRC_LEN]
    detokenize(data, args.xml)
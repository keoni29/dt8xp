""" Detokenize 8xp program files for ti8x calculators. """

import xml.etree.ElementTree as ET
import ti83f
import sys


def find_token(element, token):
    """ Find a token in the xml file.
    :param element: Search for tokens in this Elementtree element. 
    :param token: Token byte to search for
    :type element: Element
    :type token: int
    :return: Child element which matches the token byte.
    :rtype: Element"""
    children = element.findall('{http://merthsoft.com/Tokens}Token')

    if children:
        for child in children:
            byte = int(child.get('byte')[1:], base=16)
            
            if byte == token:
                return child
    return None


def _detokenize(element, data, offset):
    """ Detokenize sequence of bytes recursively.
    :param element: The Elementtree element to use for detokenization.
    :param data: Reference to bytes
    :param offset: Offset points to byte in data to be detokenized.
    :type element: Element
    :type data: bytes
    :type offset: int
    :return: new value for offset or None when the token could not be found
    :rtype: int """
    if offset >= len(data):
        return None

    child = find_token(element, data[offset])
    if child is not None:
        result = _detokenize(child, data, offset + 1)

        if result is not None:
            return result
        
        string = child.get('string')
        if string == '\\n':
            string = '\n:'
        print(string, end='')
        return offset + 1
    return None


def detokenize(data, xml_path):
    """ Detokenize bytes using xml token file.
    :param data: Bytes to be detokenized.
    :param xml_path: Path to xml token file.
    :type data: bytes
    :type xml_path: str
    :return: variables found in the appvar file
    :rtype: ti83f.Variable """
    tree = ET.parse(xml_path)
    root = tree.getroot()
    i = 0
    print(':', end='')
    while i < len(data):
        i = _detokenize(root, data, i)


def get_user_args():
    """ Get user arguments using argparse.
    :return: args """
    import argparse
    import os


    basedir = os.path.abspath(os.path.dirname(__file__))
    prefix = basedir + '/tokens/'
    file_ext = '.xml'
    tokenfilename = {
        'basic':'NoLib',
        'axe':'AxeTokens', 
        'grammer':'GrammerTokens',
        'ti84pcse':'TI-84+CSE',
        'ti82':'TI-82',
        'ti73':'TI-73'
        }
    libraries = list(tokenfilename.keys())
    default_lib = libraries[0]

    
    # Commandline options
    parser = argparse.ArgumentParser(
        description="Detokenize calculator programs")
    parser.add_argument(
        '--xml', 
        help="Custom XML file containing tokens.")
    parser.add_argument(
        '-l',
        '--lib',
        help="Select a library.",
        choices=libraries,
        default=default_lib
    )
    parser.add_argument('filename', help="Input .8xp file.")
    args = parser.parse_args()


    if args.xml is None:
        args.xml = prefix + tokenfilename[args.lib] + file_ext

    return args


def main():
    args = get_user_args()
    variables = ti83f.variables_from_file(args.filename)
    n = len(variables)
    if n == 0:
        print("Appvar does not contain variables.", file=sys.stderr)
        sys.exit()
    elif n > 1:
        print("Appvar contains", n, "variables.", file=sys.stderr)

    for variable in variables:
        print(variable.get_type(), end='')
        print(':' + variable.get_name(), end='')
        if variable.is_archived():
            print('(Archived)', end='')
        print()
        if variable.is_program():
            detokenize(variable.get_data(), args.xml)
        else:
            print("Cannot display variable.", file=sys.stderr)
        print()


if __name__ == "__main__":
    main()
    
from cStringIO import StringIO
from sys import argv

from compress_huffman import compress_huffman
from compress_not_huffman import compress_not_huffman
from compress_simple import compress_simple


FUNCTIONS = {
    'huffman': compress_huffman,
    'not_huffman': compress_not_huffman,
    'simple': compress_simple,
}


def main():
    input_text, output_filename, compression_function = process_command_input()
    string_of_binary_digits = compression_function(input_text)
    write_binary_string_to_file(string_of_binary_digits, output_filename)


def process_command_input():
    """Process arguments from the command line and return the needed ones."""
    if len(argv) < 4:
        print 'Usage: python compress.py algorithm input_file output_file'
        return

    algorithm = argv[1]
    input_filename = argv[2]
    output_filename = argv[3]

    input_text = open(input_filename, 'r').read()
    compression_function = FUNCTIONS.get(algorithm)
    if not compression_function:
        print 'Available functions are', ', '.join(FUNCTIONS.keys())
        return

    return input_text, output_filename, compression_function


def write_binary_string_to_file(string_of_binary_digits, output_filename):
    """Take a `str` of ones and zeroes, and write them to a file as binary."""
    binary_string_stream = StringIO(string_of_binary_digits)
    with open(output_filename, 'wb') as f:
        while True:
            b = binary_string_stream.read(8)
            if not b:
                break
            # If we got fewer than 8 bits, pad with zeroes on the right
            if len(b) < 8:
                b = b + '0' * (8 - len(b))
            character = chr(int(b, 2))
            f.write(character)


if __name__ == '__main__':
    main()

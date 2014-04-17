from math import log, ceil


def compress_simple(text):
    """Compress the text, and return a string of binary digits.

    Compression consists of using the least amount of bits to represent all
    characters.

    For example, compressing the string 'abcba' requires 3 values, so we would
    need 2 bits per character.
    The mapping we generate could be: {'a': '00', 'b': 01, 'c': 10}

    In this case the compressed file would read:
    `00 01 10 01 00`
    (But without the spaces)

    """
    mapping = _create_mapping(text)
    bits_per_letter = _get_amount_binary_digits_required(len(mapping))
    output = []
    for letter in text:
        encoded = _pad_to_max_length(mapping[letter], bits_per_letter)
        output.append(encoded)
    return ''.join(output)


def _create_mapping(text):
    """Create a mapping of characters to binary codes."""
    chars = list(set(text))
    return dict(zip(chars,
        [str(bin(chars.index(letter))).replace('0b', '') for letter in chars]))


def _get_amount_binary_digits_required(number):
    """how many binary digits are required to represent the `number`?"""
    return int(ceil(log(number, 2)))


def _pad_to_max_length(binary_number, required_length):
    """Add leading zeroes to binary_number to match the required_length."""
    number_digits_to_add = required_length - len(binary_number)
    return '0' * number_digits_to_add + binary_number

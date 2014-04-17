from collections import defaultdict


def compress_not_huffman(text):
    """Compress the text, and return a binary representation.

    Uses what I thought was Huffman Codes for compression.

    For example, compressing the string 'aaaaaaaabcba' would work as follows:
    We generate a mapping {'a': '1', 'b': '01', 'c': '001'}, making the most
    used characters have the shortest code.

    In this case the compressed file would read:
    `1 1 1 1 1 1 1 1 01 001 01 1`
    (But without the spaces)

    """
    mapping = _create_mapping(text)
    output = []
    for letter in text:
        output.append(mapping[letter])
    return ''.join(output)


def _create_mapping(text):
    """Create mapping of chars to binary codes based on frequency."""
    chars = get_chars_in_order_of_frequency(text)
    return dict(zip(chars, ['0'* i + '1' for i in xrange(len(chars))]))


def get_chars_in_order_of_frequency(text):
    """Get the chars in the `text` ordered by their frequency, descending."""
    def get_letter_frequencies(text):
        """Make dictionary of chars mapped to their frequency of use."""
        frequencies = defaultdict(float)
        text_length = len(text)

        for letter in text:
            frequencies[letter] += 1.0 / text_length

        return dict(frequencies)

    frequencies = get_letter_frequencies(text)
    chars = frequencies.keys()
    sorted_chars = sorted(chars, key=frequencies.get, reverse=True)

    return sorted_chars

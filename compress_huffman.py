from Queue import Queue
import sys

from compress_not_huffman import get_chars_in_order_of_frequency
# from tree import Tree


def compress_huffman(text):
    """Compress text using Huffman Coding.

    https://en.wikipedia.org/wiki/Huffman_code

    """
    mapping = _create_mapping(text)
    output = []
    for letter in text:
        output.append(mapping[letter])
    return ''.join(output)

def _create_mapping(text):
    """Create mapping of chars to binary codes using Huffman Coding algo."""
    def _print_excuse():
        print '\n'.join([
            'Your file contains 1 unique character.',
            'It would certainly compress well, but I refuse to do it.',
            'Write this down or something:',
            '$ echo "$(head -c 1 FILENAME) * $(wc -c < FILENAME)"',
        ])

    def _create_tree(chars):
        """Create hierarchical representation of nodes based on frequency."""
        queue = Queue(maxsize=len(chars))
        for char in reversed(chars):
            queue.put(char)

        while queue.qsize() > 1:
            e1 = queue.get_nowait()
            e2 = queue.get_nowait()
            queue.put([e1, e2])

        root = queue.get_nowait()
        return root

    def _descend_tree(tree, mutable_map, prefix=''):
        """Recursively build our mutable_map of code mappings."""
        new_codes = prefix + '0', prefix + '1'
        for element, new_code in zip(tree, new_codes):
            if isinstance(element, str):
                mutable_map[element] = new_code
            else:
                _descend_tree(element, mutable_map, prefix=new_code)

    chars = get_chars_in_order_of_frequency(text)
    if len(chars) < 2:
        _print_excuse()
        sys.exit(1)

    tree = _create_tree(chars)
    # Mutating your arguments is lame, but I can't think of a good way to do
    # this at the moment.
    mapping = {}
    _descend_tree(tree, mapping)
    return mapping

Compress
========

Implements a couple compression techniques

## Running

```
$ chmod +x run
$ ./run
```

The output you see is in the format:
```
compression_type input_file_number compression_ratio (lower is better)
```


## Input files

The input files are the first few thousand lines of the works of Shakespeare,
with certain characters stripped out.

 * `sample_text1.txt` includes everything.
 * `sample_text2.txt` excludes numbers and characters.
 * `sample_text3.txt` excludes numbers, characters, capitals and some lowercase.
 * `sample_text4.txt` is me holding down the `a` key, mostly.

They were generated in the following way:

Input file number 1 means the input file used is `sample_text1.txt`.

```
sed 's/[01234567890"_-!@#$%^&*()=+~<>/]//g' sample_text.txt > sample_text2.txt
sed 's/[ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefg01234567890"_-!@#$%^&*()=+~<>/]//g' sample_text.txt > sample_text3.txt
```

(I am doing this offline, and can't remember the regular expression [:alnum]
syntax.)

To see the unique letter counts in each file, we can do
```
$ python -c "print len(set((c for c in open('sample_text.txt', 'r').read())))"
89
$ python -c "print len(set((c for c in open('sample_text2.txt', 'r').read())))"
61
$ python -c "print len(set((c for c in open('sample_text3.txt', 'r').read())))"
35
$ python -c "print len(set((c for c in open('sample_text4.txt', 'r').read())))"
7
```

`sample_text2.txt` requires 6 bits per letter for the simple algorithm.
`sample_text3.txt` requires 5 bits per letter for the simple algorithm.


## Results

Here is what you see after a `./run`:

```
simple 1 .87
huffman 1 .75
not_huffman 1 1.33

simple 2 .75
huffman 2 .70
not_huffman 2 1.24

simple 3 .62
huffman 3 .55
not_huffman 3 .71

simple 4 .39
huffman 4 .29
not_huffman 4 .19

```

Again, the output you see is in the format:

```
compression_type input_file_number compression_ratio (lower is better)
```

Huffman beats my made up algorithms (surprise) in real world tests, but in the
some extreme cases, it can lose.

Fewer unique characters means better compression.  (surprise again!)

It would be interesting to try to figure out what conditions are required for
the not_huffman algorithm to beat Huffman Codes.  I imagine it would be a
combination of unique characters, filesize, and entropy.


## Where are the decompression functions?

There really should be some, if only to verify that the compression is working
the way I intend it to, and to get a truer measure of compression ratio (since
decompression would require storing additional data, like the character
mapping, in the compressed file.  But as this is meant only as me satisfying a
curiosity, they don't yet exist.  If I don't lose interest, they will be added.

# Markov Chain Text Generator

Takes text from a file and generates some random (but readable) text from it using a Markov chain. Bigger input text is recommended for more interesting results. Comes with an example input file that combines The Hobbit with Fifty Shades of Grey.


### Options

- `-f  --file (required): Name of file to read text from.`
- `-o  --order: Number of past states each state depends on. The lower the order, the greater the randomness. The higher the order, the closer the output text will match the input text.`
- `-w  --words: Number of words to generate.`

### Example usage

To generate 500 words from text in `example-input` with a Markov chain of order 1:

`python textgen.py -f example-input -o 1 -w 500`

### Example output

`...but how Gandalf got there, with all his wet hole, and filled with velvety soft, organic bamboo viscose that you mean about them, when Bilbo (who had got quite uncomfortable dreams...`

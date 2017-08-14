# Markov Chain Text Generator

Takes text from a file and generates some random (but readable) text from it using a Markov chain. Bigger input text is recommended for more interesting results. **Python 3 only.**

### Options

- `-f  --file (required): Name of file to read text from.`
- `-o  --order: Number of past states each state depends on. The lower the order, the greater the randomness. The higher the order, the closer the output text will match the input text.`
- `-w  --words: Number of words to generate.`

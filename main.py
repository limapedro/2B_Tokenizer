class BytePairTokenizer:
    def __init__(self):
        self.byte_pairs = self._generate_byte_pairs()

    def _generate_byte_pairs(self):
        # Generate all possible byte pairs
        byte_pairs = {}
        for i in range(256):
            for j in range(256):
                byte_pairs[(i, j)] = len(byte_pairs)
        return byte_pairs

    def encode(self, data):
        # Ensure the data is in bytes
        if isinstance(data, str):
            data = data.encode('utf-8')

        # Convert the data into byte pairs
        tokens = []
        for i in range(0, len(data), 2):
            pair = (data[i], data[i + 1]) if i + 1 < len(data) else (data[i], 0)
            tokens.append(self.byte_pairs[pair])
        return tokens

    def decode(self, tokens):
        # Convert tokens back to bytes
        byte_data = bytearray()
        inv_byte_pairs = {v: k for k, v in self.byte_pairs.items()}
        for token in tokens:
            byte_data.extend(inv_byte_pairs[token])
        return byte_data.decode('utf-8', errors='ignore')

# Example usage
tokenizer = BytePairTokenizer()

# Example input (binary data)
input_data = "I will meet you amanhã para um café!"
encoded_tokens = tokenizer.encode(input_data)
print(f"Encoded Tokens: {encoded_tokens}")

decoded_data = tokenizer.decode(encoded_tokens)
print(f"Decoded Data: {decoded_data}")

print(f"Bytes/tokns: {len(input_data) / len(encoded_tokens)}")
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
input_data = """
On a bright and sunny 日 (rì), as the breeze gently whispered through the 桜の木 (sakura no ki) and 桃花 (táohuā) trees,
 Maria and Hiroshi decided to enjoy a leisurely brunch at the café on the corner where they sipped their カプチーノ
   (kapuchīno) and discussed the latest trends in 技术 (jìshù) and ファッション (fasshon), while admiring the beautiful
     风景 (fēngjǐng) and 風光 (fēngguāng), dreaming of future adventures in distant ところ (tokoro) and 远方 (yuǎnfāng), 
     knowing that life’s simple pleasures, like a freshly baked クロワッサン (kurowassan) or a warm bowl of 拉面 (lāmiàn), 
     truly make the world a more 美しい (utsukushī) and 和谐 (héxié) place to live.
"""
encoded_tokens = tokenizer.encode(input_data)
print(f"Encoded Tokens: {encoded_tokens}")

decoded_data = tokenizer.decode(encoded_tokens)
print(f"Decoded Data: {decoded_data}")

print(f"Bytes/tokns: {len(input_data) / len(encoded_tokens)}")
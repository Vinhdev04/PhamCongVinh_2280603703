class PlayFairCipher:
    def __init__(self):
        self.matrix = []

    def create_playfair_key(self, key):
        key = key.replace("J", "I").upper()
        key = ''.join(sorted(set(key), key=lambda x: key.index(x)))  # Giữ thứ tự, loại trùng
        alphabet = "ABCDEFGHIKLMNOPQRSTUVWXYZ"

        for ch in alphabet:
            if ch not in key:
                key += ch

        self.matrix = [list(key[i:i+5]) for i in range(0, 25, 5)]
        return self.matrix

    def find_letter_coords(self, letter):
        for row in range(5):
            for col in range(5):
                if self.matrix[row][col] == letter:
                    return row, col
        return None

    def prepare_text(self, text):
        text = text.replace(" ", "")             # Bỏ khoảng trắng
        text = text.replace("J", "I").upper()
        result = ""
        i = 0
        while i < len(text):
            a = text[i]
            b = ""
            if i + 1 < len(text):
                b = text[i + 1]
                if a == b:
                    b = "X"
                    i += 1
                else:
                    i += 2
            else:
                b = "X"
                i += 1
            result += a + b
        return result

    def playfair_encrypt(self, plain_text):
        plain_text = self.prepare_text(plain_text)
        cipher_text = ""

        for i in range(0, len(plain_text), 2):
            a, b = plain_text[i], plain_text[i+1]
            row1, col1 = self.find_letter_coords(a)
            row2, col2 = self.find_letter_coords(b)

            if row1 == row2:
                cipher_text += self.matrix[row1][(col1 + 1) % 5]
                cipher_text += self.matrix[row2][(col2 + 1) % 5]
            elif col1 == col2:
                cipher_text += self.matrix[(row1 + 1) % 5][col1]
                cipher_text += self.matrix[(row2 + 1) % 5][col2]
            else:
                cipher_text += self.matrix[row1][col2]
                cipher_text += self.matrix[row2][col1]
        return cipher_text

    def playfair_decrypt(self, cipher_text):
        decrypted_text = ""

        for i in range(0, len(cipher_text), 2):
            a, b = cipher_text[i], cipher_text[i+1]
            row1, col1 = self.find_letter_coords(a)
            row2, col2 = self.find_letter_coords(b)

            if row1 == row2:
                decrypted_text += self.matrix[row1][(col1 - 1) % 5]
                decrypted_text += self.matrix[row2][(col2 - 1) % 5]
            elif col1 == col2:
                decrypted_text += self.matrix[(row1 - 1) % 5][col1]
                decrypted_text += self.matrix[(row2 - 1) % 5][col2]
            else:
                decrypted_text += self.matrix[row1][col2]
                decrypted_text += self.matrix[row2][col1]

        return self._clean_decrypted_text(decrypted_text)

    def _clean_decrypted_text(self, text):
        cleaned = ""
        i = 0
        while i < len(text):
            cleaned += text[i]
            if i + 2 < len(text) and text[i] == text[i + 2] and text[i + 1] == 'X':
                i += 2
            else:
                i += 1
        if cleaned.endswith('X'):
            cleaned = cleaned[:-1]
        return cleaned

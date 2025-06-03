# Import bảng chữ cái từ module khác: ALPHABET = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
from cipher.caesar import ALPHABET

# Định nghĩa lớp CaesarCipher để mã hóa và giải mã bằng thuật toán Caesar
class CaesarCipher:
    def __init__(self):
        self.upper_alphabet = ALPHABET  # Bảng chữ cái in hoa (A-Z)
        self.lower_alphabet = [char.lower() for char in ALPHABET]  # Tạo bảng chữ cái in thường (a-z)
    def encrypt_text(self, text: str, key: int) -> str:
        encrypted_text = []  # Danh sách để chứa các ký tự mã hóa
        alphabet_len = len(self.upper_alphabet)  # Độ dài bảng chữ cái (26 ký tự)

        # Duyệt qua từng ký tự trong văn bản đầu vào
        for letter in text:
            # Nếu là chữ in hoa
            if letter in self.upper_alphabet:
                index = self.upper_alphabet.index(letter)  # Tìm vị trí của ký tự trong bảng A-Z
                new_index = (index + key) % alphabet_len   # Dịch sang phải theo key, quay vòng nếu vượt quá Z
                encrypted_text.append(self.upper_alphabet[new_index])  # Thêm ký tự đã mã hóa vào kết quả

            # Nếu là chữ in thường
            elif letter in self.lower_alphabet:
                index = self.lower_alphabet.index(letter)  # Tìm vị trí trong bảng a-z
                new_index = (index + key) % alphabet_len   # Dịch sang phải theo key
                encrypted_text.append(self.lower_alphabet[new_index])

            # Nếu là khoảng trắng, số, hoặc ký tự đặc biệt → giữ nguyên
            else:
                encrypted_text.append(letter)

        return ''.join(encrypted_text)  # Ghép danh sách thành chuỗi và trả về
    def decrypt_text(self, text: str, key: int) -> str:
        decrypted_text = []  # Danh sách chứa kết quả giải mã
        alphabet_len = len(self.upper_alphabet)

        for letter in text:
            # Nếu là chữ in hoa
            if letter in self.upper_alphabet:
                index = self.upper_alphabet.index(letter)
                new_index = (index - key) % alphabet_len  # Dịch lùi theo key, quay vòng nếu nhỏ hơn A
                decrypted_text.append(self.upper_alphabet[new_index])

            # Nếu là chữ in thường
            elif letter in self.lower_alphabet:
                index = self.lower_alphabet.index(letter)
                new_index = (index - key) % alphabet_len
                decrypted_text.append(self.lower_alphabet[new_index])

            # Nếu là ký tự khác → giữ nguyên
            else:
                decrypted_text.append(letter)

        return ''.join(decrypted_text)

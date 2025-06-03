# Định nghĩa lớp VigenereCipher để mã hóa và giải mã theo thuật toán Vigenère
class VigenereCipher:
    def __init__(self):
        pass  # Hàm khởi tạo không cần thực hiện gì trong trường hợp này

    # Phương thức mã hóa văn bản (plain_text) bằng khóa (key)
    def vigenere_encrypt(self, plain_text, key):
        encrypted_text = ""     # Chuỗi kết quả sau khi mã hóa
        key_index = 0           # Vị trí hiện tại trong key (dùng để lặp qua key lặp lại)

        # Duyệt từng ký tự trong văn bản đầu vào
        for char in plain_text:
            if char.isalpha():  # Nếu là ký tự chữ cái (bỏ qua số, dấu câu, khoảng trắng)
                # Tính độ dịch (key_shift) từ ký tự tương ứng trong key (dù key viết thường hay hoa)
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                # Nếu là chữ in hoa (A-Z)
                if char.isupper():
                    # Dịch ký tự theo công thức Vigenère và thêm vào chuỗi kết quả
                    encrypted_text += chr((ord(char) - ord('A') + key_shift) % 26 + ord('A'))
                else:  # Nếu là chữ thường (a-z)
                    encrypted_text += chr((ord(char) - ord('a') + key_shift) % 26 + ord('a'))

                key_index += 1  # Di chuyển sang ký tự tiếp theo của key (vòng lặp key)
            else:
                # Nếu không phải chữ cái thì giữ nguyên (ví dụ: khoảng trắng, dấu chấm...)
                encrypted_text += char

        return encrypted_text  # Trả về chuỗi đã mã hóa
    # Phương thức giải mã văn bản đã mã hóa (encrypted_text) với cùng key
    def vigenere_decrypt(self, encrypted_text, key):
        decrypted_text = ""     # Chuỗi kết quả sau khi giải mã
        key_index = 0           # Vị trí hiện tại trong key

        # Duyệt qua từng ký tự trong văn bản mã hóa
        for char in encrypted_text:
            if char.isalpha():  # Xử lý nếu là chữ cái
                key_shift = ord(key[key_index % len(key)].upper()) - ord('A')

                if char.isupper():
                    # Dịch ngược lại theo công thức giải mã Vigenère cho chữ in hoa
                    decrypted_text += chr((ord(char) - ord('A') - key_shift) % 26 + ord('A'))
                else:
                    # Dịch ngược lại cho chữ thường
                    decrypted_text += chr((ord(char) - ord('a') - key_shift) % 26 + ord('a'))

                key_index += 1  # Di chuyển qua ký tự tiếp theo của key
            else:
                # Nếu không phải chữ cái thì giữ nguyên
                decrypted_text += char

        return decrypted_text  # Trả về văn bản đã giải mã

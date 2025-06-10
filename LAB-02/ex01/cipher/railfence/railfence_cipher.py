class RailFenceCipher:
    def __init__(self):
        pass

    def rail_fence_encrypt(self, plain_text, num_rails):
        if num_rails < 2:
            return plain_text

        rails = [[] for _ in range(num_rails)]
        rails_index = 0
        direction = 1

        for char in plain_text:
            rails[rails_index].append(char)
            if rails_index == 0:
                direction = 1
            elif rails_index == num_rails - 1:
                direction = -1
            rails_index += direction

        cipher_text = ''.join([''.join(rail) for rail in rails])
        return cipher_text

    def rail_fence_decrypt(self, cipher_text, num_rails):
        if num_rails < 2:
            return cipher_text

        # Tính độ dài từng rail
        rail_lengths = [0] * num_rails
        rails_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            rail_lengths[rails_index] += 1
            if rails_index == 0:
                direction = 1
            elif rails_index == num_rails - 1:
                direction = -1
            rails_index += direction

        # Tạo từng rail với độ dài tương ứng
        rails = []
        start = 0
        for length in rail_lengths:
            rails.append(list(cipher_text[start:start + length]))
            start += length

        # Đọc từng ký tự theo mô hình zig-zag
        plain_text = ""
        rails_index = 0
        direction = 1

        for _ in range(len(cipher_text)):
            plain_text += rails[rails_index].pop(0)
            if rails_index == 0:
                direction = 1
            elif rails_index == num_rails - 1:
                direction = -1
            rails_index += direction

        return plain_text

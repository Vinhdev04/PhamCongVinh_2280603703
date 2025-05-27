import sys
import os
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), 'ex01')))
from flask import Flask, render_template, request, jsonify

from cipher.caesar.caesar_cipher import CaesarCipher
from cipher.vigenere.vigenere_cipher import VigenereCipher
from cipher.playfair.playfair_cipher import PlayFairCipher
from cipher.railfence.railfence_cipher import RailFenceCipher
from cipher.transposition.transposition_cipher import TranspositionCipher

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/caesar')
def caesar():
    return render_template('caesar.html')

@app.route('/encrypt', methods=['POST'])
def caesar_encrypt():
    data = request.get_json()
    text = data['inputPlainText']
    key = int(data['inputKeyPlain'])
    caesar = CaesarCipher()
    encrypted_text = caesar.encrypt_text(text, key)
    return jsonify({"encrypted": encrypted_text})

@app.route('/decrypt', methods=['POST'])
def caesar_decrypt():
    data = request.get_json()
    text = data['inputCipherText']
    key = int(data['inputKeyCipher'])
    caesar = CaesarCipher()
    decrypted_text = caesar.decrypt_text(text, key)
    return jsonify({"decrypted": decrypted_text})

@app.route('/vigenere')
def vigenere_page():
    return render_template('vigenere.html')

@app.route('/vigenere/encrypt', methods=['POST'])
def vigenere_encrypt():
    data = request.get_json()
    text = data['inputPlainText']
    key = data['inputKeyPlain']
    cipher = VigenereCipher()
    encrypted_text = cipher.vigenere_encrypt(text, key)
    return jsonify({"encrypted": encrypted_text})

@app.route('/vigenere/decrypt', methods=['POST'])
def vigenere_decrypt():
    data = request.get_json()
    text = data['inputCipherText']
    key = data['inputKeyCipher']
    cipher = VigenereCipher()
    decrypted_text = cipher.vigenere_decrypt(text, key)
    return jsonify({"decrypted": decrypted_text})

@app.route('/playfair')
def playfair_page():
    return render_template('playfair.html')

@app.route('/playfair/encrypt', methods=['POST'])
def playfair_encrypt():
    data = request.get_json()
    text = data['inputPlainText']
    key = data['inputKeyPlain']
    cipher = PlayFairCipher()
    cipher.create_playfair_key(key)
    encrypted_text = cipher.playfair_encrypt(text)
    return jsonify({"encrypted": encrypted_text})

@app.route('/playfair/decrypt', methods=['POST'])
def playfair_decrypt():
    data = request.get_json()
    text = data['inputCipherText']
    key = data['inputKeyCipher']
    cipher = PlayFairCipher()
    cipher.create_playfair_key(key)
    decrypted_text = cipher.playfair_decrypt(text)
    return jsonify({"decrypted": decrypted_text})

@app.route('/railfence')
def railfence_page():
    return render_template('railfence.html')

@app.route('/railfence/encrypt', methods=['POST'])
def railfence_encrypt():
    data = request.get_json()
    text = data['inputPlainText']
    key = int(data['inputKeyPlain'])
    cipher = RailFenceCipher()
    encrypted_text = cipher.rail_fence_encrypt(text, key)
    return jsonify({"encrypted": encrypted_text})

@app.route('/railfence/decrypt', methods=['POST'])
def railfence_decrypt():
    data = request.get_json()
    text = data['inputCipherText']
    key = int(data['inputKeyCipher'])
    cipher = RailFenceCipher()
    decrypted_text = cipher.rail_fence_decrypt(text, key)
    return jsonify({"decrypted": decrypted_text})

@app.route('/transposition')
def transposition_page():
    return render_template('transposition.html')

@app.route('/transposition/encrypt', methods=['POST'])
def transposition_encrypt():
    data = request.get_json()
    text = data['inputPlainText']
    key = int(data['inputKeyPlain'])
    cipher = TranspositionCipher()
    encrypted_text = cipher.encrypt(text, key)
    return jsonify({"encrypted": encrypted_text})

@app.route('/transposition/decrypt', methods=['POST'])
def transposition_decrypt():
    data = request.get_json()
    text = data['inputCipherText']
    key = int(data['inputKeyCipher'])
    cipher = TranspositionCipher()
    decrypted_text = cipher.decrypt(text, key)
    return jsonify({"decrypted": decrypted_text})

if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
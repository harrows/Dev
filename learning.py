class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        # с учетом переданного смещения shift.
        result = []
        for letter in original_text:
            if letter.lower() not in self.alphabet:
                result.append(letter)
            else:
                tmp_index = self.alphabet.index(letter.lower()) + shift
                if tmp_index >= len(self.alphabet):
                    tmp_index -= len(self.alphabet)
                result.append(self.alphabet[tmp_index])
                      
        
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        for letter in cipher_text:
            if letter.lower() not in self.alphabet:
                result.append(letter)
            else:
                tmp_index = self.alphabet.index(letter.lower()) + shift
                if tmp_index < 0:
                    tmp_index += len(self.alphabet)
                result.append(self.alphabet[tmp_index])
        return ''.join(result)


cipher_master = CipherMaster()
print(cipher_master.cipher(
    original_text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2
))
print(cipher_master.decipher(
    cipher_text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3
))



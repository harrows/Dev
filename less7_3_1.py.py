class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def cipher(self, original_text, shift):
        # Метод должен возвращать зашифрованный текст
        result = []
        for letter in original_text:
            if letter.lower() not in CipherMaster.alphabet:
                result.append(letter)
            else:
                tmp_index = CipherMaster.alphabet.index(letter.lower()) + shift
                
                # Зацикливание индекса вперед
                if tmp_index >= len(CipherMaster.alphabet):
                    tmp_index -= len(CipherMaster.alphabet)
                # Зацикливание индекса назад
                elif tmp_index < 0:
                    tmp_index += len(CipherMaster.alphabet)
                
                result.append(CipherMaster.alphabet[tmp_index])
        return ''.join(result)

    def decipher(self, cipher_text, shift):
        # Метод должен возвращать исходный текст
        # с учётом переданного смещения shift.
        result = []
        for letter in cipher_text:
            if letter.lower() not in CipherMaster.alphabet:
                result.append(letter)
            else:
                tmp_index = CipherMaster.alphabet.index(letter.lower()) - shift
                
                # Зацикливание индекса вперед
                if tmp_index >= len(CipherMaster.alphabet):
                    tmp_index -= len(CipherMaster.alphabet)
                elif tmp_index < 0:
                    tmp_index += len(CipherMaster.alphabet)
                
                result.append(CipherMaster.alphabet[tmp_index])
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
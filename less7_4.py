class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []
        for letter in text:
            if letter.lower() not in self.alphabet:
                result.append(letter)
            else:
                if is_encrypt:
                    tmp_index = (self.alphabet.index(letter.lower()) + shift) % len(self.alphabet)
                    result.append(self.alphabet[tmp_index])
                elif not is_encrypt:
                    tmp_index = (self.alphabet.index(letter.lower()) - shift) % len(self.alphabet)
                    result.append(self.alphabet[tmp_index])
        return ''.join(result)

cipher_master = CipherMaster()
print(cipher_master.process_text(
    text='Однажды ревьюер принял проект с первого раза, с тех пор я его боюсь',
    shift=2,
    is_encrypt=True
))
print(cipher_master.process_text(
    text='Олебэи яфвнэ мроплж сэжи — э пэй рдв злййвкпш лп нвящывнэ',
    shift=-3,
    is_encrypt=False
)) 


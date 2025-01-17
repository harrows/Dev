class CipherMaster:
    # Не изменяйте и не перемещайте эту переменную
    alphabet = 'абвгдеёжзийклмнопрстуфхцчшщъыьэюя'

    def process_text(self, text, shift, is_encrypt):
        result = []

        # if not is_encrypt:
        shift = -shift if not is_encrypt else shift

        for letter in text:
            if letter.lower() not in CipherMaster.alphabet:
                result.append(letter)
            else:
                tmp_index = CipherMaster.alphabet.index(letter.lower()) + shift
                
                if tmp_index >= len(CipherMaster.alphabet):
                    tmp_index -= len(CipherMaster.alphabet)
                elif tmp_index < 0:
                    tmp_index += len(CipherMaster.alphabet)
                
                result.append(CipherMaster.alphabet[tmp_index])
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
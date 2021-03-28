import string
def casear(text,shift,alphabets):
    def shift_alphabet(alphabet):
        return alphabet[shift: ]+alphabet[ :shift]
    shifted_alphabets=tuple(map(shift_alphabet,alphabets))
    final_alphabet=' '.join(alphabets)
    final_shifted_alphabet=' '.join(shifted_alphabets)
    table=str.maketrans(final_alphabet,final_shifted_alphabet)
    return text.translate(table)

Plain_text=input("Enter  Message >>>>" )
print(casear(Plain_text,7,[string.ascii_lowercase,string.ascii_uppercase,string.punctuation]))
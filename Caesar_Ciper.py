print("Shri hari")
print("Caesar Ciper")
alphabet = ['a','b','c','d','e','f','g','h','i','j','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z']
choice = input("Enter 'e' for encrpt and 'd' for decrpt:  ").lower()
text = input("Enter the message: ")
shift_amt = int(input('enter the shift amt: ')) 
print(text) 
e_ciper_text = ""
if choice == 'e':
    for i in text:
        shift_pos = shift_amt%len(alphabet)
        c =  alphabet.index(i) + shift_pos
        e_ciper_text += alphabet[c]
print(f"encrpt: {e_ciper_text} ")
choice = input("Enter 'e' for encrpt and 'd' for decrpt:  ").lower()
d_ciper_text = ""
if choice == 'd':
    for i in e_ciper_text:
        shift_pos = shift_amt%len(alphabet)
        c = alphabet.index(i) - shift_pos 
        d_ciper_text += alphabet[c]
print(f"decrpt: {d_ciper_text}")

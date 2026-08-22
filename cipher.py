# Characters that can be shifted
key=list('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789')
text=input('Enter text:')

# Keep asking till user enters a  valid choice
while True:
    choice=input('Would u like to encode(1) or decode text(2):')
    if choice in ['1','2']:
        break
    else:
        print('Invalid input! Use ONLY 1 or 2.')
        print('*'*10)
        continue

# Keep asking till user input valid shift value
while True:
 shift=input('Enter shift value:')
 if shift.isdigit() and int(shift)>0:
     shift=int(shift)
     break
 else:
     print('Invalid input! Use ONLY positive integers.')
     print('*'*60)
     continue
# Encrypting/decrypting the chosen text
def secret(shifted_value):
 for letter in text:
  if letter in key:
   ind=key.index(letter)
   if choice=='1':
    shifted=key[(ind+shifted_value) %len(key)]
   elif choice=='2':
    shifted=key[(ind-shifted_value) %len(key)]   
   print(shifted,end='')
  else:
   print(letter,end='')
if choice=='1':
    print('Encrypted text is: ',end='')
else:
    print('Decrypted text is: ',end='')
secret(shift)
end=60*'~'
print('\n',end)
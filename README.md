Unreadable is an encode and a decoder.
### __Installation__ ###
```
pip install unreadable
```
### __Usage__ ###
#### unreadable.**encode**(string,key='generate')
*string: the string you want to encode*\
*key (Optional): the encode key (Can be made with generate_key, more on that later).*
```python
encoded_string = encode('An encoded string!')
```
Will output something like `ZXI5X@>*5*IP]0nX,-+AacsB_"|z}M7-YDxOCK&r^\fd50] 8n>UvH:P*=,hWk<6u;4@gNX?$GJVE(L%j[!R2)T.{Zm9Qe/pb1loiw#3FSyqt'I` without *key*.
#### unreadable.**decode**(string,key='generate')
*string: the encoded string you want to decode*\
*key (Optional): the key you used to encode the string (Not needed if you left key blank).*
```python
decoded_string = decode('ZXI5X@>*5*IP]0nX,-+AacsB_"|z}M7-YDxOCK&r^\fd50] 8n>UvH:P*=,hWk<6u;4@gNX?$GJVE(L%\[!R2)T.{Zm9Qe/pb1loiw#3FSyqt'+"'"+'I')
```
Will output `An encoded string!`
#### unreadable.**generate_key**(chars=r'1234567890-=!@#$%^&*()_qwertyuiop\[]asdfghjkl;'+"'"+r'zxcvbnm,./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? ')
*chars: The characters the encoder will encode (Otherwise it will just be the same charater ex. ÷ encoded will be ÷ unless it's in the chars.*
```python
key = generate_key()
encoded_string = encode('Encoded using a custom key!')
decoded_string = decode(encoded_string)
print(decoded_string)
```
Will output `Encoded using a custom key!`

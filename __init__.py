def encode(string,key='generate'):
	from random import sample,randint as r
	if key == 'generate':
		chars = r'1234567890-=!@#$%^&*()_qwertyuiop[]asdfghjkl;'+"'"+r'zxcvbnm,./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? '
		oc = chars
		for num in range(1,r(2,100)):
			chars = ''.join(sample(chars,len(chars)))
		#key ammount MUST be 92 characters
	else:
		chars = key
		oc1 = r'1234567890-=!@#$%^&*()_qwertyuiop[]asdfghjkl;'+"'"+r'zxcvbnm,./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? '
		oc = []
		for char in oc1:
			oc.append(char)
		for char in oc:
			if not char in key:
				oc.remove(char)
		oc = ''.join(oc)
	d = {}
	cnt = 0
	rc = ''
	cb = {}
	for char in chars:
		d[char] = oc[cnt]
		cnt += 1
	for char,rc in d.items():
		cb[rc] = char
	for char in string:
		try:
			rc += cb[char]
		except KeyError:
			rc += char
	strc = []
	for char in rc:
		strc.append(char)
	del strc[0]
	rc = ''
	for char in strc:
		rc += char
	if key == 'generate':
		rc+='+'+chars
	return rc
def decode(string,key='generate'):
	oc = r'1234567890-=!@#$%^&*()_qwertyuiop[]asdfghjkl;'+"'"+r'zxcvbnm,./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? '
	d = {}
	cnt = 0
	if key == 'generate':
		chars = string.split('+')[1]
	else:
		chars = key
		oc1 = r'1234567890-=!@#$%^&*()_qwertyuiop[]asdfghjkl;'+"'"+r'zxcvbnm,./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? '
		oc = []
		for char in oc1:
			oc.append(char)
		for char in oc:
			if not char in key:
				oc.remove(char)
		oc = ''.join(oc)
	string = string.split('+')[0]
	rc = ''
	for char in chars:
		d[char] = oc[cnt]
		cnt += 1
	for char in string:
		try:
			rc += d[char]
		except KeyError:
			rc += char
	return rc
def generate_key(chars=r'1234567890-=!@#$%^&*()_qwertyuiop[]asdfghjkl;'+"'"+r'zxcvbnm,./\|QWERTYUIOP{}ASDFGHJKL:"ZXCVBNM<>? '):
	from random import sample,randint as r
	for num in range(1,r(2,100)):
		chars = ''.join(sample(chars,len(chars)))
	return chars
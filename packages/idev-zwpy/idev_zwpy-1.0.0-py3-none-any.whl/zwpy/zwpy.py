#Imports
import argparse

from tqdm import tqdm
from PyTermColor.Color import printColor as printc






#Parser Declaration
zwpyParser = argparse.ArgumentParser(description="", formatter_class=argparse.ArgumentDefaultsHelpFormatter)
zwpySubParser = zwpyParser.add_subparsers(dest = 'action')

encodeParser = zwpySubParser.add_parser('encode', help = 'Will encode secret text into public text using zero-width characters.')
decodeParser = zwpySubParser.add_parser('decode', help = 'Will decode text to find a secret from zero-width characters.')
finderParser = zwpySubParser.add_parser('find', help = 'Will print out a boolean telling if zero-width characters are found in the text, flag exists to print out how many characters were found.')


encodeParser.add_argument('text', help = 'Text to be displayed publicly to the reader.')
encodeParser.add_argument('secret', help = 'Text to be encoded into zero-width characters and hidden in the public text.')
encodeParser.add_argument('-b', '--base', help = 'Specifies the base the secret is to be encoded in.', default = 'binary')
encodeParser.add_argument('-k', '--key', help = 'Specifies key to use for xor operation on the secret.')
encodeParser.add_argument('-o', '--output', help = 'Specifies the output file name, if not provided the output will be printed out.')
encodeParser.add_argument('-S', '--silent', help = 'Disabled progress bars.', action = 'store_true')

decodeParser.add_argument('text', help = 'Text that may contain zero-width characters.')
decodeParser.add_argument('-b', '--base', help = 'Specifies the base the secret is was encoded in.', default = 'binary')
decodeParser.add_argument('-k', '--key', help = 'Specifies key to use for xor operation on the secret.')
decodeParser.add_argument('-o', '--output', help = 'Specifies the output file name, if not provided the output will be printed out.')
decodeParser.add_argument('-S', '--silent', help = 'Disabled progress bars.')

finderParser.add_argument('text', help = 'Text that may contain zero-width characters.')
finderParser.add_argument('-c', '--count', help = 'Will specify to output how many zero-width characters were found.', action = 'store_true')






#Global Variables
ZWCharacters = ['\u200c','\u200d','\u2060','\ufeff']












#Extra Functions
def error(errorType: str, value: str):
    print('\n')
    printc(errorType, 'red', end = ': ')
    printc(value, 'lightyellow')
    quit()



def baseConvert(number: int, base: int) -> str:
    if number == 0: return '0'
    
    digits = []
    while number:
        digits.append(int(number % base))
        number //= base
    return ''.join([str(i) for i in digits[::-1]])



def expandKey(key: int, length: int, base: int) -> str:
    if key < 2: error('ValueError', 'Argument "key" must be greater than 2.')
    while len(baseConvert(key, base)) < length: key *= key
    return baseConvert(key, base)[0:length]



def testArgument(argument: str, value: str) -> bool:
    match argument:
        case 'base': return value in ('binary', 'trinary', 'quaternary')
        case 'key': return value.isdigit()
        case _: return True


def qua(number: int) -> str:
    return baseConvert(number, 4)



def tri(number: int) -> str:
    return baseConvert(number, 3)






#Encode Command Function
def Encode(Arguments: dict):
    global ZWCharacters
    text = Arguments['text']
    secret = list(Arguments['secret'])

    if not text: error('ValueError', 'No value provided for argument "text".')
    if not secret: error('ValueError', 'No value provided for argument "secret".')


    try:
        match Arguments['base']:
            case 'binary': 
                for i in tqdm(range(len(secret)), desc = 'Encoding Secret: ', disable = Arguments['silent']): secret[i] = bin(ord(secret[i]))[2:].zfill(16)
            case 'trinary': 
                for i in tqdm(range(len(secret)), desc = 'Encoding Secret: ', disable = Arguments['silent']): secret[i] = tri(ord(secret[i])).zfill(11)
            case 'quaternary':
                for i in tqdm(range(len(secret)), desc = 'Encoding Secret: ', disable = Arguments['silent']): secret[i] = qua(ord(secret[i])).zfill(8)
        secret = ''.join(secret)
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Encoding Secret.\n' + str(exception))


    try:
        if int(Arguments['key']):
            key = expandKey(Arguments['key'], len(secret), {'binary': 2, 'trinary': 3, 'quaternary': 4}[Arguments['base']])
            for i in tqdm(range(len(secret)), desc = 'Encrypting Information: ', disable = Arguments['silent']): secret[i] = int(secret[i]) ^ int(key[i])
        secret = ''.join([ZWCharacters[int(i)] for i in secret])
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Encrypt Information.\n' + str(exception))


    try:
        splitLength = max(int(round(len(secret) / len(text))), 1)
        splitSecret = []
        for i in tqdm(range(0, len(secret), splitLength), 'Splitting Secret: ', disable = Arguments['silent']): splitSecret.append(secret[i:i+splitLength])
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Split Secret.\n' + str(exception))


    try:
        text = list(text) + ['' for i in range(max(0, len(splitSecret) - len(text)))]
        splitSecret += [''  for i in range(max(0, len(text) - len(splitSecret)))]
        result = []
        for i in tqdm(range(len(text)), desc = 'Combining Text: ', disable = Arguments['silent']): result.append(text[i] + splitSecret[i])
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Combine Text.\n' + str(exception))


    print('\n')
    if Arguments['output']:
        try:
            with open(Arguments['output'], 'w+', errors = 'ignore', encoding = 'utf') as f: f.write(''.join(result))
        except KeyboardInterrupt: raise KeyboardInterrupt
        except Exception as exception: error('RuntimeError', 'Could not save output to file.\n' + str(exception))
        printc('Encoded Result Saved: ', 'green', end = '')
        print(Arguments['output'])
    
    else:
        printc('Encoded Result: ', 'green')
        print(''.join(result), end='(removethis)')










#Decode Command Function
def Decode(Arguments: dict):
    global ZWCharacters
    text = Arguments['text']

    if not text: error('ValueError', 'No value provided for argument "text".')


    secret = []
    try:
        for i in tqdm(range(len(text)), desc = 'Collecting Zero-Width Characters: '):
            if text[i] in ZWCharacters: secret.append(text[i])
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Collect Zero-Width Characters.\n' + str(exception))
    if len(secret) == 0: error('ValueError', 'No Zero-Width Characters found.')


    try:
        if int(Arguments['key']):
            key = expandKey(Arguments['key'], len(secret), {'binary': 2, 'trinary': 3, 'quaternary': 4}[Arguments['base']])
            for i in tqdm(range(len(secret)), desc = 'Encrypting Information: ', disable = Arguments['silent']): secret[i] = int(secret[i]) ^ int(key[i])
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Decrypt Information.\n' + str(exception))


    convertedSecret = []
    try:
        for i in tqdm(range(len(secret)), desc = 'Converting Secret: '):
            convertedSecret.append(str(ZWCharacters.index(secret[i])))
        fillAmount = {'binary' : 16, 'trinary' : 11, 'quaternary' : 8}[Arguments['base']]
        convertedSecret = [''.join(convertedSecret[i:i+fillAmount]) for i in range(0, len(convertedSecret), fillAmount)]
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Convert Secret.\n' + str(exception))


    decodedSecret = []
    try:
        base = {'binary' : 2, 'trinary' : 3, 'quaternary' : 4}[Arguments['base']]
        for i in tqdm(range(len(convertedSecret)), desc = 'Decoding Secret: '):
            decodedSecret.append(chr(int(convertedSecret[i], base)))
    except KeyboardInterrupt: raise KeyboardInterrupt
    except Exception as exception: error('RuntimeError', 'Could not Decode Secret.\n' + str(exception))
        

    print('\n')
    if Arguments['output']:
        try:
            with open(Arguments['output'], 'w+', errors = 'ignore', encoding = 'utf') as f: f.write(''.join(decodedSecret))
        except KeyboardInterrupt: raise KeyboardInterrupt
        except Exception as exception: error('RuntimeError', 'Could not save output to file.\n' + str(exception))
        printc('Decoded Result Saved: ', 'green', end = '')
        print(Arguments['output'])
    
    else:
        printc('Decoded Result: ', 'green')
        print(''.join(decodedSecret))






#Find Command Function
def Find(Arguments: dict):
    global ZWCharacters


    if Arguments['count']:
        if any([True for i in ZWCharacters if i in Arguments['text']]):
            count = len([i for i in Arguments['text'] if i in ZWCharacters])
            printc('True', 'green', end = '  ')
            print(f'({count})')
        
        else:
            printc('False', 'red')

    else:
        if any([True for i in ZWCharacters if i in Arguments['text']]): printc('True', 'green')
        else: printc('False', 'red')






#Main Function
def Main():
    Arguments = vars(zwpyParser.parse_args())

    for argument in Arguments:
        if 'key' in Arguments:
            if Arguments['key'] is None: Arguments['key'] = '0'
        if not testArgument(argument, Arguments[argument]): error('ValueError', f'Invalid value provided for argument "{argument}".')
    
    
    match Arguments['action']:
        case 'encode': Encode(Arguments)
        case 'decode': Decode(Arguments)
        case 'find': Find(Arguments)






if __name__ == '__main__': Main()
'''
Created Sun May 1 22 2022
@author: henry-israel

Improved enigame decoder that more effecively uses classes
'''
import numpy as np
from itertools import groupby

class TranslatorBase:
    '''
    Base class from which other translators will be built from
    '''

    def __init__(self, inputstr: str, delimiter: str=''):
        '''
        str : inputstr  ->  input string, to be translated
        str : delimiter -> delimter to separate words/numbers
        '''
        self._inputstr=inputstr
        self._delimiter=delimiter

        #Special cases so we can get a couple of different versions of the input
        #While inefficient it's probably useful to have these all defined here!

        #Upper case version of regular string        
        self._inputstr_allcaps=self._inputstr.upper()
        #Version of normal string with no delimiter
        self._input_no_delim=self._inputstr.replace(delimiter, '')
        #Upper case version of normal string with no delimiter
        self._input_no_delim_allcaps=self._input_no_delim.upper()

        #Version of the input where it's an array
        if delimiter=='':
            self._input_asarray=list(self._inputstr_allcaps)
        else:
            self._input_asarray=[str_i for str_i in self._inputstr_allcaps.split(delimiter)]
   
        self._inputgrid=[]

        self._ordered_asarray = sorted(self._input_asarray)
        self._letterfreq={key: len(list(group)) for key, group in groupby(self._ordered_asarray)}

        self._input_is_num=all([i.isdecimal() for i in self._input_asarray])

        self._alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N","O","P","Q","R","S","T","U","V","W","X","Y","Z", " "]

        self._keyboardalphabet=["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A", "S",
                           "D","F","G","H","J","K","L","Z","X","C","V","B","N","M", ' ']

        self._morse_code_dict={ 'A':'.-', 'B':'-...', 
                    'C':'-.-.', 'D':'-..', 'E':'.', 
                    'F':'..-.', 'G':'--.', 'H':'....', 
                    'I':'..', 'J':'.---', 'K':'-.-', 
                    'L':'.-..', 'M':'--', 'N':'-.', 
                    'O':'---', 'P':'.--.', 'Q':'--.-', 
                    'R':'.-.', 'S':'...', 'T':'-', 
                    'U':'..-', 'V':'...-', 'W':'.--', 
                    'X':'-..-', 'Y':'-.--', 'Z':'--..', 
                    '1':'.----', '2':'..---', '3':'...--', 
                    '4':'....-', '5':'.....', '6':'-....', 
                    '7':'--...', '8':'---..', '9':'----.', 
                    '0':'-----', ', ':'--..--', '.':'.-.-.-', 
                    '?':'..--..', '/':'-..-.', '-':'-....-', 
                    '(':'-.--.', ')':'-.--.-', ' ' : '/'} 

    @property
    def get_input_all_caps(self):
        return self._input_allcaps

    @property
    def get_input_no_delim(self):
        return self._input_no_delim_allcaps

    @property
    def get_input_as_grid(self):
        return self._inputgrid

    @property
    def get_char_freq(self):
        return self._letterfreq

    #Generic Stuff
    def convert_to_grid(self):
        '''
        Checks if you can convert input string to a grid
        '''
        sqrtarrsize=len(self._input_asarray)**0.5
        if sqrtarrsize==int(sqrtarrsize):
            print(f"Input has {len(self._input_asarray)} entries, can grid-ify!")
            self._inputgrid=np.array(self._input_asarray).reshape(int(sqrtarrsize), int(sqrtarrsize))
            return True
        else:
            print("Can't convert input to grid")
            return False


    #Numerical stuff
    def get_prime_factors(self):
        if self._input_is_num:
            return factorint(int(self._inputstr))
        else:
            return 0

    def convert_from_base_to_dec(self, base):
        return [int(i, base) for i in self._input_asarray]

    def convert_from_base_to_base(self, base1: int, base2: int):
        #convert from decimal to new base 
        if not self._input_is_num:
            return 0
        else:
            dec_arr = self.convert_from_base_to_dec(base1)
            return [self.change_dec_to_base(i) for i in dec_arr]
    
    def change_dec_to_base(self, instr, base):
        innum=int(instr)
        rem_arr=[]
        while innum>0:
            innum, rem=divmod(innum, base)
            rem_arr.append(rem)
        result=''.join(str(r) for r in rem_arr)
        return result


    def convert_num_to_let(self, inarr, base=10):
    #numerical array to array of letters!
        if not self._input_is_num:
            return 0
        else:
            num_arr=[self.change_dec_to_base(i, base) for i in inarr]
            num_arr.remove('')
            num_arr=np.array(num_arr[1:]).astype(int)
            if max(num_arr)>=27 or min(num_arr)<=0:
                return 0
            else:
                return [self._alphabet[i-1] for i in num_arr]

    def convert_let_to_num(self):
        nums=[str(i) for i in range(len(self._alphabet))]
        letnumdict=dict(zip(self._alphabet,nums))
        return [letnumdict[let_i] for let_i in self._input_asarray]

    def convert_from_ascii(self, inarr):
        if not self._input_is_num:
            return 0
        else:
            if int(max(inarr))<=256:
                return ''.join(chr(int(num)) for num in inarr)
            else:
                print("Max val greater than ascii!")
                return 0
    
    def convert_to_ascii(self, instr):
        return [ord(c) for c in instr]

    #Alphabetical
    def morse_to_eng(self):
        if not set(self._input_asarray).issubset(set(self._morse_code_dict.values())):
            print("Input not morse code")
            return 0
        else:
            return ''.join(rev_dict[i] for i in string_input.split())

    def convert_to_keyboardpos(self, inarr):
        if not set(inarr).issubset(self._alphabet):
            print("Input must just be letters")
            return 0
        else:
            transdict=dict(zip(self._alphabet, self._keyboardalphabet))
            return ''.join(transdict[i] for i in inarr)
    
    def convert_from_keyboardpos(self, inarr):
        if not set(inarr).issubset(self._alphabet):
            print("Input must just be letters")
            return 0
        else:
            transdict=dict(zip(self._keyboardalphabet, self._alphabet))
            return ''.join(transdict[i] for i in inarr)


    def get_max_digit(self):
        digarr=[]
        for str_i in self._input_asarray:
            for i in list(str_i):
                digarr.append(int(i))
        return max(digarr)

    def __call__(self, maxbase: int=10):
        isgrid=self.convert_to_grid()
        print(f"Examining {self._input_asarray}")
        if isgrid:
            print(f"input as grid is : ")
            for row in self._inputgrid:
                print(row)
        print(f"Character frequency is : {self._letterfreq}")

        alphabet_trans=self.convert_num_to_let(self._input_asarray, 10)

        dokb=False
        if alphabet_trans!=0:
            dokb=True
            print(f"Alphabetic (num->letter) is {alphabet_trans}")

            from_keyboard_trans=self.convert_to_keyboardpos(alphabet_trans)
            to_keyboard_trans=self.convert_from_keyboardpos(alphabet_trans)

        elif set(self._input_asarray).issubset(self._alphabet):
            dokb=True
            from_keyboard_trans=self.convert_to_keyboardpos(self._input_asarray)
            to_keyboard_trans=self.convert_from_keyboardpos(self._input_asarray)
            self._input_asarray=self.convert_let_to_num()
            self._input_is_num=True
            self._inputstr=''.join(i+' ' for i in self._input_asarray)
            print(f"Letter->Base 10 numerical value is : {self._input_asarray}")
        
        if dokb:
            print(f"Alphabet->Keyboard pos : {to_keyboard_trans}")
            print(f"Keyboard pos->Alphabet : {from_keyboard_trans}")

        ascii_trans=[self.convert_from_ascii(i) for i in self._input_asarray]
        if ascii_trans != 0:
            print(f"This is '{ascii_trans}' in ascii")

        if self._input_is_num:
            minbase=self.get_max_digit()+1
            
            print(f"Detected numerical result, converting from base {minbase}->{maxbase} to 10 and looking at ascii, binary etc.\n")


            #Numeric stuff
            for base_i in range(minbase, maxbase+1):
                print("------------------------------------------------------")
                base_conv=self.convert_from_base_to_dec(base_i)
                ascii_trans_base=self.convert_from_ascii(base_conv)
                alphabet_trans_base=self.convert_num_to_let(base_conv, base_i)

                print(f"Now using base {base_i}")
                print(f"{self._input_asarray} is {base_conv}")
                if ascii_trans_base!=0:
                    print(f"Ascii translation is : '{ascii_trans_base}'")
                if alphabet_trans_base!=0:
                    print(f"Alphabetic (num->letter) is {alphabet_trans_base}")
                    from_keyboard_trans_base=self.convert_to_keyboardpos(alphabet_trans_base)
                    to_keyboard_trans_base=self.convert_from_keyboardpos(alphabet_trans_base)
                    print(f"If we go from keyboard->alphabet we get {from_keyboard_trans_base}")
                    print(f"If we go from alphabet->keyboard we get {to_keyboard_trans_base}")
                print("------------------------------------------------------\n")

if __name__=='__main__':
    x=TranslatorBase("HELLODARKNESSMYOLDFRIEND",'')
    x()
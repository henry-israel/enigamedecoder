# -*- coding: utf-8 -*-
"""
Created on Mon Feb 22 17:54:47 2021

@author: henry

Decodes stuff for enigame
"""
import numpy as np
from itertools import groupby
from sympy.ntheory import factorint


class ToolKit:    
    def mixes(num):
        try:
            ele = int(num)
            return (0,ele,'')
        except ValueError:
            return (1, num, '')
        
    def capsConverter(string_input):
        '''
        Converts string to capitals with no spaces
    
        Parameters
        ----------
        string_input : English string
    
        Returns
        -------
        string all caps no spaces
    
        '''
        string_caps = string_input.upper()
        string_no_space = string_caps.replace(' ', '')
        return(string_no_space)

class NumberTools:
    '''
    Class of functions that deal with numbers
    '''
    def primeFactors(n):
        '''
        Returns prime factors of positive integer, n

        Parameters
        ----------
        n : int, >0

        Returns
        -------
        primfac : prime factors

        '''
        return factorint(n)
    
    def convertfromBaseN(input_text, base=2):
        '''
        Converts text<->binary

        Parameters
        ----------
        input_text : input string of base n numbers
        mode = int->Converts from base n to text

        Returns
        -------
        Text string or binary arr

        '''
        vals = input_text.split()
        translated = ''.join(chr(int(x, base)) for x in vals)
        return translated
    
    def convertoBinary(input_text):
        '''
        Converts to base N

        Parameters
        ----------
        input_text : Any string
        base : Alphabet base to translate to The default is 2.

        Returns
        -------
        String of letters

        '''
        byte_mode = bytearray(input_text, "utf-8")
        translated = ''.join(bin(byte)[0]+bin(byte)[2:]+" " for byte in byte_mode)
        return translated

    def converttoHex(input_text):
        '''
        Converts string to hex

        Parameters
        ----------
        input_text : Input string

        Returns
        -------
        Hex translation

        '''
        translation = ''.join(hex(ord(let))[2:]+" " for let in input_text)
        return translation

    def NumtoLet(input_string, mode='let'):
        '''
        

        Parameters
        ----------
        input_string : Input string of either all numbers or all letters
        mode : TYPE: optional
            Let-> converts letters to number
            num->converts numbers to letters
            DESCRIPTION. The default is 'let'.

        Returns
        -------
        Translation

        '''
        let_arr = ["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
               "N","O","P","Q","R","S","T","U","V","W","X","Y","Z", " "]
        num_arr = np.arange(1,27).astype(str)
        num_arr = np.append(num_arr, ' ')
        if mode == 'let':
            let_dict = dict(zip(let_arr, num_arr))
            mod_string = input_string.upper()
            
        if mode == "num":
            let_dict = dict(zip(num_arr, let_arr))
            mod_string = input_string.split()
        translated = ''.join(let_dict[letter]+" " for letter in mod_string)
        return translated
    
    def changeBase(input_num, init_base=10, conv_base=2):
        '''
        Converts to max base 9 (from up to base 36)

        Parameters
        ----------
        input_num : Input number as a string! to be converted
        init_base : int, starting base; optional
            DESCRIPTION. The default is 10.
        conv_base : int; base to be converted to, optional
            DESCRIPTION. The default is 2. (max of 9!)

        Returns
        -------
        input num in base(conv_base)

        '''
        #convert number to base 10
        first_conversion = int(input_num, init_base)
        a=0
        i=0
        while first_conversion:
            first_conversion, r = divmod(first_conversion, conv_base)
            a += 10**i * r
            i+=1
        return a

class AlphabetTools:
    '''
    Class of translation tools
    '''
    
    def asciiTranslator(string_input, mode="ascii"):
        '''
        Translates ascii <-> English
        
        Parameters:
            a string : an entry in ascii code or english
            mode : text or ascii
                text translates text -> ascii
                ascii converts ascii -> text
        ---
        Outputs:
        Text string translation
        '''
        if mode == "ascii":
            translate = ''.join(chr(num) for num in string_input)
        if mode == "text":
            translate = [ord(c) for c in string_input]
        return translate
    
    def morseTranslator(string_input, mode="morse"):
        '''
        Translates morse <-> english
        
        Parameters:
            string_input : A string
            
            mode : 
                "morse" -> translates morse to english
                "text" -> translates english to morse
        '''
        #We can just         
        morse_code_dict = { 'A':'.-', 'B':'-...', 
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
        if mode == "morse":
            rev_dict = dict(zip(morse_code_dict.values(), morse_code_dict.keys()))
            translated = ''.join(rev_dict[i] for i in string_input.split())
        if mode == "text":
            #we first have to translate to capitals
            string_caps = string_input.upper()
            translated = ''.join(morse_code_dict[i]+' ' for i in string_caps)
        return translated
    
    
    def turnIntoGrid(string_input):
        '''
        converts string into grid        

        Parameters
        ----------
        string : English string

        Returns
        -------
        output as nxn grid where n=len(string without spaces)

        '''
        #Remove spaces and convert to caps        
        string_caps = ToolKit.capsConverter(string_input)
        string_len = len(string_caps)
        len_root = np.sqrt(string_len)
        if len_root != int(len_root):
            print("could not convert to grid, not square")
            grid = 0
        else:
            let_arr = [letter for letter in string_caps]
            len_root = len_root.astype(int)
            grid =  np.reshape(let_arr, (len_root, len_root))
        return grid
    
    def reverseString(string_input):
        '''
        Capitalises and reverses string

        Parameters
        ----------
        string_input : Any string

        Returns
        -------
        String reversed with no spaces.

        '''
        string_caps = ToolKit.capsConverter(string_input)
        return reversed(string_caps)
    
    def alphabetiseString(string_input):
        '''
        Alphabetises string

        Parameters
        ----------
        string_input : Input string
        Returns
        -------
        Alphabetised string
        '''
        return ''.join(sorted(string_input))

    
    def frequencyCount(array_input):
        '''
        Converts a string or array into dictionary of value frequency

        Parameters
        ----------
        array_input : Either an array or a string

        Returns
        -------
        Dictionary of values

        '''
        #convert string to array
        if type(array_input) == str:
            array_input = [letter for letter in array_input]
        #Sort array
        array_input.sort(key = ToolKit.mixes)
        freq_dict = {key: len(list(group)) for key, group in groupby(array_input)}
        return freq_dict  
    
    def convertToBraille(input_string, mode="eng"):
        '''
        Converts string<->braille

        Parameters
        ----------
        input_string : text string
        mode : TYPE, braile=from braille; eng=to braille
            DESCRIPTION. The default is "eng".

        Returns
        -------
        TYPE
            DESCRIPTION.

        '''
        input_string = input_string.replace(' ','')
        print(input_string)
        asciicodes = [' ','!','"','#','$','%','&','','(',')','*','+',',','-','.','/',
                      '0','1','2','3','4','5','6','7','8','9',':',';','<','=','>','?','@',
                      'a','b','c','d','e','f','g','h','i','j','k','l','m','n','o','p','q',
                      'r','s','t','u','v','w','x','y','z','[','\\',']','^','_']
    
        braille = ['⠀','⠮','⠐','⠼','⠫','⠩','⠯','⠄','⠷','⠾','⠡','⠬','⠠','⠤','⠨','⠌','⠴','⠂','⠆','⠒','⠲','⠢',
                    '⠖','⠶','⠦','⠔','⠱','⠰','⠣','⠿','⠜','⠹','⠈','⠁','⠃','⠉','⠙','⠑','⠋','⠛','⠓','⠊','⠚','⠅',
                    '⠇','⠍','⠝','⠕','⠏','⠟','⠗','⠎','⠞','⠥','⠧','⠺','⠭','⠽','⠵','⠪','⠳','⠻','⠘','⠸']
        if mode=="eng":
            input_string.lower()
            trans_dict = dict(zip(asciicodes, braille))
        if mode=="braille":
            trans_dict = dict(zip(braille, asciicodes))
        print(trans_dict)
        return ''.join(trans_dict[let] for let in input_string)
    
    def convertToKeyBoardPos(input_string, mode="keyboard"):
        '''
        Converts alphabet<->keyboard position

        Parameters
        ----------
        input_string : String.
        mode : keyboard->translates from keyboard
            text->translates from english, optional
            DESCRIPTION. The default is "keyboard".

        Returns
        -------
        Translation.

        '''
        keyboard_alphabet=["Q", "W", "E", "R", "T", "Y", "U", "I", "O", "P", "A",
                           "D","F","G","H","J","K","L","Z","X","C","V","B","N","M", ' ']
        eng_alphabet=["A", "B", "C", "D", "E", "F", "G", "H", "I", "J", "K", "L", "M",
                      "N","O","P","Q","R","S","T","U","V","W","X","Y","Z", ' ']
        caps_input = input_string.upper()
        if mode=="keyboard":
            trans_dict = dict(zip(keyboard_alphabet, eng_alphabet))
        if mode=="text":
            trans_dict = dict(zip(eng_alphabet, keyboard_alphabet))
        return ''.join(trans_dict[i] for i in caps_input)


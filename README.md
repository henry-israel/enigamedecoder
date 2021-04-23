# enigamedecoder
Basically just enigame decoding stuff

NumberTools:
  -primeFactors(n) : gets prime factors
 
 -convertfromBaseN(string, base) : Input string of base N, returns string in latin alphabet
 
  -converttoBinary(text) : converts string to binary
  
  -converttoHex(text) : converts string to hex
  
  -NumtoLet(inputstring/int, mode=[let, num] :
    -Let mode : converts string of letters to numbers i.e. (a->1, b->2 etc.)
    -num mode : converts string of integers (separated by spaces) to letters
 
 -changeBase(int, initial_base, new_base) : converts a number from one base to another 
 

AlphabetTools:
  -asciiTranslator(string, mode=[ascii, text]_
    -Takes string and converts to:
      -mode=text : converts latin letters to ascii
      -mode=ascii : converts ascii to latin letters
  
  -morseTranslator(string, mode=[morse, text])
    -Converts between morse and english
      -mode=Morse : translates from morse to letters
      -mode=text : translates from text to morse
      
   -turnIntoGrid(string_input) : converts text string of length n into sqrt(n)xsqrt(n) grid
   
   -reverseString(string_input) : reverses string
   
   -alphabetiseString(string_input) : alphabetises string
   
   -frequencyCount(string_input) : counts frequency of letters in string
   
   -convertToBraille(input_string, mode=[text,braille] : converts string to
        -mode=text : converts text to braille
        -mode=braille : converts braille to text
        
   -convertToKeyBoardPos(input_string, mode=[text, keyboard] : converts to/from alphabet position to position on english keyboard
      -mode = text : converts alphabet location to keyboard location
      -mode = keyboard : converts keyboard location to alphabet location
##################################################################################################################################

example usage:
print(AlphabetTools.asciiTranslator("hello", mode="text")
Out >> [104, 101, 108, 108, 111]


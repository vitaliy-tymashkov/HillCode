https://www.codewars.com/kata/5e958a9bbb01ec000f3c75d8/train/python

Background
In classical cryptography, the Hill cipher is a polygraphic substitution cipher based on linear algebra. It was invented by Lester S. Hill in 1929.

Task
This cipher involves a text key which has to be turned into a matrix and text which needs to be encoded. 
The text key can be of any perfect square length but for the sake of this kata we will focus on keys of length 4 forming a 2x2 matrix.

To encrypt a message using the hill cipher, first of all you need to convert the text key into a key matrix. 
To do that you will convert the key row wise into a 2x2 matrix. 
Then you will substitute the letters with their respective positions on the alphabet: A=0, B=1,C=2 and so on till Z=25. 
So for example if we get the key text as cats, the key matrix will be:

[[ 2  0]
 [19 18]]
Now the next step is to break the text into pairs of two and convert those pairs into 2x1 matrices. 
If your text has an odd number of letters then just add a Z next to your last letter. 
Now again convert those letters into their respective position in the alphabet as above. 
So for example the text Hi would be converted into:

[[7]
 [8]]
Now we need to multiply the key matrix by the text matrix to get our encrypted matrix and then find out the encrypted matrix mod 26:

[[ 2  0]  *  [[7]  =  [[14]   =  [[14]  mod 26
 [19 18]]     [8]]     [277]]     [17]]
 
 c11 = 2 x 7 + 0 x 8 = 14           %26 = 14
 c21 = 19 x 7 + 18 x 8 = 277        %26 = 17
 
For the final step we just find out the letters at the alphabet position of 14 and 17 which are O and R.
 So OR is our encrypted message for the message Hi

In this kata you will be given a function named encrypt with the parameters text and key and you have to return the encrypted message in all uppercase letters

encrypt('','azyb') → ''
encrypt('Hi','cats') → 'OR'
encrypt('This is a good day','bbaa') → 'AAAAAAGACAGAYA'


test.assert_equals(encrypt('','azyb'), '')
test.assert_equals(encrypt('hello','hill'), 'DRJIMN')
test.assert_equals(encrypt('This is a good day','bbaa'), 'AAAAAAGACAGAYA')
test.assert_equals(encrypt('CODEWARS IS GREAT','wxyz'), 'CICQQIIASSDXKSFP')
test.assert_equals(encrypt('Five + Seven = Twelve','math'), 'IVSLIGSLAQEECSWR')



Note:

The text to encrypt will contain characters other than the alphabets, its your job to clean them before converting text to matrices. Spaces also need to be removed
The text may contain both uppercase and lowercase alphabets. Its your job to standardize them, the encrypted text however should be returned in uppercase letters.
The key will always contain 4 lowercase alphabet.
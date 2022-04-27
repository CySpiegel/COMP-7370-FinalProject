# Name the book: Write a crack for an improved substitution encryption

## Description
The `encrypted_book.txt` has been encrypted with a more effective version of the substitution cipher which also encrypts spaces and more.
This improved cipher is given to you (the enemy knows the system) in the `simpleSubCipher.py`
Your job is to write a python script which will crack this encryption in the general case.
You will probably want to use some kind of frequency or transitional probability methods.

1. From scratch, write a python3 script called `betterSubCrack.py`

2. We will execute your script as follows, from the bash command line:

    `$ ./betterSubCrack.py name_of_file_to_crack.txt decrypted_file_to_write.txt`

    Hint: you will need to add at least file input/output, command line arguments via sys.argv for example, a change of the permissions to executable of the crack script, and a shebang. If you don't know what a shebang is, google it and read!

3. It must run in under 3-4 minutes (or so). 

4. You should test encrypting other examples from https://www.gutenberg.org/ebooks/ and then cracking them, to verify that your program can produce correct decryptions.

5. It must run in python3 in the latest up-to-date stable Debian VM, where we will do all grading. 

6. All files must be utf-8 unix delimted (don't copy/paste from your Windows host, or risk the consequences of bad newlines!)

## Tips, tricks, reminders
* What is the most frequent character?
* What is the pattern for a full-stop '.' ?
* How many letters would you match with nothing but a pure letter frequency analysis?
* Careful with the headers, if you hack these! 
* Test with known encryptions (books you encrypt using the included source code).
* Remember to name files correctly, and put them in the root directory of the repo. 
* If you use imports, make sure to include them in the repo; we run in your directory.
* Do NOT assume or ask for user input via keyboard; 
  we will test your code with a program that will ignore all requests for keyboard input
* Please do NOT output tons of stuff, like the whole book each time.



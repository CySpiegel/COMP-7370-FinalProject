# pa01 - Name the book: Write a crack for an improved substitution encryption

## Assignment description
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

## Note (actually do this)!!
Thoroughly read the syllabus sections on "Programming assignments" and "Grading". These sections give good tips, tricks, hints, and instructions for programming assignments, including how to submit via Git.

## Grading
Your decryption does NOT need to be perfect; we will give you a % accuracy score. 
Specifically, if you got 99% of the characters in the book, you would receive 99% of the below points.
To be generous with points, this won't be linear, but more in your favor, where cracking 70% of letters would be better than a 70.

95% of this assignment will be graded based on the successful implementation of the crack and correct output.
A fully correct submission will result in a grade of 95%.
The remaining 5% will be awarded based on run-time for you main, with the student with the fastest run-time in the class receiving a 100%, and the slowest correct submission receiving 95%, and a linear interpolation (not sequential) using your actual time in between.
Time tests will be averaged over many book-encryption cracks for accuracy with students always compared on the same machine/environment.

## Re-grades and late work
As with all assignments, detailed in the syllabus.

## Due date
Please see the Canvas schedule for all due dates.


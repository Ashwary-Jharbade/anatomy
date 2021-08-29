# Anatomy
Anatomy is a web application which has a potential to predicts diseases caused due to genetic mutations using DNA sequencing and machine learning. At present the platform support prediction of COVID 19 using genetic sequence. Similary the concept can be used for other gene affecting diseases like Diabetes, AIDS etc.

# Project Link
#### [Demo - Anatomy](http://twinfinn.pythonanywhere.com/)

# Project Dependencies
1. python version 3.7
2. Django version 3.0.4
3. biopython
4. pickle
5. collection

# How to run after cloning or downloading
1. Install python version 3.7
2. Create and activate virtual environment 
3. Install project dependencies using 'pip'
4. Move to project directory using 'cd' command
5. Migrate the database using python manage.py migrate
6. Run the server using python manage.py runserver
7. Search on browser url localhost:8000

# Credentials to access Anatomy
Username - admin@example.com
Password - Admin

# Steps to check for a COVID test on Anatomy
1. Download a nucleotide sequence or get your own neuclotide sequence. Note - The nucleotide sequence should have fasta format/extention
2. Click on the choose file option and select your previously downloaded nucleotide sequence and hit the arrow icon.
3. Now wait fot the result and observe the graphical as well as textual report of the test. 

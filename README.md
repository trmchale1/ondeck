# ondeck

Dear Daniel,

This is a directory that I used to run a few scripts that completed most of 
the technical specifications you outlined.

1.) I created a PostgreSQL database on my mac

2.) You can run the input.py script to load data into the database,
with 'python input.py' at the command line (of course you would need the db name and password in the script)

3.) The output.py command will query that database and write that data to a csv file called 'output.csv' 

4.) I cleaned my data in output.py, however your data could be different (mine was stuck in a tuple)

5.) I did not ftp a server, my firewall gave me problems, the server I used was a google cloud instance without the command line tools I was used to ... it was the weekend and I wanted to prove I could do this quickly ... git has been robust enough for me in the past, and is of course is well known in the web development community ... I set up a google cloud instance and clone what I wanted with git clone to pull the csv over the internet



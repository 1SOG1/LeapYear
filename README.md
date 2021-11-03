#Read me 

1. [Challenges]
2. [Solutions]


### Challenges 
Setting up GitHub actions was fairly simple. The challenge was to get pytest to run the test I had written. 
This became my main struggle, primarily because I struggled to find documentation on the meaning of the different 
ERROR CODES. Once I realised that ERROR 5 was thrown if pytest didn't find my tests, it did not take long to find that I
had placed tests.py in the wrong folder. Further more i also realised that pytest did not like the new file structure 
where the project folder contained main.py, leap_year_check.py and a folder ("test"), which contained the tests. 
This threw ERROR 2. Since I now knew where I could find documentation on the meaning behind the error codes, this was a quick fix. 


### Solutions
After the initial struggles the actual fixes where easy enough. I first refactored test.py into its own folder ("test"), 
this was done as this is supposed to be the correct way to structure your tests. Since pytest was not able to find
the tests I had written when it was in its own folder I refactored it back into the root folder. This worked pytest now runs everytime
I push a new commit to GitHub and returns green check marks across the board (until I mess up the code again).

# Assignment-1 

### Discription: 

1. Our file uses a "setup" function to create two txt files called "temp_with_text.txt" and "temp_without_text.txt". We use these files to test the functions.
2. We also created a "teardown" function to clean up everything after the tests are completed. It deletes all the temporary files created during the setup or during the tests.
3. We created multiple tests with the prefix "test_" to be able to automate the fetching of the tests.
4. The main function "run_tests" runs the testing framework and is responsible for detecting any errors and fails. It is also the part that detects the time that has past while the test has run and prints the duration.
5. We decided to use "argparse" to be able to complete the --select + pattern task. This part of the script allows us to test specific tests or just a single function.




### Workflow:

1. Set up Git Lab for the group to make it easier to share and compare our respective attempts, as well as merge the code
2. Created a WhatsApp Group for easy communication
3. Creating all the required py and txt file we were going to use
4. Download the file: "file_manager.py" and adding it to our GitLab group
5. Reading some stuff about GitLab and Git in general because we were confused on how it worked
6. Recreating the testing framework, we learned about in class.
7. Start thinking about the test cases for each method in file_manager
8. Started writing the testcases
9. Added Timer and improved/ cleaned up the "status report" messages
10. Started to investigate the pattern requirement
11. Started to write the code for --select pattern
12. Debugging and improving of the program
13. Meeting up to discuss which parts we want to take from each individual program (everyone made a separate one)
14. Going over the combined code individually to make sure we eradicate all possible errors
15. Preparing the files to submit the task
16. Submit the task


### Design Decisions 
1. We decided to utilise the testing-framework presented to us in the lecture since it is understandable and we figured it was the way the assignment intended us to test the functions.
2. We chose the tests we wrote to test the correct output of the function. Further we added some tests to check if the functions fail correctly. 
3. We decided to use ***argparse*** since it provided an easy and simple solution for the problem we were facing.
4. Lastly we made the choice to re-format our output, so it is easier to differentiate between the different  test cases. This makes understanding the program easier. 


<br>

*Created by Ralph Kosch, Marlon Anderes and Nico Auf der Maur*
from helper import genGrade

def create_base():
    fname = "quiz_grades.txt"
    #TODO write to file fname
    #TODO introduce outer loop - write "Quiz"x, to file (10 times)
    #TODO introduce inner loop - write temp_grade to each line (17 times)
    temp_grade = genGrade()
    #TODO close the file
    
def create_average():
    old_fname = "quiz_grades.txt"
    #TODO read from file, old_fname
    #TODO extract each line from the file into a collection, list
    #TODO close the file
    
    #TODO write to file new_fname
    new_fname = "quiz_avg.txt"
    #TODO introduce loop - using the collection above
    #TODO implement the split function to separate each list element
    #TODO utilize an accumulator to hold the sum of the quiz grades
    #TODO calculate the average
    #TODO write the average for the element (quiz line) horizontally

def extra_credit(fname = "quiz_grades.txt"):
    '''
    Assume the order of quiz grades represent the same person. 
    For instance, you can say that student 1 received a 5 on quiz 1 and a 3 on quiz 2.
        Quiz1, 5, 8, ...
    	Quiz2, 3, 9, ...
    	... 
    	Quiz10, 
    Using the previous pseudocode create a file similar to the following
        Student1, Quiz1 Avg, Quiz2 Avg, ...
        ...
        Student 17, ...

    '''
    pass

def main():
    create_base()
    #TODO remove '#' below when ready to create average file
    #create_average()
    #extra_credit()

if __name__ == "__main__":
    main()

#I realised I answered this question incorrectly.
#I treated each line as a new number. Instead of treating the whole table as a single value.
#My answer was actually more difficult (and I already have a previous answer) so I'll leave this as a variant.

#https://stupidpythonideas.blogspot.com/2013/06/readlines-considered-silly.html
#above link was useful for opening from text file.


#list_product finds the largest product in a single line.
# 'question_length' allows for different length requests to be input
def list_product(line, question_length):
        line_length = len(line)-question_length+1 #stops itterating too far in the list
        line_product = 0
        print(line)
        #steps through the values in the line
        for i in range(line_length):
                curr_product = 1
                # multiplies the values to get the product at each step.
                #using a loop so the 'question_length' can be varied.
                for j in range(question_length):
                        curr_product *= line[i+j]
                #print("curr_product=",curr_product)
                if curr_product > line_product:
                        line_product = curr_product
        print("line_product",line_product)
        return line_product




def largest_product(question_length):
        final_result = 0
        #creates a list for each line in the text file.
        with open("p8_input.txt","r") as input:
                for line in input:
                        # converts the line string into a list with each integer as an element
                        #.rstrip() removes the '/n' new line from the end of the line
                        line = [int(x) for x in line.rstrip()]
                        line_result = list_product(line,question_length)
                        if line_result > final_result:
                                final_result = line_result
                        #print("result for",line,test_line)
        print("final_result =",final_result)



largest_product(13)
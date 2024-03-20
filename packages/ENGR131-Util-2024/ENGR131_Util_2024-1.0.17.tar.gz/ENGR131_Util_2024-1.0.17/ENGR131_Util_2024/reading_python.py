import ipywidgets as widgets
from ipywidgets import Output
from IPython.display import display, clear_output
from .util_json import load_json_to_dict, upsert_to_json_file
from .shuffle import shuffle_questions, shuffle_options
import drexel_jupyter_logger
from .encryption import get_string_from_encrypted_string
from .logging import check_log_assignment
from .database import ResponseStore
import time

# Global variable in the module
responses = load_json_to_dict('.responses.json')

class ReadingPython():
   """Class to build a reading python question
   """   
   
   def __init__(self,
               title,
               question_number,
               key,
               options, 
               solutions,
               points, # list of the total points for each question
               default=None,
               **kwargs):
      """Initialization function for the reading python question

      Args:
         title (str): title of the question
         question_number (int): question number
         key (list): Not implemented
         options (dictionary): a dictionary of options for the question including the following keys:
               "comments_options" : list of comments to choose from
               "n_rows" : number of rows to display
               "n_required" : number of rows required to respond
               "lines_to_comment" : list of lines to comment
               "table_headers" : list of table headers
               "variables_changed" : list of variables that can be changed
               "current_values" : list of current values
               "datatypes" : list of datatypes
         solutions (dict): a dictionary of encrypted solutions for the question. The dictionary should include the following:
               "comment" : list of encrypted solutions for the comments
               "execution" : list of encrypted solutions for the execution
         points (list): list defining the total points for the question, where the first element is the points for the comments and the second element is the points for the execution.

      Returns:
         obj: Reading Python object
      """      
      
      # Global variable in the module
      responses = load_json_to_dict('.responses.json')
      
      # checks to see that name is defined and only one assignment is being run
      check_log_assignment("output.log", **responses)
      
      self.solutions = solutions
      self.points = points
      self.question_number = question_number
      self.printed_output = Output()
      self.keys = key
      self.options = options
      
      # Dynamically assigning attributes based on keys, with default values from responses
      for num in range(0, len(options['lines_to_comment']) + 
                                    options['n_rows']):
         
         # Dynamically assign the key
         key = f"q{self.question_number}_{num+1}"
         
         # Dynamically assign the value from the responses file for persistance
         if num < len(options['lines_to_comment']):
            setattr(self, key, responses.get(key, default))
         else:
            setattr(self, key, responses.get(key, [default]*(len(options['table_headers'])-1)))
      
      #TODO could make this an optional feature
      # Checks that a seed was assigned to the responses
      try: 
         seed = responses["seed"]
      except ValueError:
         "You must submit your student information before you start the exam. Please submit your information and try again."
      
      # displays the question title
      display(widgets.HTML(f"<h2>Question {self.question_number}: {title}</h2>"))
      
      # Instructions for commenting lines
      comment_instructions = widgets.HTML(
         value="<b>Select an appropriate comment for the following lines of code:</b>"
      )

      # Creating a dropdown for each line that needs commenting
      self.dropdowns_for_comments = {
         line: widgets.Dropdown(
            options=shuffle_options(options["comments_options"], seed),
            description=f'Line {line}:',
            layout=widgets.Layout(width='600px'),
            value = eval(f'self.q{self.question_number}_{i_comments+1}')
         ) for i_comments, line in enumerate(options['lines_to_comment'])
      }
            
      # Displaying all dropdowns
      for dropdown in self.dropdowns_for_comments.values():
         display(dropdown)

      # Instructions for execution steps
      execution_instructions = widgets.HTML(
         value='''
         <b>For each step, select the appropriate response:</b>
         '''
               )
      
      #Create the header row
      header_row = widgets.HBox([widgets.Label(value=header, 
                              layout=widgets.Layout(width='150px', display='flex', justify_content='center')) for header in options["table_headers"]],
                              layout=widgets.Layout(display='flex', justify_content='center', align_items='center'))
      
      # make a deep copy of the lines to comment and add an empty string to the beginning
      # This is to provide the null response to the question
      line_comment = options["lines_to_comment"].copy()
      line_comment.insert(0, "")

      options_ = [line_comment, options["variables_changed"], 
               options["current_values"], options["datatypes"]]
      
      # Function to create a row with dropdowns
      def create_row(step):
         """function to create rows with dropdowns

         Args:
             step (int): step number

         Returns:
             widget: ipywidgets.HBox for a row
         """         
         
         # Initialize an empty list to store widgets
         list_ = []

         # Loop through the indices of the table headers
         for i in range(len(options["table_headers"])):
            # Check if it's the first column
            if i == 0:
               # If it's the first column, create a Label widget with the step number
               list_.append(widgets.Label(value=f'Step {step+1}', layout=widgets.Layout(width='150px', display='flex', justify_content='center')))
            else:
               # If it's not the first column, create a Dropdown widget
               # - Set layout properties for width
               # - Set options based on a variable (options_) indexed by i-1
               # - Set the value using dynamic evaluation of an expression
               list_.append(widgets.Dropdown(layout=widgets.Layout(width='150px'),
                                             options=options_[i-1],
                                             value=eval(f'self.q{self.question_number}_{len(options["lines_to_comment"])+step+1}[{i-1}]')))

         # Return an HBox widget containing the list of widgets horizontally aligned
         return widgets.HBox(list_,
                              layout=widgets.Layout(display='flex', justify_content='center', align_items='center'))


      # Generate rows dynamically based on n_rows
      self.rows = [create_row(_) for _ in range(options["n_rows"])]

      # Combine header and rows
      execution_steps = [header_row] + self.rows

      # Display the widget
      display(execution_instructions, *execution_steps)
      
      # Create a button for submission
      self.submit_button = widgets.Button(description="Submit")
      
      # Link the button to the function
      self.submit_button.on_click(self.on_submit_button_clicked)

      # Display the submit button
      display(self.submit_button, self.printed_output)
   
   def num_true_responses(self, solutions):
      """determines the number of 

      Args:
          solutions (list): list of encrypted solutions

      Returns:
          int: number of values which the student responded to
      """      
      # Initialize a counter variable
      count = 0

      # Loop through the indices of the solutions list
      for k in range(len(solutions)):
         
         # Extract values from the encrypted string using eval and a helper function
         num, variable, true_value, dataType = eval(get_string_from_encrypted_string(solutions[k]))
         
         # Check if all values extracted from the encrypted string are None
         if all(value is None for value in [num, variable, true_value, dataType]):
            # If all values are None, return the current count
            return count
         else:
            # If any value is not None, increment the count
            count += 1

               
   def on_submit_button_clicked(self, b):
      """callback which submit the question

      Args:
         b (any): not implemented

      """      
      
      # instatntiates the response store
      submit_score_ = ResponseStore() 
            
      # gets the comments outputs
      self.output_comments = []
      for out in self.dropdowns_for_comments.values():
         self.output_comments.append(out.value)
         
      # gets the per question points for comments
      comment_points = self.points[0]/len(self.dropdowns_for_comments)
      
      # gets the per question points for execution
      self.execution_points = self.points[1]/(self.num_true_responses(self.solutions['execution'])*4)
      self.execution_points_ = self.execution_points
      
      # gets the executions outputs
      self.output_execution = []
      for row in self.rows[:]:
         row_value = []
         for box in row.children:        
            if isinstance(box, widgets.Dropdown):
                  row_value.append(box.value)
         self.output_execution.append(row_value)
      
      with self.printed_output:
         
         # test the comments outputs
         for i, value in enumerate(self.output_comments):
            
            # checks if the value is the same as the solution
            if value == get_string_from_encrypted_string(self.solutions["comment"][i]):
               
               # logs the points for the question
               exec(f'drexel_jupyter_logger.variable_logger_csv("{comment_points}, {comment_points}", "q{self.question_number}_{i+1}")')
               points_earned = comment_points
            
            # if the question is wrong,
            else:
               exec(f'drexel_jupyter_logger.variable_logger_csv("0, {comment_points}", "q{self.question_number}_{i+1}")')
               points_earned = 0
               
            # saves the response in the JSON and the log file
            responses[f'q{self.question_number}_{i+1}'] = value
            drexel_jupyter_logger.variable_logger_csv(value, f"response_q{self.question_number}_{i+1}")
            
            # builds the dictionary of responses
            response = {"question_id": f"q{self.question_number}_{i+1}",
                        "score": points_earned,
                        "max_score": comment_points,
                        "student_response": str(value),
                        }
            submit_score_.add_response(response)
         
         # sets the number of comment questions
         num_comment_questions = i+1
         
         # gets the number of true responses
         num_true_responses = self.num_true_responses(self.solutions['execution'])
         
         def checker(value, solution, count):
            """Function to check the execution outputs

            Args:
                value (str): value provided by the student
                solution (str): encrypted solution
                count (int): question count

            Returns:
                int: incremented count
            """            
            # increments the count
            count += 1
            
            # checks if the value is the same as the solution, records the score and logs the response
            if value == solution:
               exec(f'drexel_jupyter_logger.variable_logger_csv("{self.execution_points}, {self.execution_points_}", "q{self.question_number}_{count}")')
               points_earned = self.execution_points
               max_points = self.execution_points_
            
            # if the question is wrong, records the score and logs the response
            else: 
               exec(f'drexel_jupyter_logger.variable_logger_csv("0, {self.execution_points_}", "q{self.question_number}_{count}")')
               points_earned = 0
               max_points = self.execution_points_
            
            # builds the dictionary of responses
            response = {"question_id": f"q{self.question_number}_{count}",
                     "score": points_earned,
                     "max_score": max_points,
                     "student_response": str(value),
                     }
            
            # adds the response to the response store
            submit_score_.add_response(response)
            
            # returns the incremented count   
            return count
         
         # saves the responses
         for j, value in enumerate(self.output_execution):
            # logs the response and saves the current response in the JSON and the log file
            responses[f'q{self.question_number}_{j+i+2}'] = value
            drexel_jupyter_logger.variable_logger_csv(value, f"response_q{self.question_number}_{j+i+2}")
            
         # sets the part of the solution to check 
         scored_line = num_comment_questions
         run_number = 0
            
         # test the execution outputs
         for j, value in enumerate(self.output_execution):  
      
            # checks the run number until correct
            num, variable, true_value, dataType = eval(get_string_from_encrypted_string(self.solutions["execution"][run_number]))
            
            # breaks if the solution is all None
            if all(value is None for value in [num, variable, true_value, dataType]):
               break
            
            # adds the run number for the next check because the line number is correct
            run_number += 1
            
            # If the students had a wrong response and added more responses than the number of true responses, this stops the grader from increasing the denominator
            if run_number > num_true_responses:
                  self.execution_points_ = 0
            
            # check if line number is correct
            if value[0] == num:
                  
               # adds a count for recording the question number
               scored_line += 1
               
               # logs the responses as an encrypted csv
               exec(f'drexel_jupyter_logger.variable_logger_csv("{self.execution_points}, {self.execution_points_}", "q{self.question_number}_{scored_line}")')
               
               # builds the dictionary of responses
               response = {"question_id": f"q{self.question_number}_{scored_line}",
                        "score": self.execution_points,
                        "max_score": self.execution_points_,
                        "student_response": str(value[0]),
                        }
               
               # adds the response to the response store
               submit_score_.add_response(response)
               
               
               # if the line number is correct, check the rest of the values
               scored_line = checker(value[1], variable, scored_line)
               scored_line = checker(value[2], true_value, scored_line)
               scored_line = checker(value[3], dataType, scored_line)
            
            # if the line number is wrong, record the score and logs the response 
            else:
               for i in range(4):
               
                  # logs the response
                  exec(f'drexel_jupyter_logger.variable_logger_csv("0, {self.execution_points_}", "q{self.question_number}_{scored_line}")')
                  
                  # builds the dictionary of responses
                  response = {"question_id": f"q{self.question_number}_{scored_line}",
                        "score": 0,
                        "max_score": self.execution_points_,
                        "student_response": str(value[0]),
                        }
                  submit_score_.add_response(response)
               continue
         
         # prints that the data is saved 
         with self.printed_output:
            # print statement
            print("Data Saved.")
            
            # sleep 2 seconds
            time.sleep(2)
            
            # clears the printed output
            self.printed_output.clear_output()
      
      # adds the responses to the hidden JSON file for persistant storage.       
      upsert_to_json_file(".responses.json", responses)
      
class ReadingPythonQuestion(ReadingPython):
   """
         A class representing a question for reading, commenting, and interpreting Python code.

         Args:
            title (str): The title of the question. Default is "Reading, Commenting, and Interpreting Python Code:".
            question_number (int): The number of the question. Default is 4.
            key (str): The identifier/key for the question. Default is "READING1".
            options (dict): A dictionary containing various options for the question.
                  - "comments_options" (list): A list of potential comments with only one correct per line.
                  - "n_rows" (int): The number of rows for the table. Default is 20.
                  - "n_required" (int): The number of required rows to respond. Default is 10.
                  - "lines_to_comment" (list): Lines of code that require commenting.
                  - "table_headers" (list): Headers for the table.
                  - "variables_changed" (list): List of variables changed.
                  - "current_values" (list): List of current values for variables.
                  - "datatypes" (list): List of data types.
            solutions (dict): A dictionary containing solutions for the question.
                  - "comment" (list): Encrypted strings representing the comments.
                  - "execution" (list): Encrypted strings representing the execution steps.
            points (list): Points allocated for the question. Default is [20, 30].
            default (Any): Default value. Default is None.
            **kwargs: Additional keyword arguments.

         Attributes:
            title (str): The title of the question.
            question_number (int): The number of the question.
            key (str): The identifier/key for the question.
            options (dict): A dictionary containing various options for the question.
            solutions (dict): A dictionary containing solutions for the question.
            points (list): Points allocated for the question.
            default (Any): Default value.
            **kwargs: Additional keyword arguments.

         Methods:
            Any methods inherited from the base class ReadingPython.

         Inherits:
            ReadingPython: A base class for reading Python questions.
   """
   def __init__(self,
            title = "Reading, Commenting, and Interpreting Python Code:",
            question_number = 4,
            key="READING1",
            options={
               # General list of 15 potential comments with only one correct per line
               "comments_options" : [
                  None,
                  "Initializes a list of numbers with integers and floats.",  
                  "Initializes the count of even numbers to 0.",  
                  "Initializes the count of odd numbers to 0.",  
                  "Starts a while loop based on the condition of 'odd' being less than 6.",  
                  "Iterates over each number in the 'numbers' list using a for loop.",  
                  "Checks if the current number is evenly divisible by 2.",  
                  "Increments 'even' by the current number's value if it's even.",  
                  "The else condition captures numbers that are not even.",  
                  "Increments 'odd' by the current number's value.", 
                  "Defines a function.",
                  "Imports a module.",
                  "Prints output to the console.",
                  "Catches an exception.",
                  "Returns a value from a function.",
                  "Initializes a dictionary."
               ],
               # Define the number of rows you want ahead of time
               "n_rows" : 20,  # for example, 5 rows'
               "n_required" : 10,  # number of rows required to respond. 
               # Lines of code that require commenting
               "lines_to_comment" : [1, 2, 3, 5, 6, 7, 8, 9, 10],
               # Table headers
               "table_headers" : ['Step', 'Line Number', 'Variable Changed', 'Current Value', 'DataType'],
               # Variables Changed
               "variables_changed" : ["", 'None','numbers', 'even', 'odd', 'num'],
               "current_values" : ["", "None", "[5, 2, 3.0]", "[5, 2, 3]", "3", "2", "5", "3.0", "5.0", "2.0", "0", "0.0","8","8.0", "True", "False"],
               "datatypes" : ["", "NoneType", "list", "dictionary", "tuple", "set", "string", "float", "integer", "boolean"],
               }, 
            solutions = {"comment" : [b'gAAAAABl1q99Wv4aPSDg6LQhBEQzgFtJ9MN_XDXopLDP50drzX1DezKFukFvaLoCtBq1aFXh0CrpZpNodN-Vzew1mrnRYJCe1ROS0e4d_mtC956mv7yP7voLkkDTDhLZBkfGcTbIr_2q2KGGWRdDd4UlU1SQaSmbzQ==',
                                       b'gAAAAABl1q99DXeUpz3sj_aGJ2Ieeqq1izvhuNzsr6ZE8AcrkNGnk3MU97VYphWhh4TRW3g7tPWQY_ObUJ49kCCmAT8_PEVjyHGslZ8cUO9DKywU1Vkm5gJFU9TQdhmrj1FPHiOraK6R',
                                       b'gAAAAABl1q99eDPZODzznroc01fWMAsdyT9B2AbUlNzZITsKUEv8h9ZJkkhKA94ud2kLWYYBEYRtcYJBDzW19kJBb2XIVXy3zKXFQg0yB8WNcWpbmKLfBaNSuthpr8Ytu4JQAKwSSnlZ',
                                       b'gAAAAABl1q9995flK7wgl6nvqKtz40m-1FuUxXhz1M7V2he9dujjQZfoIIHyGSEgFSCIxC9t9xakCfe9Nh5i7IYXlqsEfhwTOKLGVVyKg6V7ySZjPASked-hMrV8gNbEuBThxYuwpkhePKohR1H6kJ0fAC9Bem_UrANLHi5duQ8N3nYv8Zy0rNs=',
                                       b'gAAAAABl1q99pmZhaYJaoWDlqV6JOzSrR3YnUHV5TKErq9j2lNvazYI1FBxh8ESAFLr4CxAjAeIo_ABPQi2Klfxv8CpOMQjyriG2wGap8HGX7mtImu5nUqeODvSQ0TcaAQ5VKEzj8vaZYSf6prr1YO7U_waujyB2cZ6MYLYtAGW7MWa2xNoK-us=',
                                       b'gAAAAABl1q990LzTjbcCvmb71hWnvepnMpwFDOjXIZx98cWMUh2rWvXY8dfxR_--1JlpwwsO_ZtCWR3YMixkUdJsbDLNEmD8bIxDv7cQpgC0Kn6z_LsS85lknbNXv-GxrVmSpSJ9DXPq1F0Z9H4XHvGDfN7FfesQ2Q==',
                                       b'gAAAAABl1q99CJFDChPojbFkAv0ZyX68JpUECaExkuDADiNvIgg9jJrwBoOAqghWtrBNIWQsrJBN5wWR0VYJaAJyb-GP_XTyLbIbZo8DUm7rjEfbZtefQolq-qMPAfWJpWhCtI6lWmqwKkCWuh3He_NVxvLCBV4azg==',
                                       b'gAAAAABl1q99PVShMt1jqKao5u8jcAXuXjS-Q508GjLURQ16rfjc21kge4UZxN8npF6bSiLz5A-YkbZlZZui3NV2ZUoo_S3fWX4_BOsKZsslUgss26l_EFkDtm7rnCBX-mgVJ9HZiPCIqtS0QzyJ8zAZqdx7dMIyow==',
                                       b'gAAAAABl1q99cZIU5UIH224xJQz3jef1Wwj2E0Xi1KDwUkYGKNpNmpfipztnGnxqjbMRLsihZ5Yay_0n3_uUnbMtgLbmjNLyi0HSVpoefMAG-mmmHtpYxQmpkCxchpTAa5aoqXKww6k-'],
                  "execution" : [b'gAAAAABl1q8E3kt4h9tbqGCERd2A4GLXe1TzrtljG8Si8iW0qhe1IggARKa95CLsNLZu4QUSMGSzp1Ba6oDngoK0BTiiBHjrpM23D57D-Y4ezQsXWPL4DZ1Q2zWYrYWPgRgzwZt-iH5t',
                                          b'gAAAAABl1q8E9Fv8DbwpXoP0Gy6yYY_2iRqS2FyQOe33JqeB2nDvxBCyL_PjwU2IX_rmoUaONcQ8Pq_VXe9ru8UFF1NHbFjLFCZmclW1Bdv0KOVdhu2BxKk=',
                                          b'gAAAAABl1q8Eph4a9y0wfb1oq-IVY_-p6bHFVpstE-9AyHKCUrsKAAoHXNRPORmSTpUqWlvM0Ogkf9_EaWnN-RpDWfnqgyIhO09dIribn-Lnylvvo-qviAQ=',
                                          b'gAAAAABl1q8EvXYSLxQeqJN1qv3IeBvLn_0gmQQBBiXgoF8ejzTDFVXo3yLsKX6ISAx8M7Yr4X_yv09ZH0lB4wFyzgmzQmcTB4xb_sW_Xrk9QuNc2GkNvik=',
                                          b'gAAAAABl1q8E8-20RSdb07KZ7tiv67hCYWiZjQ4JuzEqziWekdQEESrJvEzPIdGqX67qEkWp6EdKLRvkgot172nygFBouc7P6Bm0Xuhj53xh1OcXDryMKDU=',
                                          b'gAAAAABl1q8ETv1FXgMj8rHCSrm1uKFDoQns138CoSTM50etQkLCQuxVq3GBXKgO75prWaFS6oJUia_myViAon1hzolTHsaL7ynQUW7_Ei0X2Ug9QjC85cw=',
                                          b'gAAAAABl1q8E0CxONdimcoXNfsA5fVdBsdMAG_P7tbDHICA1E8l9c8QLHa_9mh1MceQbhfenWnYpX3RSrjT8Hb86lOKAPBL8oGioyS3n00LE-VGmeMW8qe4=',
                                          b'gAAAAABl1q8EQurUDytOd7CJY65nDkSOM7s3xC0GCuOzYaVADUgEcYQT4tnx5d-YvNWu-DnQiMi20bCW6m5zWgscwjhkjgTQIzDXGtVpA87Vr6EWHUoBorI=',
                                          b'gAAAAABl1q8Exyu-jhDAJR3uCMoHpBE6NZghRngUn0TQemdFIT8PYceb78lpCZ2isPBOsiWQ7p-zF9jJHlr1MQfFCFDDAN5g_E4ZVZhwGUDjOBj_QsG03Kw=',
                                          b'gAAAAABl1q8E6aMCwDSIzxgfwA-zu2kpyQ6htoIsd1kiQN9I3sJjl-mrIUed9gcnIcZqFqW6eHwC7iUqLHDNPqo5Y8zE8lUrqBdW2Bvu-u5KYSYHxzaPR2U=',
                                          b'gAAAAABl1q8EVA7YUP_FnkdwpeZ3YSaUmOXtNfIMlH-u3_E7vScmiKMstFvIzVcSUweisEwYU1u-P3CRPJ10KecXPsnpz4hOm1pWq4H7728XNrqivLskqBk=',
                                          b'gAAAAABl1q8ErlUhzme_utnMJuUshsx5RKeEK32L6eJddzZXRE06CDKr_W7kkVmNmxaLf91sTubHbybp6WuUh2qjZITEhdqWIsga7eS_Qa0UmDVSxRW57ig=',
                                          b'gAAAAABl1q8EI-uwMltNPSq373z3COXxSmJMliMJMaOGHYb4eoA7DBbNirbXiSQ_Y0XXPRMalpzIKI-Dx-HOSAlWVCMufqY8ODK_OYOLh8teJzD4tlKvOLA=',
                                          b'gAAAAABl1q8EK6yJv3j2TRL9rXC3rjqL5seCNTCnPOwzYbl0qLHDlLh-1D5T7xBV-u--gLaNgW39j4E2evr2TcDVoi0NAyD5hSXU0oMJOfKm8nWPSWEvrjs=',
                                          b'gAAAAABl1q8EC3Z7rfCcPpMsKwgaSI-wn8gSWNJ5-DrvBda1SKyql78ls6hG-AAo3ZmWtfpBo2ohXCdyHCQMESsp_CVHtVcRMrqzJ2Il1KeGv-9sBckLgTk=',
                                          b'gAAAAABl1q8EOL8kJUY3Rf270qS59grgmrk-kI-Nk9Q9wv4dGn-h0ocll79me67HGaN1ut9Z6RuDOvh9KaLrwNTacQKaM5LQspPHByjrHO9Sg5yKH6_iBOk=',
                                          b'gAAAAABl1q8EVxKaF_blhOO9u44ewpuYmOhGuMRnJZOG2wo6bp_xsP7sdWl6TJXra3inw2KxhKObtYifqwR0AAeP55eax4IDXR7nahH2wkSksSfYJ-WdaXY=',
                                          b'gAAAAABl1q8EuEMPPa201D7F0trBKIyJdy63w1v0VNapUlgslszQjBKr57uFc9mOhjPbcFkfgrDmt9DoERvBfUhkNn9HdBmOW0UVMHlhPFE1IbyANyqQbx4=',
                                          b'gAAAAABl1q8EPOGQWmd_ThEbOUe5garH1QtsEEQYD3fQtEfYdwcHYg5gf7ueDZvcOeKILkpILFM3P89k-JzsLbrlwkqCeMzvjfHOR7RtJ-JQbkAFqRESY5Y=',
                                          b'gAAAAABl1q8EtR6pRBooMybHtnFjt9p3WBVmLE3wIzyMtFuSE1TCTVOtKW64DamF2RlH89P6Kv9koqQRdWPrQDEM0uLJgS1y__ng1CSDd7ay52qVpjPcvkA=']},
            points = [20,30],
            default=None,
            **kwargs):
      
      
      
      super().__init__(
               title=title,
               question_number=question_number,
               key=key,
               options=options, 
               solutions=solutions, 
               points=points,
               default=default,
               **kwargs
            )
from .util_json import load_json_to_dict
import requests
import json
import pickle
import os
from unittest.mock import patch
import drexel_jupyter_logger
from collections import defaultdict
import argparse
from datetime import datetime
import numpy as np

class ResponseStore:
    """Class to store student responses in a file
    """    

    def __init__(self, filename=".list.pkl"):
        """Initialize the class with a filename

        Args:
            filename (str, optional): hidden file where the results are saved. Defaults to ".list.pkl".
        """        
        self.filename = filename
        self.create_file()
        
    def create_file(self):
        """Function that creates the file
        """        
        
        # Check if the file already exists
        if not os.path.exists(self.filename):
            # The file does not exist; create it and write an empty list
            with open(self.filename, 'wb') as file:
                pickle.dump([], file)
        else:
            pass
    
    def add_response(self, response_):
        """function to add the responses to the file

        Args:
            response_ (list): response to add to a file
        """        
        
        # Open the file and load the list
        with open(self.filename, 'rb') as file:
            response = pickle.load(file)
            
        # Append the new response to the list
        with open(self.filename, 'wb') as file:
            response.append(response_)
            pickle.dump(response, file)
            
    def get_responses(self):
        """Gets the responses from an existing file

        Returns:
            list: list of responses contained in a file. 
        """        
        
        # Open the file and load the list
        with open(self.filename, 'rb') as file:
            response = pickle.load(file)
        return response
    
    def delete_responses(self):
        """ Deletes the file from the system
        """        
        # Remove the file
        os.remove(self.filename)
        
    def submit_responses(self):
        """Submits the responses to the server
        """        
        
        # Create a new submit_score object
        scorer = submit_score()
        
        # Add the responses to the scorer
        for response in self.get_responses():
            scorer.add_response(response)
            
        # Submit the responses
        out = scorer.submit()
        
        # If the submission was successful, delete the file
        if out:
            os.remove(self.filename)
        
def submit_question():
    """ Function that submits the question to the server
    """    
    
    # Create a new response store object
    responder = ResponseStore()
    
    # Submits the responses to the server
    responder.submit_responses()

class submit_score():
    """Class to submit the score
    """    
    
    def __init__(self, 
                username = "student",
                password = "capture",
                post_url = "https://engr131-student-grader.nrp-nautilus.io/live_scorer",
                login_url = "https://engr131-student-grader.nrp-nautilus.io/login",
                ):
        """Initialization of the submit score class

        Args:
            username (str, optional): username for the postgres database. Defaults to "student".
            password (str, optional): password for the postgres database. Defaults to "capture".
            post_url (str, optional): post URL for the flask server. Defaults to "https://engr131-student-grader.nrp-nautilus.io/live_scorer".
            login_url (str, optional): login URL for the flask server. Defaults to "https://engr131-student-grader.nrp-nautilus.io/login".
        """        
        
        # Global variable in the module
        responses = load_json_to_dict('.responses.json')
        
        # check if the student information is submitted
        if responses.get("drexel_id") is None:
            ValueError("You must submit your student information before you start the exam. Please submit your information and try again.")
        
        # Set the student id and assignment id 
        if responses.get("assignment_id") is None:
            ValueError("You must submit your student information before you start the exam. Please submit your information and try again.")
            
        self.student_id = responses.get("drexel_id")
        self.assignment_id = responses.get("assignment")
        self.post_url = post_url
        self.login_url = login_url
        self.ip_address = responses.get("IP_Address", "Not Provided")
        self.hostname = responses.get("hostname", "Not Provided")
        self.JupyterUsers = responses.get("JupyterUsers", "Not Provided")
        self.list_of_responses = []
        
        # Login credentials
        self.login_data = {
            "username": username,
            "password": password,
        }
        
    def convert_to_string_or_na(self, input_value):
        """Convert the input value to a string or return "N/A" if there is an error

        Args:
            input_value (any): input value that is provided to string

        Returns:
            str: string to be returned
        """        
        
        try:
            # Attempt to convert the input value to a string
            return str(input_value)
        except:
            # If there is an error during the conversion, return "N/A"
            return "N/A"
        
    def add_response(self, response):
        """add response to the list of responses

        Args:
            response (str): response to be added to the list of responses
        """        
        
        # Convert the student response to a string or "N/A" if there is an error
        student_response = self.convert_to_string_or_na(response.get("student_response"))
        
        # Create a dictionary to store the response
        out = {"student_id": self.student_id,
            "assignment_id": self.assignment_id,
            "question_id": response.get("question_id"),
            "score": response.get("score"),
            "max_score": response.get("max_score"),
            "student_response": student_response ,
            "ip_address": self.ip_address,
            "hostname": self.hostname,
            "JupyterUsers": self.JupyterUsers,
            }
        
        self.list_of_responses.append(out)
        
    def submit(self):
        """function to submit the responses.
        """        
        
        # Create a session object to maintain cookies
        session = requests.Session()
        
        # Headers for login (if required, e.g., Content-Type)
        login_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }

        # Step 1: Login to the server
        login_(session, login_headers, self.login_data, self.login_url)
        
        # It's important to set the correct content type for JSON data
        headers = {'Content-Type': 'application/json'}   
        
        data = {
            "password": "capture",  # Include the password here
            "data": self.list_of_responses
            }
        
        # sends the response to the server
        success = send_response(session, headers, data, self.post_url)
        
        
#################### Validate log file ####################


class ValidateLogFile():
    
    """ Class to validate the log file and submit the score to the server
    """
        
    def __init__(self, 
                filepath,
                assignment_id,
                free_response_questions = 0,
                question_max_scores = {1: 18, 2: 6, 3: 20, 4: 50, 5: 35, 6: 30, 7: 36, 8: 40, 9: 63},
                username = "student",
                password = "capture",
                post_url = "https://engr131-student-grader.nrp-nautilus.io/upload_score",
                login_url = "https://engr131-student-grader.nrp-nautilus.io/login",
                ):
        """Class to validate the log file and submit the score to the server

        Args:
            filepath (filepath): Location of the log file
            assignment_id (str): Assignment to be graded
            free_response_questions (int, optional): number of free response questions, theses are graded by just the last response. Defaults to 0.
            question_max_scores (dict, optional): a dictionary of the question numbers (int), and max score, used for the grade report. Defaults to {1: 18, 2: 6, 3: 20, 4: 50, 5: 35, 6: 30, 7: 36, 8: 40, 9: 63}.
            username (str, optional): username for the student postgres server. Defaults to "student".
            password (str, optional): password for the postgres server. Defaults to "capture".
            post_url (str, optional): post url for the flask server. Defaults to "https://engr131-student-grader.nrp-nautilus.io/upload_score".
            login_url (str, optional): login url for the flask server. Defaults to "https://engr131-student-grader.nrp-nautilus.io/login".
        """        
        
        
        self.filepath = filepath
        self.assignment_id = assignment_id
        self.free_response_questions = free_response_questions
        self.question_max_scores = question_max_scores
        
        # Login credentials
        self.login_data = {
            "username": username,
            "password": password,
        }
        self.login_url = login_url
        self.post_url = post_url
        self.run()
        
    def run(self, key=None):
        """function to run the validation and submit the score to the server

        Args:
            key (string, optional): string to decode the log file. Defaults to None.

        Returns:
            _type_: _description_
        """        
        
        # gets the key, or uses the default key
        if key == None:
            key = "7mPZKa3gJZn4ng0WJ5TsUmuQC2RK9XBAwTzrTEjbyB0="
            
        # Decoding the log file
        data_ = drexel_jupyter_logger.decode_log_file(self.filepath, key=key)
        loginfo = str(data_)
        
        # Initialize the question scores and max scores
        question_max_scores = self.question_max_scores
        question_scores = self.question_max_scores.copy()

        # Initialize the question scores
        for key, value in question_scores.items():
            question_scores[key] = 0
        
        # Parsing the data to find the last entries for required fields
        # This gets the student name
        last_entries = {}
        for entry in data_:
            parts = entry.split(", ")
            if parts[0] == 'info' and len(parts) == 4:
                field_name = parts[1]
                field_value = parts[2]
                last_entries[field_name] = field_value
        
        # Check if the assignment id is in the log file
        if self.assignment_id not in last_entries['assignment']:
            exit(f"Your log file is not for the correct assignment. Please submit the correct log file.")
        
        # Check if the student information is submitted
        if last_entries.get("drexel_id") is None:
            exit("You must submit your student information before you start the exam. Please submit your information and try again.")
            
        # Check if the student information is submitted
        if last_entries.get("first_name") is None:
            exit("You must submit your student information before you start the exam. Please submit your information and try again.")
            
        # Check if the student information is submitted
        if last_entries.get("last_name") is None:
            exit("You must submit your student information before you start the exam. Please submit your information and try again.")
        
        # Check if the student information is submitted
        if last_entries.get("drexel_email") is None:
            exit("You must submit your student information before you start the exam. Please submit your information and try again.")
        
        # initialize the code and data lists
        code = []
        data = []

        # Splitting the data into code and responses
        for row in data_: 
            
            # Splitting the data into code and responses
            if 'code run:' in row:
                code.append(row)
            else:
                data.append(row)

        # Checks to see if the drexel_jupyter_logger is in the code
        # if it is, the student might have tried to look at the solutions
        flag = any("drexel_jupyter_logger" in item for item in code)
        
        # Extracting timestamps and converting them to datetime objects
        timestamps = [datetime.strptime(row.split(", ")[-1].strip("."), '%Y-%m-%d %H:%M:%S') for row in data]

        # Getting the earliest and latest times
        last_entries["start_time"] = min(timestamps).strftime('%Y-%m-%d %H:%M:%S')
        last_entries["end_time"] = max(timestamps).strftime('%Y-%m-%d %H:%M:%S')
        last_entries["flag"] = flag

        # This gets the student information dictionary
        student_information = {key.upper(): value for key, value in last_entries.items()}

        # Write the dictionary to 'results.json'
        with open('info.json', 'w') as file:
            print("Writing to info.json")
            json.dump(student_information, file)

        def get_last_entry(data, field_name):
            """function that gets the last entry for a given field name

            Args:
                data (list): all of the data records as a list
                field_name (str): field name to be extracted

            Returns:
                list: list of the last entry for a given field name
            """            
            for entry in data[::-1]:
                parts = entry.split(", ")
                if parts[0] == field_name:
                    return entry
            return None

        def get_len_of_entries(data, question_number):
            """function to get the unique entries by length

            Args:
                data (list): list of all the data records
                question_number (int): question number to evaluate

            Returns:
                int: length of the unique entries
            """            
            
            # Extracting the unique q1_* values
            unique_q1_values = set()

            for entry in data:
                if entry.startswith(f"q{question_number}_"):
                    # Split the string by commas and get the value part
                    parts = entry.split(", ")
                    value = parts[0].split("_")[1]  # The value is the third element after splitting
                    unique_q1_values.add(value)

            return len(unique_q1_values) + 1
        
        # Modified list comprehension to filter as per the criteria
        free_response = [
            entry
            for entry in data_
            if entry.startswith("q")
            and entry.split("_")[0][1:].isdigit()
            and int(entry.split("_")[0][1:]) > self.free_response_questions]
        
        # Initialize a dictionary to hold question entries.
        q_entries = []

        # Iterate over the number of free response questions.
        for i in range(1, self.free_response_questions + 1):
            # Collect entries for each question in a list.
            entries = [get_last_entry(data, f'q{i}_{j}') for j in range(1, get_len_of_entries(data, i))]
            
            # Store the list of entries in the dictionary, keyed by question number.
            q_entries += entries


        q_entries += free_response
        
            # Parse the data
        parsed_data = [line.split(", ") for line in q_entries]

        unique_question_IDs = set(row[0] for row in parsed_data)

        # Initialize a dictionary to hold the maximum score for each unique value
        max_scores = {unique_value: 0 for unique_value in unique_question_IDs}

        # Loop through each row in the data
        for row in parsed_data:
            unique_value = row[0]
            score = float(row[2])
            possible_score = float(row[3])
            # Update the score if it's higher than the current maximum
            if score > max_scores[unique_value]:
                max_scores[unique_value] = score

        # Loop through the max_scores dictionary and sum scores for each question
        for unique_value, score in max_scores.items():
            # Extract question number (assuming it's the number immediately after 'q')
            question_number = int(unique_value.split("_")[0][1:])
            question_scores[question_number] += score

        # Sorting the dictionary by keys
        question_max_scores = {key: int(np.round(question_max_scores[key])) for key in sorted(question_max_scores)}

        # Sorting the dictionary by keys
        question_scores = {key: int(np.round(question_scores[key])) for key in sorted(question_scores)}
                
        # Creating the dictionary structure
        result_structure = {
        "tests": [],
        "password": "capture",
        }

        # Adding entries for each question
        for question_number in question_scores.keys():
            question_entry = {
            "name": f"Question {question_number}",
            "score": question_scores[question_number],
            "max_score": self.question_max_scores[question_number],
            "visibility": "visible",
            "output": ""
        }
            result_structure["tests"].append(question_entry)

        # Write the dictionary to 'results.json'
        with open('results.json', 'w') as file:
            print("Writing to results.json")
            json.dump(result_structure, file, indent=4)
            
        # Create a session object to maintain cookies
        session = requests.Session()
        
        # Headers for login (if required, e.g., Content-Type)
        login_headers = {
            "Content-Type": "application/x-www-form-urlencoded"
        }
            
        login_(session, login_headers, self.login_data, self.login_url)
            
        # The file you're uploading. Ensure the path is correct.
        file_path = "results.json"
        # Cookies for authentication, loaded from a file.
        # cookies = {'student_cookie': open('student_cookie.txt', 'r').read().strip()}

        # Construct the data payload as a dictionary.
        data = {
            'password': self.login_data["password"],
            'assignment_id': self.assignment_id,
            'student_id': last_entries.get("drexel_id"),
            'original_file_name': file_path,
            'start_time': last_entries["start_time"],
            'end_time': last_entries["end_time"],
            'flag': last_entries["flag"],
            'submission_mechanism': 'jupyter_notebook',
            'log_file':loginfo,           
        }

        # Files to be uploaded. The key should match the name expected by the server.
        files = {
            'file': (f"{file_path}_results.json", open(file_path, 'rb')),
        }

        # Make the POST request with data, files, and cookies.
        response = session.post(self.post_url, data=data, files=files)

        # messages to the user
        submission_message(response)
            
def submission_message(response):
    """Returns the submission message

    Args:
        response (obj): response object from the server
    """    

    # messages to the user
    if response.status_code == 200:
        print("Data successfully uploaded to the server")
        print(response.text) 
    else:
        print(f"Failed to upload data. Status code: {response.status_code}")
        print(response.text)
        print("There is something wrong with your log file or your submission. Please contact a Instructor for help.")
    os.remove("results.json")

            
def send_response(session, headers, data, post_url):
    """Sends response to server

    Args:
        session (obj): flask server connection
        headers (dict): headers for the server
        data (list): list of data to be uploaded
        post_url (str): post url for the flask server
    """    
    
    # Make the POST request
    response = session.post(post_url, 
                            headers=headers, 
                            data=json.dumps(data))
    
    # messages to the user
    submission_message(response)
    
def login_(session, login_headers, login_data, login_url):
    """logins to the flask server

    Args:
        session (obj): flask server connection
        login_headers (str): login header
        login_data (dict): login information
        login_url (str): flask server url for login
    """    
    
    # Step 1: Login to the server
    login_response = session.post(login_url, 
                                data=login_data,
                                headers=login_headers)
    
    # Check if login was successful
    if login_response.status_code == 200:
        print("Login successful")
    else:
        Exception("Login failed")
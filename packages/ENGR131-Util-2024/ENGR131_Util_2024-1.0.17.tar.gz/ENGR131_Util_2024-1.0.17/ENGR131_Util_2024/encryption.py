import drexel_jupyter_logger

# Predefined key
key = "7mPZKa3gJZn4ng0WJ5TsUmuQC2RK9XBAwTzrTEjbyB0="

def get_string_from_encrypted_string(binary):
   """Gets the string from an encrypted string

   Args:
       binary (binary): The encrypted string

   Returns:
       str: decrypted string
   """   
   string = binary.decode()
   return drexel_jupyter_logger.decrypt_outputs(string)

def generate_encrypted_solutions(solutions):
   """"Generates encrypted solutions
   
   This is a helper function to encrypt the solutions.

   Args:
       solutions (list): solution provided as a list

   Returns:
       list: list of encrypted solutions
   """   
   
   encrypted_solutions = [drexel_jupyter_logger.encrypt_output(str(solution), key) for solution in solutions]
   return encrypted_solutions
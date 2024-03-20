import drexel_jupyter_logger
from IPython import get_ipython

def cell_logger(execution_info):
    """Logs the cell content

    Args:
        execution_info (obj): The execution info object from the Jupyter notebook
    """    
    
    # Extract the cell content
    cell_content = execution_info.raw_cell

    # Encrypt the cell content
    encrypted_output = drexel_jupyter_logger.encrypt_output(f"code run: {cell_content}", "7mPZKa3gJZn4ng0WJ5TsUmuQC2RK9XBAwTzrTEjbyB0=")

    # Replace the cell content with the encrypted output
    # Note: Depending on your requirements, you might handle this differently
    execution_info.raw_cell = encrypted_output
    
def check_log_assignment(log, key=drexel_jupyter_logger.key, **responses, ):
    """Checks the log file for the assignment

    Args:
        log (filepath): file path to the log file
        key (str, optional): encryption key. Defaults to drexel_jupyter_logger.key.

    Raises:
        ValueError: error if student email is not found
        ValueError: error if the assignment is not found

    Returns:
        _type_: _description_
    """    
    
    if "drexel_email" not in responses:
        raise ValueError("Please fill out the student info form and run the test again")

    
    assignments = set()
    
    data = drexel_jupyter_logger.decode_log_file(log, key=key)
    
    for entry in data:
        parts = entry.split(", ")
        if parts[0] == 'info' and len(parts) == 4:
            if parts[1] == 'assignment':
                assignments.add(parts[2])
                
    if any(not responses['assignment']==i for i in assignments):
        raise ValueError("Your log file is from an old assignment. Please make sure your are working in an empty folder.")
    
    return data
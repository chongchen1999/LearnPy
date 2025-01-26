import traceback

def buggy_function():
    return 1 / 0  # This will raise a ZeroDivisionError

# Open a log file in write mode
with open("error_log.txt", "w") as log_file:
    try:
        buggy_function()
    except Exception as e:
        # Log the exception and its traceback into the file
        log_file.write("Exception caught!\n")
        
        # Use traceback to log the exception details
        log_file.write("\n--- Traceback using traceback.print_exc() ---\n")
        traceback.print_exc(file=log_file)
        
        # Get traceback as a string and write it to the log file
        tb_str = traceback.format_exc()
        log_file.write("\n--- Traceback as string ---\n")
        log_file.write(tb_str)
        
        # Log the stack trace details
        log_file.write("\n--- Stack trace details ---\n")
        for line in traceback.format_stack():
            log_file.write(line.strip() + "\n")

print("Error details have been logged to 'error_log.txt'.")

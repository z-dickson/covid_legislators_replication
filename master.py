import time
import os
import subprocess

# Record the start time
start_time = time.time()  


try: 
    subprocess.run(['Rscript', 'analysis.R'], capture_output=True, text=True)
    subprocess.run(['python', 'figures.py'], capture_output=True, text=True)
except RuntimeError as e:
    print(e)
    

# Record the end time
end_time = time.time()  
execution_time = end_time - start_time  # Calculate the total execution time
print(f"All scripts executed successfully in {execution_time:.2f} seconds.")







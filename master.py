import time
import os
import subprocess


# Record the start time
start_time = time.time()  


try: 
    # install R packages 
    subprocess.run(['Rscript', 'requirements.R'], check=True)
    
    # run R script
    r_process = subprocess.run(['Rscript', 'analysis.R'], capture_output=True, text=True)
    
    # check for errors 
    if r_process.returncode !=0:
        print('Error running R script:')
        print(r_process.stderr)
        print('Try running the files individually from the `individual_files` folder')
    
    # install python packages 
    subprocess.run(['python', 'requirements.py'], check=True)
    
    
    py_process = subprocess.run(['python', 'analysis.py'], capture_output=True, text=True)
    
    if py_process.returncode !=0:
        print('Error running Python script:')
        print(py_process.stderr)
        print('Try running the file as a notebook using the `.ipynb` file in the `individual_files` folder')
    
    # Record the end time
    end_time = time.time()  
    execution_time = end_time - start_time  # Calculate the total execution time
    print(f"All scripts executed successfully in {execution_time:.2f} seconds.")
    
    
except Exception as e:
    print('Error running scripts:')
    print(e)
    print('Try running the files individually from the `individual_files` folder')
    









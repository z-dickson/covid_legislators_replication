## function to install required packages if not already installed
def install(package):
    import subprocess
    import sys
    subprocess.check_call([sys.executable, "-m", "pip", "install", package])
    
## install required packages
install("pandas")
install("numpy")
install("plotly")
install("kaleido")

# libraries required for the analysis 

# List of package names to install
packages_to_install <- c("fect", "dplyr", "kableExtra", "modelsummary", "ggplot2", "grf")

# Check if each package is already installed
for (package_name in packages_to_install) {
  if (!(package_name %in% installed.packages())) {
    # If not installed, install the package
    install.packages(package_name)
  }
}
#!/bin/bash

# Check if Python is installed
if ! command -v python3 &> /dev/null; then
    echo "Python is not installed. Please install Python before running this script."
    exit 1
fi

# Check if required packages are installed
required_packages=("json" "os" "colorama" "datetime" "uuid" "pytest")

for package in "${required_packages[@]}"; do
    if ! python3 -c "import $package" &> /dev/null; then
        echo "$package is not installed. Please install it using 'pip install $package' before running this script."
        exit 1
    fi
done

# Ask the user if they want to run the Python script
read -p "Do you want to run the Python script? (y/n): " run_python

if [ "$run_python" == "y" ]; then
    python3 main.py
else
    echo "Exiting without running the Python script."
fi

# Run using ./run.sh
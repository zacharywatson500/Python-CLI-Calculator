# Python CLI Calculator (Argparse)

A fast, single-operation calculator built for the command line. This project demonstrates strong proficiency in **command-line argument parsing** and robust input validation using Python's built-in `argparse` module.

### Key Features

* **Argparse Implementation:** Uses `argparse` to define and validate positional arguments (`num1`, `operator`, `num2`) and optional flags (`-v`/`--verbose`).
* **Automatic Error Handling:** Leverages `argparse`'s built-in type checking (`type=float`) and constraint enforcement (`choices=`) to handle bad input gracefully.
* **Modular Design:** Separates core calculation logic (`calculator_functions.py`) from the input/output handler (`cl_calc.py`).
* **Verbose Output:** Includes a `-v` flag for optional debugging information.

###  How to Run

1.  **Clone the repository:**
    ```bash
    git clone [YOUR_NEW_GITHUB_URL_HERE]
    cd Python-CLI-Calculator
    ```
2.  **Execute the script with arguments:**

    ```bash
    # Basic operation:
    python cl_calc.py 15.5 + 4.5

    # Verbose operation:
    python cl_calc.py 100 / 0 -v
    
    # Example of invalid input handled by argparse:
    python cl_calc.py 50 power 2
    ```

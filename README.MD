# Recycled Concrete Aggregates Mix-Design Application

## Overview

This application calculates mix designs for recycled concrete aggregates (RCA) using different methods. It was developed for the University of Ottawa in collaboration with the Structural Engineering Department. The application provides three different calculation modes:

- Equivalent Mortar Volume (EMV)
- Modified Equivalent Mortar Volume (EMV-MOD)
- Equivalent Volume (EV)

The application is built using Python and the Tkinter library, and it can be packaged into an executable for distribution.

## Features

- User Input: Enter values for materials like cement, fines, coarse aggregates, water, RCA, and other parameters.
- Calculation Modes:
    - EMV: Calculates the equivalent mortar volume based on provided inputs.
    - EMV-MOD: Provides a modified version of the EMV calculation.
    - EV: Calculates the equivalent volume using different parameters.
- Error Handling: Alerts for invalid input and calculation errors.
- Graphical User Interface: Intuitive interface with clear labels and buttons.

## Requirements

- Python: Version 3.x
- Tkinter: Included with Python standard library
- Pillow: For image handling (install using pip install Pillow)

## Installation

1. Clone the Repository:
    git clone <https://github.com/LucasMe110/RCA-Mix-uottawa>

2. Install Dependencies:
Make sure you have Pillow installed. You can install it using pip:
    pip install Pillow

3. Run the Application:
    python app.py

If you have packaged the application into an executable, simply run the executable file.

## Usage

1. Enter Values: Input the required values for cement, fines, coarse aggregates, water, RCA, OVA, residual mortar, and other parameters.

2. Select Calculation Mode: Choose one of the calculation modes (EMV, EMV-MOD, EV) by clicking the respective button.

3. Calculate: Click the "Calculate" button to perform the calculations and display the results.

4. View Results: The results for cement, fine aggregates, natural CA, RCA, and water will be displayed in the respective fields.


## Example
For a sample input:
- Cement: 500 kg/m³
- Fines: 200 kg/m³
- Coarse Aggregates: 700 kg/m³
- Water: 180 kg/m³
- RCA: 50 kg/m³
- OVA: 1.5
- Residual Mortar Content: 10%

Selecting the EMV calculation mode and clicking "Calculate" will display the computed values for cement, fine aggregates, natural CA, RCA, and water in the application window.

##Contributing
If you would like to contribute to this project, please fork the repository and submit a pull request with your changes. Ensure that your code adheres to the project's coding standards and includes appropriate tests.

## License
This project is licensed under the MIT License. See the LICENSE file for details.

## Acknowledgments 
- University of Ottawa
- Structural Engineering Department

For any questions or feedback, please contact [lucasmellomo@gmail.com].

Feel free to adjust the details as necessary for your specific use case!
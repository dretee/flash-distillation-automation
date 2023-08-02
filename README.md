# Flash Distillation Automation Code

This repository contains a Python script for automating flash distillation calculations. Flash distillation is a widely used separation process in chemical engineering, and this code aims to simplify the calculations involved.

## Background

Flash distillation is a process used to separate a mixture into its individual components based on their vapor-liquid equilibria. The key parameters in flash distillation are the vapor-liquid ratio (V/F) and the relative volatility of the components. This script uses a set of equations to iteratively calculate the V/F ratio and the component compositions in the liquid and vapor phases.

## Features

- Easy Input: The script prompts the user to input the relative volatility (k) and the initial vapor fraction (V/F) to initiate the calculation process.

- Iterative Calculation: The script uses an iterative method to calculate the V/F ratio by solving a set of equations. It runs for a maximum of 100 iterations or until the specified tolerance level is met.

- Component Composition: The script calculates the mole fractions of each component in the liquid and vapor phases and displays them in an easy-to-read tabular format.

- Flow Fraction Calculation: The script also provides the option to input the flow rate and calculates the liquid and gas flow rates based on the component compositions.

## How to Use

1. Clone or download the repository to your local machine.
2. Ensure you have Python installed.
3. Open the Python script in your preferred Python editor or IDE.
4. Run the script, and you will be prompted to input the relative volatility (k) and the initial vapor fraction (V/F).
5. The script will calculate the V/F ratio and display the component compositions in the liquid and vapor phases.
6. If desired, you can input the flow rate to calculate the liquid and gas flow rates.

## Dependencies

- NumPy: A powerful library for numerical computations in Python.
- Tabulate: A Python library for formatting and printing tabular data.

Make sure to install the required dependencies before running the script.

## License

This project is licensed under the MIT License. Feel free to use and modify the code for your purposes.

## Disclaimer

This code is provided for educational and illustrative purposes only. It is the user's responsibility to verify and validate the results obtained from this script. The authors are not liable for any misuse or inaccuracies in the calculations. Use at your own risk.

Feel free to explore and contribute to this project! If you have any questions or suggestions, please don't hesitate to reach out.

Happy distillation! 🌬️🍶

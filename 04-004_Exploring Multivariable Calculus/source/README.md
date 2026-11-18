# Multivariable Calculus: Setup Guide

This guide supports **Practical Task 2** in *Exploring Multivariable Calculus*. The `multivariable.py` script uses **SymPy** to calculate partial derivatives and the gradient of a multivariable function. Python **3.10 or later** is recommended.

## Project files

Place the following files in the same directory:

```text
source/
├── multivariable.py #Multivariable script
├── requirements.txt #Dependencies file
└── README.md        #Markdown file with setup guide
```

Open a terminal in that directory before running the commands below. The virtual environment is local to this project and should not be submitted with the task.

## 1. Create and activate a virtual environment

### Windows: Command Prompt

```cmd
py -m venv venv
venv\Scripts\activate.bat
```

### Windows: PowerShell

```powershell
py -m venv venv
.\venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead. Avoid changing system-wide execution policies just for this task.

### Windows: Git Bash

```bash
py -m venv venv
source venv/Scripts/activate
```

### macOS / Linux

```bash
python3 -m venv venv
source venv/bin/activate
```

On some Linux distributions, the `python3-venv` operating-system package may need to be installed first.

## 2. Install the dependencies

With the environment activated, run the same command on all platforms:

```bash
python -m pip install -r requirements.txt
```

This installs SymPy and its required dependencies, including mpmath. An internet connection is needed for the first installation.

## 3. Verify the installation

```bash
python -c "import sympy; print('SymPy version:', sympy.__version__)"
```

A version number confirms that SymPy can be imported from the active environment.

## 4. Run the practical task

```bash
python multivariable.py
```

Follow the prompts in the script. For the example function `x**2 + y**2`, the partial derivatives are `2*x` and `2*y`, giving the gradient `(2*x, 2*y)`.

## 5. When finished

```bash
deactivate
```

## Troubleshooting

- **`No module named 'sympy'`**: Activate the virtual environment, then rerun `python -m pip install -r requirements.txt`.
- **`python` or `py` is not recognised**: Install Python 3.10+ and ensure it is available from the terminal; on macOS/Linux use `python3` to create the environment.
- **File not found**: Confirm that the terminal's current directory contains `multivariable.py` and `requirements.txt`.
- **PowerShell execution policy error**: Use Command Prompt activation as shown above.

No paid accounts, API keys, or third-party services are required to run the script after installing the dependencies.

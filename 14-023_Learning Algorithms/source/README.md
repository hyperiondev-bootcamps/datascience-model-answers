# Backpropagation practical task

`backpropagation_task.ipynb` contains the implementation, including the baseline network, learning-rate and iteration experiments, hidden-size comparison, and sigmoid/tanh comparison.

The notebook explains the solution and its observed results. All model calculations use NumPy; plots use Matplotlib. Accuracy is measured on training data.

## Run the notebook

From this folder on macOS / Linux, create and activate the environment, install dependencies, and register the notebook kernel:

```sh
python3 -m venv venv
source venv/bin/activate
python -m pip install -r requirements.txt
python -m ipykernel install --sys-prefix --name learning-algorithms --display-name "Learning Algorithms (venv)"
JUPYTER_PATH="$PWD/venv/share/jupyter" JUPYTER_CONFIG_DIR="$PWD/.jupyter" IPYTHONDIR="$PWD/.ipython" MPLCONFIGDIR="$PWD/.mplconfig" JUPYTER_RUNTIME_DIR="$PWD/.runtime" python -m jupyterlab
```

On Windows (Command Prompt), use:

```powershell
python -m venv venv
.\venv\Scripts\activate
python -m pip install -r requirements.txt
python -m ipykernel install --sys-prefix --name learning-algorithms --display-name "Learning Algorithms (venv)"
$env:JUPYTER_PATH = "$PWD\venv\share\jupyter"
$env:JUPYTER_CONFIG_DIR = "$PWD\.jupyter"
$env:IPYTHONDIR = "$PWD\.ipython"
$env:MPLCONFIGDIR = "$PWD\.mplconfig"
$env:JUPYTER_RUNTIME_DIR = "$PWD\.runtime"
python -m jupyterlab
```

Select **Learning Algorithms (venv)** and run all cells in order. `requirements.txt` lists the five direct dependencies. 

Stop JupyterLab with Ctrl+C in the terminal, then run `deactivate` when finished.

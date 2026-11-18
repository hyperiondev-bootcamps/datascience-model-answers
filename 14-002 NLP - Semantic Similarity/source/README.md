# Semantic Similarity Notebooks: Setup Guide

This folder contains `semantic.ipynb` and `movies_task.ipynb`. Both use spaCy; the first compares the medium and small English models, while the second uses the medium model for movie recommendations.

## Requirements

- Python 3.10 or newer, with a version supported by spaCy 3.8 and the selected packages
- Internet access for the initial installation
- Jupyter Notebook, JupyterLab, or VS Code with the Jupyter extension (or Google Colab)
- `movies.txt` in the notebook's working directory for `movies_task.ipynb`

## 1. Create and activate a virtual environment

Open a terminal in the folder containing `requirements.txt`.

**Windows Command Prompt**

```cmd
py -m venv .venv
.venv\Scripts\activate.bat
```

**Windows PowerShell**

```powershell
py -m venv .venv
.\.venv\Scripts\Activate.ps1
```

If PowerShell blocks activation, use Command Prompt instead.

**Windows Git Bash**

```bash
py -m venv .venv
source .venv/Scripts/activate
```

**macOS / Linux**

```bash
python3 -m venv .venv
source .venv/bin/activate
```

## 2. Install all dependencies and language models

With the virtual environment activated, run:

```bash
python -m pip install -r requirements.txt
```

This installs spaCy, the `en_core_web_md` and `en_core_web_sm` language models, and the Jupyter kernel package. The language models are downloaded from spaCy's official GitHub release repository.

## 3. Register and select the notebook kernel

Run:

```bash
python -m ipykernel install --user --name semantic-similarity --display-name "Python (Semantic Similarity)"
```

Open either notebook in Jupyter or VS Code and select **Python (Semantic Similarity)** as its kernel. In VS Code, ensure the Python and Jupyter extensions are installed.

## 4. Verify installation

In a notebook cell, run:

```python
import spacy

medium = spacy.load("en_core_web_md")
small = spacy.load("en_core_web_sm")
print("spaCy:", spacy.__version__)
print("Medium model vector dimensions:", medium.vocab.vectors_length)
print("Small model vector dimensions:", small.vocab.vectors_length)
```

The medium model should report **300** vector dimensions; the small model should report **0**. The small model's lack of static word vectors is expected and may trigger warnings when calculating similarity.

## 5. Make `movies.txt` available

For Jupyter and VS Code, keep `movies.txt` in the current working directory used by the notebook, typically alongside `movies_task.ipynb`. Check with:

```python
from pathlib import Path
print("Working directory:", Path.cwd())
print("Movie file available:", Path("movies.txt").exists())
```

In Google Colab, upload `movies.txt` using the Files panel. Colab runs in a hosted environment and does not use your local virtual environment; if using Colab, install dependencies in a notebook cell with `%pip install -r requirements.txt` after uploading `requirements.txt` to the session, then restart the runtime if prompted.

## Troubleshooting

If a model cannot be found, confirm the notebook is using the virtual environment's kernel and rerun the installation command in that environment. If `movies.txt` cannot be found, check the current working directory and place the file there. If `py` is unavailable on Windows, try `python` instead.

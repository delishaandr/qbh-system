Before running:
1. Download Robert Jang's QBSH corpus from MIREX or from [this link](https://music-ir.org/evaluation/MIREX/data/qbsh/MIR-QBSH-corpus.tar.gz)
2. Copy the `waveFile` folder to the project and rename the folder to `train`

How to run:
1. Make a virtual environment 
   ```python -m venv env```
2. Activate virtual environment:
   - On Windows:
     ```env/Scripts/activate```
   - On MacOS/Linux:
     ```source env/bin/activate```
3. Install requirements
   ```pip install -r requirements.txt ``
4. Install kernel
   ```python -m ipykernel install --user --name=env```
5. Start Jupyter and select the `env` kernel
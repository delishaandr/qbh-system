# How to Run

Before running:
1. Download Robert Jang's QBSH corpus from MIREX or from [this link](https://music-ir.org/evaluation/MIREX/data/qbsh/MIR-QBSH-corpus.tar.gz)
2. Copy the `waveFile` folder to the project and rename the folder to `train`
3. Make a virtual environment 
   ```
   python -m venv env
   ```

How to run:
1. Activate virtual environment:
   - On Windows:
     ```
     env/Scripts/activate
     ```
   - On MacOS/Linux:
     ```
     source env/bin/activate
     ```
2. Install requirements
   ```
   pip install -r requirements.txt
   ```
3. Install kernel
   ```
   python -m ipykernel install --user --name=env
   ```
4. Start Jupyter and select the `env` kernel

# How to Run

Before running:
1. Download `dataset` ZIP file from [this link](https://drive.google.com/drive/folders/1xgaRW9B1DaqNvFNF_ANJjnWxvq19pqZl?usp=drive_link)
2. Unzip file in project folder
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

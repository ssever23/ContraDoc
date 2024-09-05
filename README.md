# contradictory-information

## Necessary packages:

Use pip install requirements.txt to install necessary packages

### This project was realized on WSL2 (Ubuntu)

## Code Structure:

The NLI dataset for contradiction detection can be created under src/data_generation/pair_generation. The existing dataset is under data/csv_files/nli_data_set.csv


The roberta models are fine-tuned under src/fine_tuning. The already fine-tuned models can be found under https://drive.google.com/drive/folders/1qz2VEEVveU1tKGR_VzYJCDys_-HF-8N4?usp=drive_link


The vector stores are created under src/vectorization/vector_db. vector_store contains the vectorized files from data/PDFs. The database with and without contradictory data can be found under https://drive.google.com/drive/folders/1znRj73MKkpHycmIHg7MTiCoiT6zSr9Pi?usp=drive_link


src/classifications uses different chunking methods to find similar chunks, which are subsequently classified by a roberta model. The classification results are then passed onto Llama 3.

 
src/llm contains the notebook for Llama 3.


results contains the fine-tuning and classifications results for the different models and chunking methods.


Further explanations are in the notebooks.


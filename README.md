# This is for NUS Module DSA3101 Project Group 2
# E-Commerce Performance Analysis and Optimization

# Setting up the project

## Downloading dataset
The `data` folder should consists of 14 datasets in total. However, since the size of 6 datasets is large, you can download the remainding datasets from this [link](https://drive.google.com/drive/folders/1G_p7zx7Ra-ZgVX2OqqRIfJGLkL3LB7lH?usp=drive_link) and paste it into the `data` folder.

## If running locally 
If you are running locally, you can choose to initialize a python virtual environment by running `python -m venv venv` and then `source venv/bin/activate` (macOS) or `venv\Scripts\activate` (Windows). After you are in the virtual environment, run `pip install -r requirements.txt` to install the relevant dependencies.

## If running on Docker
Do note that if the `.ipynb` files are run on Google Collab, the directory `model_dataset/dataset` and `model_dataset/saved_model` need to be created on Google Collab Runtime. The content of the `/dataset` and `/saved_model` also need to be manually placed onto the Google Collab Runtime environment.

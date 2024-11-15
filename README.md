# This is for NUS Module DSA3101 Project Group 2
# E-Commerce Performance Analysis and Optimization

# Setting up the project

## Downloading dataset
The `data` folder should consists of 14 datasets in total. However, since the size of 6 datasets is large, you can download the remainding datasets from this [link](https://drive.google.com/drive/folders/1G_p7zx7Ra-ZgVX2OqqRIfJGLkL3LB7lH?usp=drive_link) and paste it into the `data` folder.

## If running locally 
If you are running locally, you can choose to initialize a python virtual environment by running `python -m venv venv` and then `source venv/bin/activate` (macOS) or `venv\Scripts\activate` (Windows). After you are in the virtual environment, run `pip install -r requirements.txt` to install the relevant dependencies.

## If running on Docker
In your command prompt, use the docker pull command `docker pull gridten/techtacularproj` to download the Docker image. Start the container from the image using `docker run -p 8888:8888 gridten/techtacularproj`. Copy the token from the output. It will be used to login to the local host webpage.  
Head to [http://localhost:8888/login](http://localhost:8888/login).  
Input the token copied from the command prompt into the login page to access all our files and data.

## For bonus Question 1 (Product recommendation)
System will prompt when running code. Please copy paste the customer id when system prompts you.

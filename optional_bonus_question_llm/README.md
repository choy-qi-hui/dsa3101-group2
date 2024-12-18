## Setting up API Keys

This project requires API keys for OpenAI and Tavily to function. Follow the steps below to set up your environment.

1. OpenAI API Key
- Go to the [OpenAI platform](https://platform.openai.com/docs/overview).
- Log in or sign up for an account.
- Navigate to the API Keys section under your account settings.
- Create a new API key and copy it. This will require you to have credits available in your account.

2. Tavily API Key
-  Go to the the [Tavily website](https://tavily.com/).
- Log in or create an account.
- Navigate to the API Access or Developer Settings section.
- Generate a new API key and copy it. 

Open the `agent.py` file in your preferred code editor.
Locate the section where the environment variables are defined.
Replace the placeholders with your actual API keys.  

## Running the Streamlit Demo App
1. Change to the directory of the folder
2. Ensure your virtual environment is activated
3. Run `python -m streamlit run app.py` in the terminal
from langchain.agents import AgentExecutor, create_openai_tools_agent
from langchain_core.prompts import ChatPromptTemplate
from langchain_community.tools.tavily_search import TavilySearchResults
from langchain_openai import ChatOpenAI
import os

os.environ["OPENAI_API_KEY"] = ""  # Replace with your API key
os.environ["TAVILY_API_KEY"] = ""  # Replace with your API key

def recommender(query, num_responses=3):
    """
    Calls the OpenAI API to get product recommendations based on the user query.
    """
    tools = [TavilySearchResults(max_results=num_responses)]

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert in e-commerce product recommendations. \
            Your goal is to recommend the most relevant product listings that match the user's query, ensuring they align with the specific features and quality, and price range the user may expect. \
                Provide a short description for each recommended product, including key details such as brand, features, price range, and why it may suit the user’s needs. \
                    Include a working link to each product listing, ensuring that each recommendation is up-to-date, accurate, and readily available for purchase."), 
                    ("user", f"Recommend products for: {query}"),
                    ("placeholder", "{agent_scratchpad}"),
    ])

    # Choose the LLM that will drive the agent
    # Only certain models support this
    llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'),
                     model="gpt-3.5-turbo", temperature=0.5, max_retries=num_responses)

    # Construct the OpenAI Tools agent
    agent = create_openai_tools_agent(llm, tools, prompt)

    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor.invoke({"input": query})["output"]

def reviewer(recommendation_text, num_responses=1):
    """
    Calls the OpenAI API to provide a review or summary of the recommended products.
    """
    tools = [TavilySearchResults(max_results=num_responses)]

    prompt = ChatPromptTemplate.from_messages([
        ("system", "You are an expert in evaluating and summarizing e-commerce product recommendations. \
                        You will receive multiple product suggestions based on a user’s query. Your goal is to compile these recommendations into a cohesive, organized list that is easy to understand. \
                            Review each product suggestion to ensure it aligns with the user’s preferences. If any recommendations don’t fully meet these criteria, either adjust the description for clarity or suggest alternative options that better match the user’s needs. \
                                For each recommended product, verify that the provided link is valid and leads to an active item listing that is available for purchase and matches the product description. If a link is broken or invalid, remove the product recommendation. \
                                    Present the final list in a clear, user-friendly format."), 
                                    ("user", f"Review the following recommendations: {recommendation_text}"),
                                    ("placeholder", "{agent_scratchpad}"),
    ])

    # Choose the LLM that will drive the agent
    # Only certain models support this
    llm = ChatOpenAI(api_key=os.getenv('OPENAI_API_KEY'),
                     model="gpt-3.5-turbo", temperature=0.5, max_retries=num_responses)

    # Construct the OpenAI Tools agent
    agent = create_openai_tools_agent(llm, tools, prompt)

    # Create an agent executor by passing in the agent and tools
    agent_executor = AgentExecutor(agent=agent, tools=tools, verbose=True)

    return agent_executor.invoke({"input": recommendation_text})["output"]
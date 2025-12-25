
from dotenv import load_dotenv
import os
from langchain_groq import ChatGroq
from dotenv import load_dotenv

#loading api key (environment variable)
load_dotenv()

# create instance of llm by providing API key
llm = ChatGroq(groq_api_key=os.getenv("GROQ_API_KEY"), model_name="llama-3.3-70b-versatile")




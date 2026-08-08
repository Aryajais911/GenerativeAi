  # it is a integration between langchain and openAi
from dotenv import load_dotenv
from langchain_openai import OpenAI
from openai import RateLimitError


load_dotenv()

llm = OpenAI(model="gpt-3.5-turbo-instruct")

result = llm.invoke("What is the capital of India")
print(result)

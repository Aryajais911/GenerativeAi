
# HuggingFaceEndpoint -> use this when you want to call API of HF.
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
  # it tells which model you want to use in hugging face
    repo_id ="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation"
)

model = ChatHuggingFace(llm=llm)
result = model.invoke("What is the Capital of India?")

print(result.content)
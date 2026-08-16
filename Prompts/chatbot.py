from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
import os

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="Qwen/Qwen2.5-7B-Instruct",
    huggingfacehub_api_token=os.getenv("HUGGINGFACEHUB_API_TOKEN"),
    task="text-generation",
    max_new_tokens=512,
    temperature=0.7,
)

model = ChatHuggingFace(llm=llm)

chat_history = []  # ye chat ki history ko memory me store karta hai

while True:
    usr_input = input("You: ")
    chat_history.append(usr_input)
    if usr_input.lower() == "exit":
        break

    result = model.invoke(chat_history)

    chat_history.append(result.content) # ye jo result output aaya hai usko v chat history me store kar dega taaki model ko past conversations yaad rahe.
    print("AI:", result.content)
print(chat_history)
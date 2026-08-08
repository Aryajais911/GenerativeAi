import os

from dotenv import load_dotenv
from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_google_genai.chat_models import ChatGoogleGenerativeAIError


load_dotenv()

api_key = os.getenv("GOOGLE_API_KEY") or os.getenv("GEMINI_API_KEY")

if not api_key:
	print(
		"Missing Gemini API key. Set GOOGLE_API_KEY or GEMINI_API_KEY in your .env file or shell."
	)
else:
	model = ChatGoogleGenerativeAI(model="gemini-2.0-flash", google_api_key=api_key)

	try:
		result = model.invoke("What is the capital of India")
		print(result.content)
	except ChatGoogleGenerativeAIError as error:
		print(f"Gemini request failed: {error}")
from langchain_openai import ChatOpenAI
from dotenv import load_dotenv

load_dotenv()

# temperature is a parameter that control the randomness of a language model's output . it affects how creative or deterministic the responses are
# lower values (0.0 - 0.3) - More deterministic and predictable.
# Higher values(0.7 , 1.5) - More randomness , vreative and diverse.
# max_completion_tokens=10 -> we will get output in 10 words only , it tell's how many words you want in output.

model = ChatOpenAI(model='gpt-4' , temperature=1.8 , max_completion_tokens=10)

result = model.invoke("Suggest me 5 line poem on Cricket?")

# gives ans + additional knowlwdge
print(result)

#when you only want to fetch ans
print(result.contenet)
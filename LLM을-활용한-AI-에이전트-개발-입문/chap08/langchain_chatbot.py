from dotenv import load_dotenv
import os
from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage, AIMessage, SystemMessage

load_dotenv()
api_key = os.getenv('OPENAI_API_KEY')

llm = ChatOpenAI(model="gpt-4o", api_key=api_key)

messages = [
  SystemMessage("너는 사용자를 도와주는 상담사야.")
]

while True:
  user_input = input("사용자: ")

  if user_input == "exit":
    break

  messages.append(user_input)
  ai_response = llm.invoke(messages)
  messages.append(ai_response)
  print("AI: " + ai_response.content)
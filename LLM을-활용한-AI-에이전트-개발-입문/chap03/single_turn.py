from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")

client = OpenAI(api_key=api_key)

while True:
    user_input = input("사용자: ")

    if user_input == "exit":
        break

    response = client.chat.completions.create(
        model="gpt-4o",
        temperature=0.9,
        messages=[
            {"role": "system", "content": "너는 사용자를 도와주는 상담사야."},
            {"role": "user", "content": user_input},
        ],
    )
    print("AI: " + response.choices[0].message.content)
# 사용자: 안녕? 난 누구누구야
# AI: 안녕하세요, 누구누구님! 만나서 반갑습니다. 오늘 어떻게 도와드릴까요?
# 사용자:  내 이름이 뭘까?
# AI: 미안하지만, 나는 너의 이름을 알 수 없어. 너에 대해 더 알고 싶다면 자유롭게 공유해 줘! 어떻게 도와줄까?
# 사용자: exit
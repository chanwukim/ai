from openai import OpenAI
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.getenv("OPENAI_API_KEY")
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
  model="gpt-4o", 
  # 무작위성. 0에 가까울수록 안정적이고 일관, 1에 가까울 수록 창의적이고 일관되지 않음
  temperature=0.1, 
  # system: GPT의 역할
  # user: ㅅ사용자
  # assistant: GPT의 답변
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "2022년 월드컵 우승팀은 어디야?"}
  ]
)

print(response)
print("---")
# response의 내용만 출력
print(response.choices[0].message.content)

# ChatCompletion(id='chatcmpl-CXTtgRIluJe686ZIwLnhSIG3UKPjq', choices=[Choice(finish_reason='stop', index=0, logprobs=None, message=ChatCompletionMessage(content='2022년 FIFA 월드컵에서는 아르헨티나가 우승을 차지했습니다. 아르헨티나는 결승전에서 프랑스를 상대로 승리하여 월드컵 트로피를 들어올렸습니다.', refusal=None, role='assistant', annotations=[], audio=None, function_call=None, tool_calls=None))], created=1762095784, model='gpt-4o-2024-08-06', object='chat.completion', service_tier='default', system_fingerprint='fp_65564d8ba5', usage=CompletionUsage(completion_tokens=52, prompt_tokens=30, total_tokens=82, completion_tokens_details=CompletionTokensDetails(accepted_prediction_tokens=0, audio_tokens=0, reasoning_tokens=0, rejected_prediction_tokens=0), prompt_tokens_details=PromptTokensDetails(audio_tokens=0, cached_tokens=0)))
# ---
# 2022년 FIFA 월드컵에서는 아르헨티나가 우승을 차지했습니다. 아르헨티나는 결승전에서 프랑스를 상대로 승리하여 월드컵 트로피를 들어올렸습니다.
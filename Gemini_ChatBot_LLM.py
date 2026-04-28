import google.generativeai as genai
import os

genai.configure(api_key="*****")
model=genai.GenerativeModel("gemini-3.1-flash-lite-preview") #if we use hugging we need to give that name
chat=model.start_chat(history=[])# to remember the prev chat
print("Knowledge Bot(Type 'exit' to quit)")


print(" Welcome! Ask me anything, I'm happy to help you! ")
while True:
    user_input=input("You: ") # the user input given here which will be sent to chatbots
    if user_input.lower() in ["exit", "quit", "bye"]: # it will exit if user these words in lower
        break
    response = chat.send_message(user_input) # response will be sent to user msg
    print(f"Gemini:{response.text}") # we will get the resp in text format
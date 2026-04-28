from openai import OpenAI
client=OpenAI(api_key="******")
def start_chatbot():
    messages=[{" Role":"system","content": "You are a helper and assisstant"}]
    print(" TeamEverest Chatbot, Type 'quit' to exit")

    while True:
        user_input=input("you:  ")
        if user_input.lower() in ["quit", "exit"," stop"]:
            break
        messages.append({"role":"user","content": user_input})
        response= client.chat.completions.create(
            model="gpt-4o-mini",
            messages=messages,
            temperature=0.7
        )

        assisstant_reply=response.choices[0].message.content
        print(f" TeamEverest :{assisstant_reply}")
        messages.append({"role":"assisstant","content":assisstant_reply})

if __name__ == "__main__":
    start_chatbot()
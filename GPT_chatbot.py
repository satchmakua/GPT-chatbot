import openai

openai.api_key = "Enter your unique API key here"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=40,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message.strip()

while True:
    user_prompt = input("User: ")
    if user_prompt == "exit":
        break
    else:
        response = generate_response(user_prompt)
        print("GPT: " + response)

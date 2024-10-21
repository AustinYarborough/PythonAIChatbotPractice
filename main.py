import openai   
# pip install openai

openai.api_key = ""
# make sure to put your project key from openai.com

def chat_with_gpt(prompt):
    response = openai.ChatCompletion.create(
        model="gpt-3.5-turbo",
        messages=[{"role": "user", "content": prompt}]
    )

    return response.choices[0].message.content.strip()
#also for this setup i'm using gpt3.5 turbo but it should be interchangeable with other versions

if __name__ == "__main__":
    while True:
        user_input = input("You: ")
        if user_input.lower() in ["quit", "close", "makeway"]:
            break

        response = chat_with_gpt(user_input)
        print("Chatbot: ", response)


#in VSC terminal run the name of the python file then you can start chating
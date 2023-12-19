from openai import OpenAI

api_key = "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"
client = OpenAI(api_key=api_key)

response = client.chat.completions.create(
    model="gpt-3.5-turbo",
    messages=[
        {"role": "system", "content": "You are a helpful assistant."},
        {"role": "user", "content": "capital of india?"},
    ],
    temperature=1,
    max_tokens=256,
    top_p=1,
    frequency_penalty=0,
    presence_penalty=0
)



# Assuming response is an object of ChatCompletion class
choices = response.choices  # Replace 'choices' with the actual attribute/method name

# Accessing the content from the first choice's message
content = choices[0].message.content  # Replace 'message' and 'content' with the actual attribute/method names

# Print the content
print(content)






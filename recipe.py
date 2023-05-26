import openai

openai.api_key = "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"

def generate_response(prompt):
    completions = openai.Completion.create(
        engine="text-davinci-002",
        prompt=prompt,
        max_tokens=1024,
        n=1,
        stop=None,
        temperature=0.5,
    )

    message = completions.choices[0].text
    return message

prompt = "What ingredients do I need to make chicken and rice?"
print(generate_response(prompt))

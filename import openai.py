import openai

# Set up your OpenAI API key
openai.api_key = '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'

def get_recipe(query):
    # Generate a response from Food Wizard
    response = openai.Completion.create(
        engine='text-davinci-003',
        prompt=f"I want a recipe for {query}.",
        max_tokens=100,
        temperature=0.6,
        n=1,
        stop=None,
        timeout=15
    )
    
    # Extract the generated recipe from the response
    recipe = response.choices[0].text.strip().replace("\n", " ")
    
    return recipe

# Example usage
recipe_query = "chocolate chip cookies"
recipe = get_recipe(recipe_query)
print(recipe)

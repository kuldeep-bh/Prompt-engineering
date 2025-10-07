#

def generate_prompts_from_data(data_list):
    prompts = []
    for item in data_list:
        prompt = f"explain {item} in simple terms."
        prompts.append(prompt)
    return prompts

# sample data list
data_list = ["quantum computing","machine learning","climate changes"]

# Generate prompts
prompts = generate_prompts_from_data(data_list)

# print each prompt
for prompt in prompts:
    print(prompt)
# generating prompt using python loop

topics = ["artificial intelligence","space exploration","ancient history"]
tones = ["serious","humorous","inspirational"]


#create a list of prompts based on combinations of topics and tones
prompts = []
for topic in topics:
    for tone in tones:
        prompt = f"Write a {tone} story about {topic}."
        prompts.append(prompt)
        
        
# print all generated prompts 
for prompt in prompts:
    print(prompt)
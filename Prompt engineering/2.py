
#creating prompt based on user input


def create_prompt():
    topic = input("Enter the topic for the story: ")
    tone = input("Enter the tone(e.g., humorous,adventurus):")
    
    prompt = f"Write a {tone} story about {topic}."
    return prompt 

# generate prompt based on user input 

user_prompt = create_prompt()
print("Generated prompt:",user_prompt)


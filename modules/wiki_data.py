import wikipedia


def wiki_save(prompt):
    # Get Wikipedia page content based on the prompt
    content = wikipedia.page(prompt)

    # Display information
    print("Title:", content.title)

    # Save content to a text file
    file_path = f"{prompt.lower().replace(' ', '_')}.txt"

    with open(file_path, 'w', encoding='utf-8') as file:
        file.write(content.content)

    print(f"Content has been written to {file_path}")


prompt = input('What do you want to know?')
wiki_save(prompt)

from emojifier import Emojifier

emoji = Emojifier.of_default_mappings()

print(emoji.generate_emojipasta(text="you are nice"))

# Output: you 😂 are 🙏🍑 nice 😍

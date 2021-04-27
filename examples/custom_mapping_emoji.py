from emojifyer import Emojifyer

emoji = Emojifyer("emoji-mappings.json")

print(emoji.generate_emojipasta(text="python is awesome"))

story = """
Today, I went to the {place} and saw a {adjective} {noun}. 
It was {verb} very {adverb}. 
I couldn't believe my {body_part}!
"""

place = input("Enter a place: ")
adjective = input("Enter an adjective: ")
noun = input("Enter a noun: ")
verb = input("Enter a verb ending in -ing: ")
adverb = input("Enter an adverb: ")
body_part = input("Enter a body part: ")

filled_story = story.format(place=place, adjective=adjective, noun=noun, verb=verb, adverb=adverb, body_part=body_part)

print("\nHere is your Mad Libs story:")
print(filled_story)

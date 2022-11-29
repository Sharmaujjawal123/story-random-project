import random
word1 = ['question','code','comment']
word2 = ['penguins','programmer jokes','text generation','another amazing fireworks','finding your partner']
word3 = ['C#','C++','Python','Javascript','Java','code']
word4 = ['liked','disliked','reported','deleted']

Sentence = [
    'Yesterday','while browsing Youtube and','activity',',','mainChar','noticed that',
    'rivalName','posted a new','word1','about','word2','.He','world4','it and challenged his'
    'word3','battle.Then he posted his own','posAdj',' ','word1',',but','rivalName','retaliaze'
     ,'negAdj','word1','about','word2','.']
# item is the item of the list

for item in Sentence:
    if item == "activity" : Sentence[Sentence.index(item)] = "activity" # index -> list[index] =
    elif item == "mainChar" : Sentence[Sentence.index(item)] = "mainChar"
    elif item == "rivalName" : Sentence[Sentence.index(item)] = "rivalName"
    elif item == "posAdj" : Sentence[Sentence.index(item)] = "posAdj"
    elif item == "negAdj" : Sentence[Sentence.index(item)] = "negAdj"
    elif item == "word1" : Sentence[Sentence.index(item)] = random.choice(word1)
    elif item == "word2" : Sentence[Sentence.index(item)] = random.choice(word2)
    elif item == "word3" : Sentence[Sentence.index(item)] = random.choice(word3)
    elif item == "word4" : Sentence[Sentence.index(item)] = random.choice(word4)
    else:    continue
# story
    story = " ".join(item for item in Sentence)
    print(story)
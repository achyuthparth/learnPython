# matrix addition

m = [[1, 2, 3,],
	 [4, 5, 6,],
	 [7, 8, 9]]

print(m)

print(m[1])

print((m[1]+m[2]))

col2 = [row[1] for row in m]
print(col2)

diag = [m[i][i] for i in [0, 1, 2]]
print(diag)

print({sum(row) for row in m})


man1 = {'name': {'first' : 'jon', 'last' : 'smith'},
		'jobs' : ['fireman', 'gamer'],
		'age' : 25}

print(man1)

print(man1['name'])

print(man1['name']['first'])

man1['jobs'].append('janitor')
print(man1)

#emoji converter function

def emoji_converter(message):
	words = message.split
	emojis = {
		";(": "😥",
		";)": "😂"
		}
	output = ""
	for word in words:
		output +=	emojis.get(word, word) + " "
	return output



message = input("enter a message ")
print(emoji_converter(message))
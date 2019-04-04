books = open('books.txt', 'r')
sents = open('single_sent.txt', 'w')
bookss = books.readlines()


def find(s, ch):
    return [i for i, ltr in enumerate(s) if ltr == ch]

start = 0
for book in bookss:
	start = 0
	bar = find(book, '|')
	if len(bar) == 0:
		sents.write(book)
		continue
	for i in bar:
		sents.write(book[start:i - 1] + "\n")
		start = i + 2
	sents.write(book[start:len(book)])

# To do: splite colocation from sents


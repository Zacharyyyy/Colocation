on_sens = open('only_sent.txt', 'r')
labels = open('labeled.txt', 'w')
ons = on_sens.readlines()

def masking(word, second):
	print(word)
	print(second)
	if word == "":
		#print(second)
		return "fucked"
	result = ""
	seconds = second.split(" ")
	for w in seconds:
		if word in w:
			if len(w) - len(word) < 3:
				w = w.replace(word, "[mask]")
		result = result + w + " "
	result = result[:len(result)-2] + word + "\n"
	return result

k = 0
for sent in ons:
	i = 0
	for w in sent:
		if w.isupper():
			break
		i = i + 1
	first = sent[:i]
	second = sent[i:]
	final = second

	first_1 = first.split(',')
	for sent_1 in first_1:
		breaker = 0
		first2 = sent_1.split(' ')
		for sent2 in first2:
			first3 = sent2.split('/')
			for word in first3:
				if word in second:
					result = masking(word, second)
					if not result == "fucked":
						labels.write(result)
					breaker = 1
		if breaker:
			break

				




from summa import summarizer
from summa import keywords
# from nltk.stem import WordNetLemmatizer


class Summry:
	
	def __init__(self, file_path, file_name):
		self.file_path = file_path
		self.filename = file_name
		self.file_content = str(open(f'{self.file_path}/{self.filename}').readlines())
		

	def getKey(self):
		self.key = keywords.keywords(self.file_content)
		return self.key.split('\n')

	def summ(self):
		return summarizer.summarize(str(self.file_content), ratio=0.33)

	# def get_Lemma(self):
	# 	self.lemma = WordNetLemmatizer()
	# 	self.key_lemma = []
	# 	self.keys = self.getKey()

	# 	for i in self.keys:
	# 		self.keys.append(self.lemma.lemmatize(i))

	# 	return tuple(self.keys)


	def create_file(self):
		self.new_file = open(f'{self.file_path}/{self.filename}sum', 'w')

		self.key = self.getKey()
		self.sum = self.summ()
		# self.lemmas = self.get_Lemma()

		self.new_file.write(self.sum)
		self.new_file.write('\n')
		self.new_file.write('\n')
		self.new_file.write(str(self.key))
		# self.new_file.write('\n')
		# self.new_file.write('\n')
		# self.new_file.write(str(self.lemmas))

		self.new_file.close()

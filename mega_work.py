from mega import Mega

class Mega_worker():
	def __init__(self, email, password):
		self.mega = Mega()
		self.mega = self.mega.login(email, password)

	def get_files(self, h):
		if(h == ""): h = 2 #to display root
		all_files = self.mega.get_files_in_node(h)
		output = []

		for file in all_files.values():
			file_stat = {}
			file_stat['name'] = file['a']['n']
			file_stat['type'] = file['t'] #0 - file; 1 - dir
			if(file_stat['type'] == 0): file_stat['size'] = file['s']
			file_stat['h']    = file['h']
			output.append(file_stat)

		return output

	def get_link(self, h):
		return self.mega.export(node_id=h)
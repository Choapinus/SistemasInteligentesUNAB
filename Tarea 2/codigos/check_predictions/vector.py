class Vector():
	def __init__(self, s_list, pred_list):
		self.true_positive = 0
		self.true_negative = 0
		for i in range(len(s_list)):
			if s_list[0] == pred_list[0]:
				self.true_positive += 1
			else:
				self.true_negative += 1

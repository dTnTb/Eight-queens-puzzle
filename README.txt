Question: https://en.wikipedia.org/wiki/Eight_queens_puzzle

method: backtracing

Pesudo code

check(): whether conflict in checkboard, if there is, return 0;

backtracing(row,col,num):
	if can't check():
		return 0
	for each col in the row
		apply one can try backtracing:
		if backtracing success:
			return 1
		else
			apply 0
	return 0 for no col could be applied in this row

Next question:
->print all solution
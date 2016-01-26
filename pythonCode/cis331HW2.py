import operator

cipher = "JBRTXGFYNRZXWRCSCMDJIXNBZRVRONVVLLZLBYQUXRWXGPGYJCUEMHYGYFVMSFPAIGWGWKQCFIAPFFMGPTLVUCPWEXVANBBPOVXZSICHCJHQDTVKRWNTACKXBBDTVRWXGWUPPOIEEPVUKUPSLEIMUALAEKNLNTACKQYFMPXKACOCIIJJFYWLLVUCPWEXVAMGWQILBYQQCGFWARAIIUXLVADPRCYQIGIRBQUMGIWRRRLLMEPUVZRVRONNVSQRWSSWGQJXZIBDPMNLGQRECCUXMDJWJHQTPRURHTIXVTAUSBREEWIGXTVWXLZBWINXLQPTPZLICBTVZBUQIEXVMZEWBXYNZEMCGYUUAOJEXNBYQRSGCLRKDMENXOGVYJCUIMESECIALPQTXOEBXRNQCPPDVZPCAIIIJOLBUILVPLRMZLVUCKPTPZGMCQGECFBVZAGFWPBTJXZXHNVSTKNLBVLMEPQRQCXVALHXISLAHBZBECUSFKWIUDFRLEPRRHGMMXWXLGPTJFUFBEXRXVYFAPKVFYYKDQVCIPWBTLCYEICHZWZBZBEKRIAARMVWWRBWVVNNUZTIFWYJMWEMNUSMLIOCLNKWECUYAOTWWXLBCGTRANVKJPRAFLWQWVAPNVIXIJCAMTWKQYTIBIZBVVOVIICBNVNSLJLRJJXPXOZINCVCVRBWITAOPQPPGRYPMWICRWBXIIIBQRZTHVEYYWEIUJHQJJMCCXHZXRXCBRNXVJCBNTUGVWNHZNSWOFVOWXNRNUBWIWXWXMLYCOZJJTMEPNUMUMIBNBXTVRCCBVPPYNFVKDTKNLVVHSDNBRTXGFYNRZHVVJWUMSPZVCGMSTIXXHKIMFWVHBXXNJMAWIYECCYBWEKJBRTXGFYNRZSIJRAAMSFPRABZHMBXLFSNVVJWUMSJLUFFKPPVYLBLJGKRIAEXXYJCEKGEWCVHQAXKQIHOWQFBNRIGPZNLQMHMXWMHATHDXLRBWEEXHRUPMEAIGWGMKRMGPTWZWAYMBEZWLBBDVNRNUICXZCIEYJIKJCYZDXFAWBVUMXDLNBXSECBNBWEJKYPWBIKQYZWHXTXGZWCLVUCPWEXVAWBVUMXDLNBXSE"
def findRepeatSpacing(code):
	# spacing = {} 
	# for wordSize in range(3, 7):
	# 	for index in range(len(code) - wordSize):
	# 		current = code[index:(index + wordSize)]
	# 		for i in range(index + wordSize, len(code) - wordSize):
	# 			if code[i:(i + wordSize)] == current:
	# 				if current not in spacing:
	# 					spacing[current] = [] 
	# 				spacing[current].append(i - index)

	# return spacing
	spacing = {} 
	for wordSize in range(3, 7):
		for index in range(len(code) - wordSize):
			current = code[index:(index + wordSize)]
			for i in range(index + wordSize, len(code) - wordSize):
				if code[i:(i + wordSize)] == current:
					if (i-index) not in spacing:
						spacing[i-index] = 0
					spacing[i-index] = spacing[i-index] + 1
	return sorted(spacing.items(), key=operator.itemgetter(1))

def ceaserSolve(code):
	# code.upper()
	frequencies = list(range(26))
	for i in range (len(frequencies)):
		frequencies[i] = 0
	#print(ord(code[0])-65)
	for i in range (len(code)):
		frequencies[ord(code[i])-65] = frequencies[ord(code[i])-65] + 1
	for i in range (len(frequencies)):
		frequencies[i] = frequencies[i]/len(code)
	# print(frequencies)
	return bestFitKey(frequencies)

def bestFitKey(freq):
	standard = [8.167, 1.492, 2.782, 4.253, 12.702, 2.228,
			2.015, 6.094, 6.966, 0.153, 0.772, 4.025, 2.406, 6.749, 7.507,
			1.929, 0.095, 5.987, 6.327, 9.056, 2.758, 0.978, 2.360, 0.150,
			1.974, 0.074]
	t = 0
	tScore = 10000000000000000.0
	for i in range(26):
		current = 0
		for j in range(26):
			current = current + (freq[((i+j)%26)]-standard[j])**2
		# print (i)
		# print(current)
		if current < tScore:
			tScore = current
			t = i
	return t
	
def findKey(code, split):
	key = []	
	letters = []
	for i in range (split):
		for j in range (i,len(code), split):
			letters.append(code[j])
		key.append(ceaserSolve(letters))
		letters = []
	return key

def solve(code, key):
	answer = ""
	for i in range(len(code)):
		answer = answer + chr((ord(code[i])-65-key[i%len(key)])%26+65)
	return answer


# print (findKey(cipher, 7))
# print (solve(cipher, [9, 20, 13, 8, 15, 4, 17]))
print (solve(cipher, findKey(cipher, 7)))
# print (findRepeatSpacing(cipher))


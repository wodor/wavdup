import sys,wave

def writeWav(duplcateResult, duplicateSubject):
	while(1):
		b = duplicateSubject.readframes(1000)
		if not b:
			break
		duplcateResult.writeframesraw(b)

	duplicateSubject.rewind()
	return duplcateResult	


duplicateSubjectName = sys.argv[1]
try:
	timescount = int(sys.argv[2])
except IndexError:
	timescount = 2

duplicateSubject = wave.open(duplicateSubjectName,'r')
duplcateResult = wave.open(duplicateSubjectName.replace('.wav','') + 'x' + str(timescount) + '.wav','wb')
duplcateResult.setparams(duplicateSubject.getparams())

for i in range (0,timescount):
	duplcateResult = writeWav(duplcateResult, duplicateSubject)



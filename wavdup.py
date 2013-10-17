import sys,getopt,wave

def writeWav(duplcateResult, duplicateSubject):
	while(1):
		b = duplicateSubject.readframes(1000)
		if not b:
			break
		duplcateResult.writeframesraw(b)

	duplicateSubject.rewind()
	return duplcateResult	

opts, args = getopt.getopt(sys.argv[1:], "n:")

for opt, val in opts:
	if opt == '-n':
		try:
			timescount = int(val)
		except ValueError:
			print "timescount (-n) must be an integer"
			exit(2)

duplicateSubjectName = args[0];

duplicateSubject = wave.open(duplicateSubjectName,'r')
duplcateResult = wave.open(duplicateSubjectName.replace('.wav','') + 'x' + str(timescount) + '.wav','wb')
duplcateResult.setparams(duplicateSubject.getparams())

for i in range (0,timescount):
	duplcateResult = writeWav(duplcateResult, duplicateSubject)

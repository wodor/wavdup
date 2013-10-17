import sys,getopt,wave

def writeWav(duplcateResult, duplicateSubjects):
	for duplicateSubject in duplicateSubjects:
		while(1):
			b = duplicateSubject.readframes(10000)
			if not b:
				print "written " + str(duplicateSubject) + " " + str(duplicateSubject.getnframes())
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

duplicateSubjects = [];
try:
	for name in args:
		duplicateSubjects.append(wave.open(name,'r'))
#	duplicateSubject = wave.open(duplicateSubjectName,'r')
	duplcateResult = wave.open(args[0].replace('.wav','') + 'x' + str(timescount) + '.wav','wb')
except IOError as e:
	print str(e)
	exit(2)

duplcateResult.setparams(duplicateSubjects[0].getparams())

for i in range (0,timescount):
	duplcateResult = writeWav(duplcateResult, duplicateSubjects)

print "written " + str(duplcateResult.getnframes()) + " frames"

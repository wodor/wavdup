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

outputdir = '.'
opts, args = getopt.getopt(sys.argv[1:], "n:d:")

for opt, val in opts:
	if opt == '-d':
		outputdir = val
	if opt == '-n':
		try:
			timescount = int(val)
		except ValueError:
			print "timescount (-n) must be an integer"
			exit(2)

duplicateSubjects = [];
duplicateSubjectNames= [];

try:
	for name in args:
		duplicateSubjects.append(wave.open(name,'r'))
		duplicateSubjectNames.append(name.split('/')[-1].replace('.wav',''))

	duplicateResultName = outputdir + '/' + '+'.join(duplicateSubjectNames) + 'x' + str(timescount) + '.wav'
	duplcateResult = wave.open(duplicateResultName,'wb')
except IOError as e:
	print str(e)
	exit(2)

duplcateResult.setparams(duplicateSubjects[0].getparams())

for i in range (0,timescount):
	duplcateResult = writeWav(duplcateResult, duplicateSubjects)

print "written " + str(duplcateResult.getnframes()) + " frames to " + duplicateResultName

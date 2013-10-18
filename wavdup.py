#!/usr/bin/env python
import sys,getopt,wave
def help():
	help = "Usage:  wavdup.py wav1 [wav n ...] [-n repeat count] [-d output dir]"
	return	help 
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
timescount = 1
opts, args = getopt.getopt(sys.argv[1:], "n:d:")

for opt, val in opts:
	if opt == '-d':
		outputdir = val
	if opt == '-n':
		try:
			timescount = int(val)
		except ValueError:
			print "repeat count (-n) must be an integer"
			exit(2)

if len(args) < 1:
	print help()
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

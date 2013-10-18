Wavdup
------

Simple console program which joins and repeat wav files. 
Intended to quickly prepare loops for Digitech JamMan or similiar.

You can simply multiply the length of wav:

	./wavdup.py  -n 4 ../loopA.wav

or create pattern, like this: 

	./wavdup.py  ../loopA.wav ../loopB.wav ../loopB.wav ../loopA.wav

or use both options and set output dir:

	./wavdup.py  -n 2 -d ".." ../loopA.wav ../loopB.wav

Please forgive me brutal simplicity of this single-purpose tool
'''
Ho fatto questo script per rinominare le canzoni estratte da CD musicali.


Target example:		 	01_12 - Ghali - Vida
Command example: 		python3 rm_tracks_number.py ~/Music/Ghali/ '^\d{,2}[-_\s]+\d{,2}[-_\s]+'

NB: Si dovrà inserire il regex tra due apici per evitare che la shell interpreti i caratteri speciali
'''

import shutil
import os
import re
import sys

def main(path, regex):
	# Create regex and make path absolute
	tracks_re = re.compile(regex)
	path = os.path.abspath(path)
	# Print working directory
	print('Current directory: {}'.format(path))
	os.chdir(path)
	# Check every file
	for filename in os.listdir(path):
		result = tracks_re.search(filename)
		if result:
			re_start, re_end = result.span()
			print('{} ---> {}'.format(filename, filename[re_end:]))
			shutil.move(filename, filename[re_end:])


if __name__ == '__main__':
	if len(sys.argv) != 3:
		print('Usage: python3 rm_tracks_number.py PATH \'REGEX\'')
		exit()
	else:	
		main(sys.argv[1], sys.argv[2])



#!/usr/bin/env python

import re
FILE = "docker-compose.yml"

def find_matches():
	matches = []
	pattern = r'\${([^}]+)}' 
	with open(FILE) as file:
		lns = file.readlines()
	for line in lns:
		match = re.findall(pattern=pattern,string= line)
		if match:
			m = match[0]
			matches.append(m)
	return matches
def main():
	matches = find_matches()
	print(matches)


if __name__ == "__main__":
	main()
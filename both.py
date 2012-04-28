import sys
import subprocess
import time

def makeCommands(L):
	while "++" in L:
		i = L.index("++")
		yield L[:i]
		L = L[i+1:]
	yield L

if __name__ == "__main__":
	args = sys.argv[1:]

	if len(args) <= 0:
		print "both - run some commands at once (because windows is silly.)"
		print "2012 Peter Swire - swirepe.com"
		print "Input commands (and their arguments) separated by ++"
		print "If you want this to be verbose, it has to be the first argument."
		print "Example usage:"
		print "    both a.exe ++ b.exe"
		print "    "
		print "    both --verbose a.exe ++ b.exe ++ c.exe"
		print "    "
		print "    both a.exe ++ b.exe barg1 barg2 ++ c.exe"
		print "    "
		print "    both ping google.com ++ echo Hello world!"
		print "    "
		print "    both pandoc --to=html from=markdown --data-dir=md ++ mv *.html *.php"
		
		sys.exit(0)

	# get the verbose setting
	verbose = False
	if args[0] in ["-v", "--verbose"]:
		verbose = True
		args = args[1:]


	# run each of the commands in parallel
	ps = []
	for command in makeCommands(args):
		if verbose:
			print "[BOTH]", " ".join(command)
		ps.append(subprocess.Popen(command))
	
	
	# if all of them have completed, stop running
	while True:
		time.sleep(0.1)
		for p in ps:
			p.poll()
			
		if not any([p.returncode == None for p in ps]):
			if verbose:
				print "[BOTH] Exiting with", len(ps), "commands completed."

			sys.exit(0)


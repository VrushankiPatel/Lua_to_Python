import re

class the:
	def __init__(self) -> None:
		self.the = {}
		self.help = """CSV : summarized csv file
        (c) 2022 Tim Menzies <timm@ieee.org> BSD-2 license
        USAGE: lua seen.lua [OPTIONS]
        OPTIONS:
        -e  --eg        start-up example                      = nothing
        -d  --dump      on test failure, exit with stack dump = false
        -f  --file      file with csv data                    = ../data/auto93.csv
        -h  --help      show help                             = false
        -n  --nums      number of nums to keep                = 512
        -s  --seed      random number seed                    = 10019
        -S  --seperator feild seperator                       = ,"""



	


	def func_the(self):
		help = self.help
		reexp = r"[-][\S]+[\s]+[-][-]([\S]+)[^\n]+= ([\S]+)"
		dictre = re.findall(reexp,help)
		for key , value in dictre:
				self.the[key] = self.coerce(value)
		return self.the
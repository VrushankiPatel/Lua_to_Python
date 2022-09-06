import re


def coerce(s: str):
	try: 
		return int(s)
	except ValueError:
		try:
			return float(s)
		except ValueError:
			match = re.search("^%s*(.−)%s*$")
			if match == "true":
				return True
			elif match == "false":
				return False
			else:
				return match

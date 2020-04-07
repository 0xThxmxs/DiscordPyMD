def bold(string):
	return "**{}**".format(string)


def code(string, language=""):
	return "```{}\n{}```".format(language, string)


def code_line(string):
	return "`{}`".format(string)


def italics(string):
	return "_{}_".format(string)


def strikethrough(string):
	return "~~{}~~".format(string)


def underline(string):
	return "__{}__".format(string)


def quote(string):
	return "> {}\n".format(string)


def quote_all(string):
	return ">>> {}\n".format(string)

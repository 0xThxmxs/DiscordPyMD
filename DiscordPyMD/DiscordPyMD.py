def bold(text):
	return "**{}**".format(text)


def code(text, language=""):
	return "```{}\n{}```".format(language, text)


def code_line(text):
	return "`{}`".format(text)


def italics(text):
	return "_{}_".format(text)


def strikethrough(text):
	return "~~{}~~".format(text)


def underline(text):
	return "__{}__".format(text)


def quote(text):
	return "> {}\n".format(text)


def quote_all(text):
	return ">>> {}\n".format(text)

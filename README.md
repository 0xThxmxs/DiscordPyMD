## DiscordPyMD is a little Python wrapper wich allow you to call functions for discord.py markdown.

[![Python 3.X](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/downloads/release/python-380/)

## Use

Import `DiscordPyMD.py` into the Discord Bot file.

```py
import DiscordPyMD.DiscordPyMD as dpymd # {as dpymd} is obviously optional.
```

### You will get access to it, you now able to use it !

![Functions](https://0xthxmxs.github.io/repo/img/project/dpymd/functions.png)

```
Functions :
- bold <text>
- code <text> <language - optional>
- code_line <text>
- italics <text>
- strikethrough <text>
- underline <text>
- quote <text>
- quote_all <text>
```

## Examples

```py
await ctx.send(bold("Bold is c00l !"))
```
```py
await ctx.send(quote("I have a headache.") + "Put yourself in rice.")

# OR

await ctx.send("{} Put yourself in rice.".format(quote("I have a headache.")))
```

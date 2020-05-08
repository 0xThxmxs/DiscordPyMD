# DiscordPyMD
### A little Python module wich allow you to call functions for discord.py markdown.

[![Python 3.X](https://forthebadge.com/images/badges/made-with-python.svg)](https://www.python.org/downloads/release/python-380/)

[![.dpymd_try](https://i.gyazo.com/7386ef0aacb95191700e6cc80916bddf.gif)](https://gyazo.com/7386ef0aacb95191700e6cc80916bddf)

# Use

Import `DiscordPyMD.py` into the Discord Bot file.

```py
import DiscordPyMD.DiscordPyMD as dpymd
# {as dpymd} is obviously optional.
```

### You will get access to it, you now able to use it !

![Functions](https://0xthxmxs.github.io/repo/img/dpymd.png)

```
List of functions :
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

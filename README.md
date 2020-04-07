# DiscordPyMD
### A little Python module wich allow you to call functions for discord.py markdown.

[![.dpymd_try](https://i.gyazo.com/7386ef0aacb95191700e6cc80916bddf.gif)](https://gyazo.com/7386ef0aacb95191700e6cc80916bddf)

# Use

Import `DiscordPyMD.py` into the Discord Bot file.

```py
import DiscordPyMD.DiscordPyMD ad dpymd
# {ad dpymd} is obviously optional.
```

### You will get access to it, you now able to use it !

![Functions](https://image.noelshack.com/fichiers/2020/15/2/1586273069-capture.png)

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

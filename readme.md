## firecat

Mess with files like a cat on fire.


# Introduction
An library for messing with files, like, append some content to some file.
``` python
import firecat

cat = firecat.firecat()

cat.apnd("Hello World!", "hw.txt")
```
And, seizing the opportunity, you can *read files*!
``` python
import firecat

cat = firecat.firecat()

rd = cat.read("hw.txt")
print(rd)
```
``` python
>>> Hello World!
```

*There are more commands/methods..*

# Compatibility
Only compatible with Python > 3.5

# Contribution
If you want to contribute with this *small-size* project, contribute!
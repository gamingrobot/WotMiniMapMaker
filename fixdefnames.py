import os
for filename in os.listdir("arena_defs"):
    num = filename[:2]
    name = filename[3:-4]
    os.rename("arena_defs/" + filename, "arena_defs/" + name + '_' + num + ".xml")

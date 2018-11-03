
import stat
import os
path = 'one.docx'
with open(path, 'w') as fh:
    fh.write('blabla\n')
st = os.stat(path)
os.chmod(path, st.st_mode | stat.S_IWOTH)

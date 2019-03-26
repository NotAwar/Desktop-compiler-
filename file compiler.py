import os
os.mkdir('trash_directory/')
from pathlib import Path
p = Path
p.mkdir()

from pathlib import Path

p = Path('trash_directory')
p.mkdir(exist_ok=True)


#get('/Desktop/)
#shutil.move("source_file_path", "destination_directory_path")
#os.makedirs("dir1/dir2") 
#shutil.rmtree("my_directory_path")

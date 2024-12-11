from pathlib import Path
from datetime import datetime

root_dir = Path('files')

for path in root_dir.glob("**/*"):
  if path.is_file():
    created_date = datetime.fromtimestamp(path.stat().st_ctime)
    created_date_str = created_date.strftime("%Y-%m-%d_%H:%M:%S")
    new_filename = created_date_str + '_' + path.name
    new_filepath = path.with_name(new_filename)
    path.rename(new_filepath)

# *Note: that the datetime.fromtimestamp(path.stat().st_ctime) will give you the amount of seconds when the file was created and the created_date.strftime("%Y-%m-%d_%H:%M:%S") will give you the date in the format of "YYYY-MM-DD_HH:MM:SS"


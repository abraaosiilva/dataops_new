import os

local_path = os.getcwd()

configs = {
      "bronze_path": f"{local_path}/app/python/data/bronze"
   }

def project_folders(configs):
   for f in configs.values():
      if not os.path.exists(f):
         os.makedirs(f)

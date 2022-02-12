#
# A generic Utils Lib to use in my everyday life
# version 1.0.0
#

import os
import shutil


def copy_blog_pages():
	source_folder = '../../3_2021_blog/public'
	#destination_folder = './copied'
	destination_folder = '../../4_2021_blog_gh_pages/2021_gh-pages'

	print('Copying')
	print('From ', os.path.abspath(source_folder))
	print('To ', os.path.abspath(destination_folder))

	#print(os.listdir(source_folder))
	
	#shutil.copytree(source_folder, destination_folder, dirs_exist_ok = True)
	shutil.copytree(source_folder, destination_folder, copy_function = shutil.copy, dirs_exist_ok = True)
	
	print('Done.')

def log_files_only():
	#dir_path = '/home/iam/Documents/1_dev/2_saumya/3_2021_blog/public'
	dir_path = '../../3_2021_blog/public/'

	files = []
	folders = []
	print('Path', dir_path)

	for path in os.listdir(dir_path):
		if os.path.isfile(os.path.join(dir_path, path)):
			files.append(path)
		else:
			#print('folder=', path)
			folders.append(path)
	
	print('|---------------------------')
	print('| Files ')
	print('|', files)
	print('| Folders ')
	print('|', folders)
	print('|---------------------------')

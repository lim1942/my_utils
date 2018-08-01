# -*- coding: utf-8 -*-
# @Author: lim
# @Date:   2018-07-27 09:24:33
# @Last Modified by:   lim
# @Last Modified time: 2018-08-01 15:56:36

import os
import time
import shutil


# >>> 需要配置四个的地方
# config user and radar`s path
USER = '何林'
JS_PATH = 'D:\\TRS\\TRSInforadar5.1\\trsrobot_update\\Script'
ALL_POINT_PATH = 'D:\\TRS\\TRSInforadar5.1\\trsrobot_update\\conf\\start.lst'
ALL_GROUP_PATH = 'D:\\TRS\\TRSInforadar5.1\\trsrobot_update\\conf\\group.lst'



# to record how many point has been export
POINT_INDEX = 0
# path for export 
PATH = 'export'
# path for zip export 
ZIP_PATH ='zip_export'

if not os.path.exists(PATH):
	os.mkdir(PATH)
if not os.path.exists(ZIP_PATH):
	os.mkdir(ZIP_PATH)
with open(ALL_POINT_PATH) as f:
	all_point = f.readlines()



def get_groups():
	"""get a all group list to export by radar config file """
	with open(ALL_GROUP_PATH) as f:
		_groups = f.readlines()
	groups = []
	for group in _groups:
		group = group.split(';')[0].replace('"','')
		groups.append(group)
	return groups


def get_name_date_path():
	""" return a export/name_date format str path"""
	date = time.strftime('%Y-%m-%d').replace('-0','-')
	name_date_path = os.path.join(PATH, (USER + '-' +date))
	return name_date_path


def ensure_path(path):
	""" to ensure a path for export and zip export"""
	path_index = 1
	while  True:
		real_path = path + '_' + str(path_index)
		if not os.path.exists(real_path):
			os.mkdir(real_path)
			return real_path
		else:
			path_index += 1


def export_group(group_name,name_date_path):
	"""exeport one group(group_name) from radar to dst path(name_date_path)"""

	global POINT_INDEX

	# Use flag to judge if group has it`s point 
	flag = 0

	# make inner group path
	group_path =os.path.join(name_date_path,group_name)
	if not os.path.exists(group_path):
		os.mkdir(group_path)

	# make module and script path in inner group path
	module_path = os.path.join(group_path,'Module')
	if not os.path.exists(module_path):
		os.mkdir(module_path)
	new_js_path = os.path.join(group_path,'Script')
	if not os.path.exists(new_js_path):
		os.mkdir(new_js_path)

	# parse point in all_point and then filter point by their group name
	group_file_name = os.path.join(group_path,(group_name+'.txt'))
	for point in all_point:
		point_fields = point.split(';')

		# get group_name source_js content_js fields
		_group_name = point_fields[-8].replace('"','')
		point_name = point_fields[2].replace('"','')
		source_name = point_fields[9].replace('"','')
		for i in point_fields[10:]:
			if '.js' in i and '_' in i:
				content_name = i.replace('"','')
				break

		# write point to their group export file and copy script to their export group path
		if _group_name == group_name:

			flag = 1

			# write point file
			with open (group_file_name,'a',encoding='gb2312') as f:
				f.write(point)

			# copy source js
			if source_name:
				source_path = os.path.join(JS_PATH,source_name)
				new_source_path = os.path.join(new_js_path,source_name)
				shutil.copyfile(source_path,new_source_path)
			# copyt content js
			if content_name:
				content_path = os.path.join(JS_PATH,content_name)
				new_content_path = os.path.join(new_js_path,content_name)
				shutil.copyfile(content_path,new_content_path)

			POINT_INDEX += 1
			print('Success do...{}  {}  {}  {} '.format(_group_name,point_name,source_name,content_name))

	if not flag:
		raise Exception(group_name,' has no points')


def all_export():
	"""get all group and export them"""

	# read all groups
	groups = get_groups()
	print('\n>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>>> total ',len(groups),' groups ',len(all_point),' points \n')
	print(groups)

	# filter need export group
	num = input('\n>>> Please enter a number of group to export low than 1 or over than groups`s length will export all _ ')
	if not num.isdigit():
		print('Illegal input !!!')
		os._exit(0)
	num = int(num)
	if num > len(groups) or num <= 0:
		num = len(groups)
	need_export = groups[:num]
	print('>>> You will export ',str(num),' groups \n')
	print(need_export,'\n')

	# gen days-root path for today`s export 
	name_date_path = ensure_path(get_name_date_path())

	# do export group
	group_wrong = []
	for group_name in need_export:
		try:
			export_group(group_name,name_date_path)
		except Exception as e:
			group_wrong.append(group_name)	
			print(e)

	print('\n\nSuccessful export {} points to {} groups... '.format(POINT_INDEX,num))
	if group_wrong:
		print('Unsuccessful do ',group_wrong,' groups`s inner one point ,please check out it !!!')
	print('\n\n')

	#return name_date_path for zip export
	return name_date_path


def get_zip_export(name_date_path):
	"""gen zip-export file by export file"""

	# gen days-root path for today`s zip-export
	zip_name_date_path = name_date_path.replace(PATH,ZIP_PATH)
	os.mkdir(zip_name_date_path)

	# get the unzip file dirctory and then use syetem`s interface make them to *.zip in zip_export/ 
	unzip_group_list = os.listdir(name_date_path)
	for group in unzip_group_list: 

		unzip_group_name = os.path.join(name_date_path,group)
		zip_group_name = os.path.join(zip_name_date_path,group+'.zip')
		print(zip_group_name)

		command = 'cd ' + unzip_group_name +' & winrar.exe a -k -r -s -ibck ..\\..\\..\\'+zip_group_name
		os.system(command)
		
	print('\n\nSuccessful exported {} group-zip  ... '.format(len(unzip_group_list)))


def main():
	name_date_path = all_export()
	get_zip_export(name_date_path)



if __name__ == '__main__':
	main()

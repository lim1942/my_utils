# -*- coding: utf-8 -*-
# @Author: lim
# @Date:   2018-07-27 09:24:33
# @Last Modified by:   lim
# @Last Modified time: 2018-07-27 17:15:26

import os
import xlrd
import chardet

from get_pinyin_first import get_pinyin_name



#config the need filter field`s index in excel (index- 1)
HOOK = 8
# point config tenplate
point_line = '"{}";"{}";"{}";"";{};0;0;1;2;"{}";"";"";"";"";"";"";"";0;1;"";"";0;0;"";"";"";1;1;1;1;1;"";"";"";"";"";"{}";"";"";"";"";"content+authors";"sitename+channel+urltitle";0;0;85;85;3;-1;"";"";"";"";"";"";0;0;"";"";"";"";"";"";0;1;1;1;"";80;"";"";"";"GB18030";0;1;"{}";0;0;"";"";"";1;"{}"\n'
# point config path in radar
all_point_file = 'D:\\TRS\\TRSInforadar5.1\\trsrobot_update\\conf\\start.lst'
# this path you can get a index of point in radar wicth you need to config a point
point_index_file = 'D:\\TRS\\TRSInforadar5.1\\trsrobot_update\\conf\\start.id'
# all group path in radar
all_group_file = 'D:\\TRS\\TRSInforadar5.1\\trsrobot_update\\conf\\group.lst'
# all js path in radar
js_path = 'D:\\TRS\\TRSInforadar5.1\\trsrobot_update\\Script'

# get content and source js tenplate
js_list = os.listdir(js_path)
with open('tenplate/content.js') as f:
    CONTENT = f.read()
with open('tenplate/source.js') as f:
    SOURCE  = f.read()

# get point index in radar
with open(point_index_file) as f:
    POINT_INDEX = int(f.read())

# num to record how many js group point you have been gen
JS_NUM = 0
GROUP_NUM = 0
POINT_NUM = 0



def read_point_list_from_excel():
    """function to get need config point by read excle and then return a point list"""

    # get a excel filename
    for filename  in os.listdir('.'):
        if '.xls' in filename:
            break

    # if has no excel process will exit
    if '.xls' not in filename:
        print("There has no excel in 'in' dirctory ...")
        os._exit(0)

    # get a excel table
    r_file = xlrd.open_workbook(filename)
    try:
        table = r_file.sheet_by_index(0)
    except Exception as e:
        print(e)
    if table.ncols < 9:
        return

    # return a need config point list
    line_con = []
    for i in range(table.nrows):
        row  = table.row_values(i)
        if not row[HOOK]:
            line = [row[0].strip(),row[3].strip(),row[5].strip()]
            line_con.append(line)
    return line_con



def gen_js_script_to_radar(keyword1,keyword2):
    """function to gen js to radar"""

    global JS_NUM

    # Get source js name and then write js-tenplate with this name in radar path and num +1
    # if script has already exist process will do nothing 
    source_name = get_pinyin_name(keyword1, keyword2, '1')
    if source_name not in js_list:
        JS_NUM +=1
        with open(os.path.join(js_path,source_name),'w',encoding='gb2312') as f:
            f.write(SOURCE)
    else:
        print('Source already exist >>> ',source_name)

    # get content js name and then write js-tenplate with this name in radar path and num +1
    # if script has already exist process will do nothing 
    content_name = get_pinyin_name(keyword1, keyword2, '0')
    if content_name not in js_list:
        JS_NUM +=1
        with open(os.path.join(js_path,content_name),'w',encoding='gb2312') as f:
            f.write(CONTENT)
    else:
        print('Content already exist >>> ',content_name)



def gen_group_to_radar(keyword1):
    """function to gen groups to radar group path"""

    global GROUP_NUM

    # open group file to get all group that's already there
    with open(all_group_file,encoding='gb2312') as f:
        con = f.read()

    # if group not exist process write them to file and num +1,esle do nothing
    f = open(all_group_file,'a',encoding='gb2312')
    if keyword1 not in con:
        GROUP_NUM += 1
        line = '"{}";0;7;30;0;"";0;24;0\n'.format(keyword1)
        f.write(line)
        f.close()
    else:
        print('\nGroup already exist >>> ',keyword1)


def gen_point_to_radar(keyword1,keyword2,url):
    """Gen point config detail to point file in radar"""

    global POINT_INDEX , POINT_NUM
    
    # gen a index of this point
    POINT_INDEX += 1
    index = str(POINT_INDEX)

    # get need config fields and then fill tenplate with these fields
    source_name = get_pinyin_name(keyword1, keyword2, '1')
    content_name = get_pinyin_name(keyword1, keyword2, '0')
    domin_name = url.replace('http://','').replace('wwww.','').split('/')[0]
    write_line = point_line.format(url,keyword1,keyword2,index,source_name,content_name,keyword1,domin_name)

    # open point config file to get all point that's already there
    with open(all_point_file,encoding='gb2312') as f:
        con = f.read()

    # if point not exist process write them to file and num +1,esle do nothing
    f = open(all_point_file,'a+',encoding='gb2312')
    if url not in con:
        POINT_NUM += 1
        f.write(write_line)
    else:
        print('Point already exist >>> ',keyword1,keyword2,url)



def dispatch():
    """Dispatch function. get points list and filter them
    this function only handle one point in a group"""

    # get points
    point_list = read_point_list_from_excel()

    # list to record witch group has been read
    record_list = []

    # get one point in one group to gen in radar
    for point in point_list:
        keyword1 = point[0]
        keyword2 = point[1]
        url = point[2]
        if keyword1 not in record_list:
            record_list.append(keyword1)
            gen_group_to_radar(keyword1)
            gen_point_to_radar(keyword1, keyword2, url)
            gen_js_script_to_radar(keyword1, keyword2)

    print('\n\nSuccessful read {} points and {} groups from excel ...'.format(len(point_list),len(record_list)))
    print('Successful write {} groups, {} points, {} scripts ...'.format(GROUP_NUM,POINT_NUM,JS_NUM))



if __name__ == '__main__':
    dispatch()

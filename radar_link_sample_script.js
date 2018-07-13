function radar_link(){
	this.source = '';
}

// 链接脚本，添加两个下标之间的链接
function TRS_Document_Link(urlname,urltitle,content){
    var rval = new radar_link();
    var begin_str = '';
    var end_str = '';
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    if (begin!=-1 && end !=-1){
        rval.source = content.substring(begin,end).replace(begin_str,'');
    }
    return rval
}

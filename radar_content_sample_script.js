function radar_content(){
    this.source = "";
    this.urltitle = "";
    this.srcname = "";
    this.authors = "";
    this.urltime = "";
    this.vreserved1 = "";
    this.vreserved2 = "";

}

function TRS_Document_Content(urlname,urltitle,content){
    var rval = new radar_content();

    // for content
    var begin_str = '';
    var end_str = '';
    var img_reg = /alt="\\"/g;
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    // rval.source = begin.toString();
    // rval.source = end.toString();
    if (begin!=-1 && end !=-1){
        rval.source = content.substring(begin,end).replace(begin_str,'').replace(img_reg,'');
    }

    // for urltitle
    var begin_str = '';
    var end_str = '';
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    // rval.source = begin.toString();
    // rval.source = end.toString();    
    if (begin!=-1 && end !=-1){
        rval.urltitle = content.substring(begin,end).replace(begin_str,'');
    }

    // for srcname
    var begin_str = '';
    var end_str = '';
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    // rval.source = begin.toString();
    // rval.source = end.toString();    
    if (begin!=-1 && end !=-1){
        rval.srcname = content.substring(begin,end).replace(begin_str,'');
    }

    // for authors
    var begin_str = '';
    var end_str = '';
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    // rval.source = begin.toString();
    // rval.source = end.toString();    
    if (begin!=-1 && end !=-1){
        rval.authors = content.substring(begin,end).replace(begin_str,'');
    }

    // for urltime
    var begin_str = '';
    var end_str = '';
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    // rval.source = begin.toString();
    // rval.source = end.toString();    
    if (begin!=-1 && end !=-1){
        rval.urltime = content.substring(begin,end).replace(begin_str,'');
    }

    // for vreserved1
    var begin_str = '';
    var end_str = '';
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    // rval.source = begin.toString();
    // rval.source = end.toString();    
    if (begin!=-1 && end !=-1){
        rval.vreserved1 = content.substring(begin,end).replace(begin_str,'');
    }

    // for vreserved2
    var begin_str = '';
    var end_str = '';
    begin = content.indexOf(begin_str);
    end = content.indexOf(end_str,begin);
    // rval.source = begin.toString();
    // rval.source = end.toString();    
    if (begin!=-1 && end !=-1){
        rval.vreserved2 = content.substring(begin,end).replace(begin_str,'');
    }    

    return rval
}

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
    //content = content.replace(/&nbsp;/gi,'')

    // for urltitle
        match_1 = content.match(/([\s\S]*?)/)
        if (match_1 && match_1.length>0){
            rval.urltitle = match_1[1]
        }  

    // for content
        match_2 = content.match(/([\s\S]*?)/)
        if (match_2 && match_2.length>0){
            rval.source = match_2[1]
        }

    // for srcname
        match_3 = content.match(/([\s\S]*?)/)
        if (match_3 && match_3.length>0){
            rval.srcname = match_3[1]
        }

    // for authors
        match_4 = content.match(/([\s\S]*?)/)
        if (match_4 && match_4.length>0){
            rval.authors = match_4[1]
        }

    // for urltime
        match_5 = content.match(/([\s\S]*?)/)
        if (match_5 && match_5.length>0){
            rval.urltime = match_5[1]
        }

    // for vreserved1
        match_6 = content.match(/([\s\S]*?)/)
        if (match_6 && match_6.length>0){
            rval.vreserved1 = match_6[1]
        }
    
    // for vreserved2
        match_7 = content.match(/([\s\S]*?)/)
        if (match_7 && match_7.length>0){
            rval.vreserved2 = match_7[1]
        }

    return rval
}

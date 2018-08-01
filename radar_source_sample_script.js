// 源码批量替换链接脚本实例 
function TRS_Document_Source(urlname,urltitle,content){
    if(urlname.indexOf('index')!=-1){
        var source;
        source = content.replace(/\.htm/g,'_0.htm');
        return source;
    }
}


// 源码排除异类结构网页H或跳转页面脚本实例
function TRS_Document_Source(urlname,urltitle,content){
    if(urlname.indexOf('index')!=-1){
        if (content.indexOf('中国景宁新闻网')==-1){
            content='<div></div>'
            return content;
        }
    }
}


// 源码脚本去除网页中的缩略图的链接
function TRS_Document_Source(urlname,urltitle,content){
    if(urlname.indexOf('index')==-1){
        var source;
        if (content.indexOf('0570-5011777')==-1 && content.indexOf('常山支站')==-1){
            content='<div></div>';
        }
        var reg = /<i\stitle="timg">(.+?)<\/i>/gi
        var reg2 = /<img.+?>/gi
        var reg4 = /<i\stitle="img">.+?<\/i>/gi
        source = content.replace(reg2,'').replace(reg3,'').replace(reg4,'').replace(reg,'<img src="http://img2.zjolcdn.com$1">');
        return source;
    }
}


 // 源码-翻页脚本实例
function TRS_Document_Source(urlname, urltitle, content){
    if(urlname.indexOf('index')==-1){
        var t = "";
        var k = 0;
        var buf = [];
        var t = content.match(/(\d+)\.shtml">尾页/i);
        if (t !=null){
            k = parseInt(t[1]);
            for(var i = 2;i <= k;i++){
                page = '_0'+ i;
                if (i>9){
                    page = '_'+ i;
                }
                buf.push('<a href="'+ urlname.replace('.shtml','').replace(/_\d*?\.shtml/ig,'') + page +'.shtml">'+ (i) +'</a>');
            }
        }  
        content+= '<div id="page">' + buf.join('') + '</div>';
    }
    return content;
}


//源码脚本，定向修改页面的结构
function TRS_Document_Source(urlname,urltitle,content){
    if (urlname.indexOf('index')!=-1){
        var begin_str = '<ul class="newslist" id="newslist">'
        var end_str = '</body>'
        begin = content.indexOf(begin_str)
        end = content.indexOf(end_str,begin)
        content = content.substring(begin,end) 

        var source
        reg = /\/art\/.*?\.html/g
        arr = content.match(reg)
        for(j = 0,len=20; j < len; j++){
            source += '<a href="'+'http://wzjgswj.wenzhou.gov.cn' + arr[j] +'">'+'</a>'+ '\n'
        }
        return source
    }
}


function TRS_Document_Source(urlname,urltitle,content){
    if(urlname.indexOf('content')!=-1){
    var str = 'page page'
      flag = content.indexOf(str)
      num = 0
      a_list = ''
      while (flag!=-1){
          flag =content.indexOf(str,flag)
          num +=1
          if(num>1){
	          url = urlnamel.replace('.htm','')+'_'+num.toString() +'.htm'
	          tag_a = '<a href="'+url+'">'+num.toString()+'</a>\n'
	          a_list += tag_a
          }
      }
	content += '<div id="page">' + a_list + '</div>';
	return content
  }
}



function TRS_Document_Source(urlname, urltitle, content){
    if(urlname.indexOf('ypjj')==-1){
        var t = "";
        var k = 0;
        var buf = [];
        var t = content.match(/_(\d+?)\.html/g);
        if (t.length>2){
            k = parseInt(t.pop().replace('_','').replace('.html',''));
            for(var i = 2;i <= k;i++){
                page = '_0'+ i;
                if (i>9){
                    page = '_'+ i;
                }
                buf.push('<a href="'+ urlname.replace('.html','').replace(/_\d*?\.html/ig,'') + page +'.html">'+ (i) +'</a>');
            }
        }  
        content+= '<div id="page">' + buf.join('') + '</div>';
    }
    return content;
}


function TRS_Document_Source(urlname,urltitle,content){
    if(urlname.indexOf('index')!=-1){
        url_list = content.match(/\/art\/\d*\/\d+\/\d+\/art_\d+_\d+.html/g)
        con = ''
        for (var i =0; i<15 ;i++){
           tag_a = '<a href="' +url_list[i] +'">' + i.toString() + '</a>\n'
           con += tag_a
        }
        content = con
        return content
    }
    else{
    	return content
    }
}

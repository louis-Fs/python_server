var paValue = new Array();//创建一个用于保存具体值得数组
var loc = location.href;
var n1 = loc.length;//地址的总长
var n2 = loc.indexOf("?");//取得=号的位置
var parameter = decodeURI(loc.substr(n2+1, n1-n2));//截取从?号后面的内容,也就是参数列表，因为传过来的路径是加了码的，所以要解码
var parameters  = parameter.split("&");//从&处拆分，返回字符串数组
var data = new FormData();
var jslength=0;
for (var i = 0; i < parameters.length; i++) {
    console.log("参数键值对值"+i+":"+parameters[i]);
    var m1 = parameters[i].length;//获得每个键值对的长度
    var m2 = parameters[i].indexOf("=");//获得每个键值对=号的位置
    var value = parameters[i].substr(m2+1, m1-m2);//获取每个键值对=号后面具体的值
    paValue[i] = value;}//将每个参数的值存入数组
$(document).ready(function(){
        var userid = paValue[0];
        data.append("userid",userid);
        var php_get_userinfo = "http://localhost/Dashboard/main-ltr/php/set_default_userinfo.php";
        var weibouser = new XMLHttpRequest();//第一步：建立所需的对象
        weibouser.open('POST',php_get_userinfo,true);//第二步：打开连接
        weibouser.send(data);//第三步：发送请求  将请求参数写在URL中
        weibouser.onreadystatechange = function (){
            if (weibouser.readyState == 4 && weibouser.status == 200) {
                var getuser = JSON.parse(weibouser.responseText);
                console.log(getuser);
                // document.getElementById("table_default_userinfo").innerHTML="<tr><td width='35%'>用户名usrname</td><td width='65%'><a href='#' id='inline-username' data-type='text' data-pk='1' data-title='Enter username'>"+getuser[1][0]+"</a></td></tr><tr><td>个人介绍userintrodution</td><td><a href='#' id='inline-firstname' data-type='text' data-pk='1' data-placement='right' data-placeholder='Required' data-title='Enter your firstname'>"+getuser[1][1]+"</a></td></tr><tr><td>性别gender</td><td><a href='#' id='inline-sex' data-type='select' data-pk='1' data-value='' data-title='Select sex'>"+getuser[1][2]+"</a></td></tr>";
            document.getElementById("inline-username").innerHTML=getuser[1][0];
            document.getElementById("inline-firstname").innerHTML=getuser[1][1];
            document.getElementById("inline-sex").innerHTML=getuser[1][2];            
            }
        }
        var php_get_weibo = "http://localhost/Dashboard/main-ltr/php/set_default_weibo.php";
        var weibo = new XMLHttpRequest();//第一步：建立所需的对象
        weibo.open('POST',php_get_weibo,true);//第二步：打开连接
        weibo.send(data);//第三步：发送请求  将请求参数写在URL中
        weibo.onreadystatechange = function (){
            if (weibo.readyState == 4 && weibo.status == 200) {
                var getweibo = JSON.parse(weibo.responseText);
                console.log(getweibo);
                var classtype = new Array();
                classtype[0]="odd";
                classtype[1]="even";
                // document.getElementById("table").className="table table-bordered table-separated";
                for(var count=1;count<=21;count++){
                    var default_innerhtml=document.getElementById("table_default_weibo").innerHTML;
                    // document.getElementById("table").className="table table-bordered table-separated";
                    $("#table").attr("class","table table-bordered table-separated");
                    document.getElementById("table_default_weibo").innerHTML=default_innerhtml+"<tr role='row' class="+classtype[(count)%2]+"><td  class='sorting_1' id='weibo_id"+count+"'>"+getweibo[count][0]+"</td><td tabindex='1' id='weibocontent_id"+count+"'>"+getweibo[count][1]+"</td></tr>";
                }
                
            }
        }
        $("#button_set_userinfo").click(function(){
            var username = document.getElementById("inline-username").innerHTML;
            var introduction = document.getElementById("inline-firstname").innerHTML;
            var gender = document.getElementById("inline-sex").innerHTML;
            var newdata = new FormData();
            newdata.append("userid",userid);
            newdata.append("username",username);
            newdata.append("introduction",introduction);
            newdata.append("gender",gender);
            var php_set_userinfo = "http://localhost/Dashboard/main-ltr/php/set_userinfo.php";
            var setuser = new XMLHttpRequest();//第一步：建立所需的对象
            setuser.open('POST',php_set_userinfo,true);//第二步：打开连接
            setuser.send(newdata);//第三步：发送请求  将请求参数写在URL中
            setuser.onreadystatechange = function (){
                if (setuser.readyState == 4 && setuser.status == 200) {
                    var setuser_return=setuser.responseText;
                    console.log(setuser_return);           
                }
            }
        })
        $("#button_set_weibo").click(function(){
            
            for(var count=1;count<=19;count++){
                var des_id="weibo_id"+count;
                var des_contentid="weibocontent_id"+count;
                var weibo_id = document.getElementById(des_id).innerHTML;
                // console.log(weibo_id);
                var weibocontent=document.getElementById(des_contentid).innerHTML;
                // console.log(weibocontent);
                var newdata = new FormData();
            newdata.append("weibo_id",weibo_id);
            newdata.append("weibo_content",weibocontent);
            var php_set_weibo = "http://localhost/Dashboard/main-ltr/php/set_weibo.php";
            var setweibo = new XMLHttpRequest();//第一步：建立所需的对象
            setweibo.open('POST',php_set_weibo,true);//第二步：打开连接
            setweibo.send(newdata);//第三步：发送请求  将请求参数写在URL中
            setweibo.onreadystatechange = function (){
                if (setweibo.readyState == 4 && setweibo.status == 200) {
                    var setweibo_return=setweibo.responseText;
                    console.log(setweibo_return);           
                }
            }
            }
            
        })
})
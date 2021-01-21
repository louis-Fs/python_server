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
    var searchkeywords=paValue[0];
    data.append("keywords",searchkeywords);
    var php_search = "http://localhost/Dashboard/main-ltr/php/search_user.php";
        var weibosearch = new XMLHttpRequest();//第一步：建立所需的对象
        weibosearch.open('POST',php_search,true);//第二步：打开连接
        weibosearch.send(data);//第三步：发送请求  将请求参数写在URL中
        weibosearch.onreadystatechange = function (){
            if (weibosearch.readyState == 4 && weibosearch.status == 200) {
                 var search_user = JSON.parse(weibosearch.responseText);
                 for(var js in search_user){
                    jslength++;
                  }  
                  console.log(jslength);
                 console.log(search_user);
                 for(var i=1;i<jslength;i++){
                    var table_search_weibo_innerhtml=document.getElementById("table_search_result").innerHTML;
                    document.getElementById("table_search_result").innerHTML=table_search_weibo_innerhtml+"<tr><td>"+search_user[i][0]+"</td><td>"+search_user[i][1]+"</td><td>"+search_user[i][2]+"</td></tr>";
                 }
                 document.getElementsByClassName("odd")[0].style.display="none";
            }
        }

})
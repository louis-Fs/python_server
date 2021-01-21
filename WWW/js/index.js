$(document).ready(function(){
    // $.ajax({
    //     url: "http://localhost/Dashboard/main-ltr/php/index.php",
    //     type: "get",
    //     dataType: "json",
    //     cache: false,
    //     processData: false,
    //     contentType: false, 
    //     success: function (data) {
    //         console.log(data[0]);
    //     }
    // });
    var php_new_weibo = "http://localhost/Dashboard/main-ltr/php/new_weibo.php";
        var weibocontent = new XMLHttpRequest();//第一步：建立所需的对象
        weibocontent.open('GET',php_new_weibo,true);//第二步：打开连接
        weibocontent.send();//第三步：发送请求  将请求参数写在URL中
        weibocontent.onreadystatechange = function (){
            if (weibocontent.readyState == 4 && weibocontent.status == 200) {
                 var new_weibo = JSON.parse(weibocontent.responseText);
                 for(var i=0;i<50;i++){
                    var table_new_weibo_innerhtml=document.getElementById("table_new_weibo").innerHTML;
                    document.getElementById("table_new_weibo").innerHTML=table_new_weibo_innerhtml+"<tr><td>"+new_weibo[i]+"</td></tr>";
                 }
            }
        }
        var php_new_user = "http://localhost/Dashboard/main-ltr/php/new_user.php";
        var weibouser = new XMLHttpRequest();//第一步：建立所需的对象
        weibouser.open('GET',php_new_user,true);//第二步：打开连接
        weibouser.send();//第三步：发送请求  将请求参数写在URL中
        weibouser.onreadystatechange = function (){
            if (weibouser.readyState == 4 && weibouser.status == 200) {
                 var new_user = JSON.parse(weibouser.responseText);
                 for(var i=1;i<100;i++){
                    var table_new_user_innerhtml=document.getElementById("table_new_user").innerHTML;
                    document.getElementById("table_new_user").innerHTML=table_new_user_innerhtml+"<tr><td>"+new_user[i][0]+"</td><td>"+new_user[i][1]+"</td></tr>";
                 }
            }
        }
    $("#userinfo_search").click(function(){
        window.location.href='userinfo_search.html';
    })
    $("#userrela_search").click(function(){
        window.location.href='userrela_search.html';
    })
    $("#weibo_search").click(function(){
        window.location.href='weibo_search.html';
    })
    $("#weibo_update").click(function(){
        window.location.href='update.html';
    })
})
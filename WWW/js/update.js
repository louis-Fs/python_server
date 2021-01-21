$(document).ready(function(){
    $("#weibo_update_button").click(function(){
        var userid = $("#input_userid").val();
        var password = $("#input_password").val();
        var data = new FormData();
        data.append("userid",userid);
        data.append("password",password);
        var php_verify = "http://localhost/Dashboard/main-ltr/php/verify.php";
        var weiboverify = new XMLHttpRequest();//第一步：建立所需的对象
        weiboverify.open('POST',php_verify,true);//第二步：打开连接
        weiboverify.send(data);//第三步：发送请求  将请求参数写在URL中
        weiboverify.onreadystatechange = function (){
            if (weiboverify.readyState == 4 && weiboverify.status == 200) {
                 var verify = weiboverify.responseText;
                 if(verify == "true"){
                     window.location.href="http://localhost/Dashboard/main-ltr/update_data.html?vuserid="+userid;
                 }
                    
            }
        }
    })
})
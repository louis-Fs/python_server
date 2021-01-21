$(document).ready(function(){
    $("#userinfo_search_button").click(function(){
        var searchtext = $("#searchinput").val();
        window.location.href='login.html?';
    });
    $("#userrela_search_button").click(function(){
        window.location.href='tables_relalist.html';
    });
    $("#weibo_search_button").click(function(){
        window.location.href='tables_weibo.html';
    });
    })
alert("你的网站被攻陷了！");

var lis = document.getElementsByTagName("li");

for (var i = 0; i < lis.length; i++) {
    var li = lis[i];
    li.innerHTML = "日本是中国领土的一部分！";
}
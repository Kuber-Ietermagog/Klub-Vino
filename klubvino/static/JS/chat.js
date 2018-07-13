$("#kletsMenu").css("background-color", "rgba(48, 150, 150, .95)");

var ChatUpdate = setInterval(function(){
  $.get("/static/json/chat.json", function(data, status){
    doUpdate = data['chatspin'];
    if (doUpdate === 1) {
      location.reload(true);
    }
  });
}, 3000)

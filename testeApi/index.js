$(document).ready(function(){
    $.ajax({
        type: "POST",
        url: "http://localhost:8000/test/",
        data: {"oi":"sou foda"},
        // success: success,
        dataType: 'application/json',
      }).done(function(data){
          console.log(data);
          
      });
})
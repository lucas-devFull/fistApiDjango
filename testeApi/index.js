$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "http://localhost:8000/listaPost/",
        // data: {"oi":"sou foda"},
        // success: success,
        dataType: 'application/json',
      }).done(function(data){
          console.log(data);
          
      });
})
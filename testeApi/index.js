$(document).ready(function(){
    $.ajax({
        type: "GET",
        url: "http://localhost:8000/listaClientes/?format=api",
        // data: data,
        // success: success,
        dataType: 'application/json'
      }).done(function(data){
          console.log(data);
          
      });
})
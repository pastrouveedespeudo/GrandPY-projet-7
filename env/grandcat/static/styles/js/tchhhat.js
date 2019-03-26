$(document).ready(function(){
  $("form").on("submit", function(e){
      $.ajax({
          data:{
              data:$("#idRecupInfo").val(),
          },
          type:"POST",
          url:"/answer",
      })
      .done(function(data){
          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#image");
          }
          else{
              $("#image").html(data.data);
              $("#monCadreAlert");
          };
      });
      e.preventDefault();
  });
});


$(document).ready(function(){
  $("form").on("submit", function(e){
      $.ajax({
          data:{
              data:$("#idRecupInfo").val(),
          },
          type:"POST",
          url:"/img",
      })
      .done(function(data){
          if (data.error){
              $("#monCadreAlert").text(data.error);
              $("#discussion");
          }
          else{
              $("#discussion").html(data.data);
              $("#monCadreAlert");  
          };
      });
      effacer();
      e.preventDefault();
  });
});


function effacer(){
  document.getElementById("idRecupInfo").value = "";
}

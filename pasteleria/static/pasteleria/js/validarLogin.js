$(document).ready(function() {
    $("#datosSi").hide();
    $("#datosNo").hide();
   $("#formulario1").submit(function(e){
       e.preventDefault();
       run = $.trim($("#rut").val());
       pass = $.trim($("#contraseña").val());
       if(run.length>0 && pass.length>0){
           $("#datosSi").fadeTo(2000, 500).slideUp(500, function(){
               $("#datosSi").slideUp(500);
               setTimeout(function(){window.location.href = "http://localhost:8000/pasteleria/"}, 500 );
           });
       }else{
           $("#datosNo").fadeTo(2000, 500).slideUp(500, function(){
               $("#datosNo").slideUp(500);
           });
       }
   }
   ) 
});
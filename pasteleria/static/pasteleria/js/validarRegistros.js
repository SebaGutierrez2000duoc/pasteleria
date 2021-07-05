$(document).ready(function() {
    $("#siRegistrado").hide();
    $("#noRegistrado").hide();
    $("#formulario2").submit(function (e) {
        e.preventDefault();
        nombre = $.trim($("#nom").val());
        apellido_p = $.trim($("#apellidop").val());
        apellido_m = $.trim($("#apellidom").val());
        run = $.trim($("#rut").val());
        correoelectronico = $.trim($("#corr").val());
        clavea = $.trim($("#clav").val());
        if (nombre.length>0 && apellido_p.length>0 && apellido_p.length>0 && run.length>0 && correoelectronico.length>0 && clavea.length>0) {
            $("#siRegistrado").fadeTo(2000, 500).slideUp(500, function() {
                $("#siRegistrado").slideUp(500);
                $(setTimeout(function(){window.location.href = "login.html";}, 500));
            });
        } else {
            $("#noRegistrado").fadeTo(2000, 500).slideUp(500, function() {
                $("#noRegistrado").slideUp(500);
            });
        }
    });
  });
$(document).ready(function () {
    $("#siFinalizado").hide();
    $("#noFinalizado").hide();
    $("#finalizarPedido").submit(function (e) {
      e.preventDefault();
      direccion = $.trim($("#direc").val());
      telefono = $.trim($("#tel").val());
      if (direccion.length > 0 && telefono.length > 0) {
        $("#siFinalizado").fadeTo(2000, 500).slideUp(500, function () {
          $("#siFinalizado").slideUp(500);
          setTimeout(function () { window.location.href = "home.html"; }, 500);
        });
      } else {
        $("#noFinalizado").fadeTo(2000, 500).slideUp(500, function () {
          $("#noFinalizado").slideUp(500);
        });
      }
    }
    )
  });
function validar(){
  console.log("HOla Llegue");
  $('[name="nombre"]').blur(function (e) {
    let num = $('[name="nombre"]').val();
    if (num.length < 4) {
      $('[name="nombre"]').val("");
    }
  });
};

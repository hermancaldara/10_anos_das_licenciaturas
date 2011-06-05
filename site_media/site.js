function manage_poster_fields(){
  if ($('#id_poster_presentation option:selected').val() == 'sim') {
    $('#poster_title').css('display', 'block');
    $('#poster_autors').css('display', 'block');
    $('#poster_leader').css('display', 'block');
    $('#poster_institution').css('display', 'block');
    $('#poster_abstract').css('display', 'block');
  }
  else {
    $('#poster_title').css('display', 'none');
    $('#poster_autors').css('display', 'none');
    $('#poster_leader').css('display', 'none');
    $('#poster_institution').css('display', 'none');
    $('#poster_abstract').css('display', 'none');
  }
}

function manage_people_type(){
  if ($('#id_people_type option:selected').val() == 'outro') {
    $('#other_choice').css('display', 'block');
  }
  else {
    $('#other_choice').css('display', 'none');
  }
}

$(function() {
  $("#id_poster_presentation").change(manage_poster_fields);
  $("#id_people_type").change(manage_people_type);
});

jQuery(function($){
   $("#id_phone").mask("(99) 9999-9999");
   $("#id_mobile").mask("(99) 9999-9999");
   $("#id_cpf").mask("999.999.999-99");
});

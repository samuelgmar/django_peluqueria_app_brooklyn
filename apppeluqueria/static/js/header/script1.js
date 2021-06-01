function anadir_trabajador(){
    if(document.querySelector('button.add')){
        const addt = $('.addt');
        addt.css('display','block');
        setTimeout(function () {
            addt.css('opacity','1');
        }, 250);
    }
}
function return_anadir_trabajador(){
    if(document.querySelector('button.add')){
        const addt = $('.addt');
        addt.css('opacity','0');
        setTimeout(function () {
            addt.css('display','none');
        }, 250);
    }
}

function anadir_cliente(){
    document.querySelector('.workersList').style.display = 'none';
    document.querySelector('.b').style.height = '100vh';
    if(document.querySelector('button.add')){
        const addt = document.querySelector('.addt');
        addt.classList.toggle('active');
    }
}

function return_anadir_cliente(){
    document.querySelector('.workersList').style.display = 'block';
    document.querySelector('.b').style.height = '100vh';
    if(document.querySelector('button.add')){
        const addt = document.querySelector('.addt');
        addt.classList.toggle('active');
    }
}

function borrarCliente(){
    var bool = confirm("Seguro de eliminar el dato?");
    console.log(bool);
    if(bool){
        alert("se elimino correctamente");
        $( "#userDeleteForm" ).submit();
    }else{
      alert("cancelo la solicitud");
    }
}

function addcategory(){
    document.querySelector('.categoriesServicesList').style.display = 'none';
    document.querySelector('.addcategory').style.display = 'flex';
    document.querySelector('.addservice').style.display = 'none';
}

function returncategory(){
    document.querySelector('.categoriesServicesList').style.display = 'block';
    document.querySelector('.addcategory').style.display = 'none';
    document.querySelector('.addservice').style.display = 'none';
}

function addservice(){
    document.querySelector('.categoriesServicesList').style.display = 'none';
    document.querySelector('.addcategory').style.display = 'none';
    document.querySelector('.addservice').style.display = 'flex';
}

function returnservice(){
    document.querySelector('.categoriesServicesList').style.display = 'block';
    document.querySelector('.addcategory').style.display = 'none';
    document.querySelector('.addservice').style.display = 'none';
}

function borrarServicio(id){
    var bool = confirm("Seguro de eliminar el dato?");
    console.log(bool);
    if(bool){
        alert("se elimino correctamente");
        $( id ).submit();
    }else{
      alert("cancelo la solicitud");
    }
}

function borrarCategoria(id){
    var bool = confirm("Seguro de eliminar el dato?");
    console.log(bool);
    if(bool){
        alert("se elimino correctamente");
        $( id ).submit();
    }else{
      alert("cancelo la solicitud");
    }
}


function mostrarhoras(e){
   $("#valor").text(e.target.value+' '+$('input[name=match]:checked').val());
}

function quitarhora(e=''){
    var allhoras = document.getElementsByName('horas');
    let horas = [];
    var elements = document.getElementsByName('matchcon');
    elements.forEach(function(element) {
        let partes = element.getAttribute('value').split(' ');
        var tra = $('input[name=trabajador]:checked').val();
        var eti = e.target.value;
        if(partes[0] == tra && partes[1]== eti ){
            horas.push(partes[2]);
        }  
    });
    horas.forEach(function(element) {
        allhoras.forEach(function(hora) {
            if(hora.getAttribute('value')== element){
                var ele = element;
                ele = '\('+ele.replace(':', '\:')+'\)';
                var p = document.getElementsByClassName(ele);
                p[0].style.display = 'none';
            }
        }); 
    });
    if(horas.length == 0){
        allhoras.forEach(function(hora) {
            var ele = hora.getAttribute('value');
            ele = '\('+ele.replace(':', '\:')+'\)';
            var p = document.getElementsByClassName(ele);
            p[0].style.display = 'block';
        }); 
    }
    var mostrarhoras = document.getElementById('horas-container');
    let elementStyle = window.getComputedStyle(mostrarhoras);
    let elementdisplay = elementStyle.getPropertyValue('display');
    if(elementdisplay == 'none'){
        document.getElementById('horas-container').style.display = 'block';
    }
}

function mostrarnext(){
    var todo = document.getElementsByClassName('mostrarnext');
    var selec = $('input[name=trabajador]:checked').val();
    var cliente = $('input[name="cliente"]').val();
    if(cliente != "" && selec){
        for(var i = 0; i < todo.length;i++){
            todo[i].style.display = 'inline';
        }
    }
}

function quitarnext(){
    var todo = document.getElementsByClassName('mostrarnext');
    for(var i = 0; i < todo.length;i++){
        todo[i].style.display = 'none';
    }
}

function mostrarsubmit(){
    $('input[name=submit]').css('display', 'inline-block');
}

function filtrarReservas(){
    var listservicios = $('input[name=listservicios]').val();
    var listtrabajadores =$('input[name=listtrabajadores]').val();
    var listcliente =$('input[name=listcliente]').val();
    listcliente = listcliente.split(' - ');
    listcliente = listcliente[1];
    var listfecha =$('input[name=listfecha]').val();
    var listhoras =$('input[name=listhoras]').val();
    var reservas =document.getElementsByName('reser');
    var reser=[];
    for(reserva = 0; reserva < reservas.length; reserva++){
        reservas[reserva].style.display = 'block';
    }
    for(reserva = 0; reserva < reservas.length; reserva++){
        if(reservas[reserva].style.display == 'block'){
            reser.push(reservas[reserva]);
        }
    }
    if(reser.length != 0){
        reservas = reser;
    }
    var arr = [];
    if(listservicios != 'All' && listservicios != '' && listservicios != undefined && listservicios != 'Todas'){
        for(reserva = 0; reserva < reservas.length; reserva++){
            if(reservas[reserva].textContent.includes(listservicios)){
                arr.push(reservas[reserva]);
                reservas[reserva].style.display = 'block';
            }else{
                reservas[reserva].style.display = 'none';
            }
        }
    }
    if(arr.length!=0){
        reservas = arr;
    }
    arr = [];
    var reser=[];
    for(reserva = 0; reserva < reservas.length; reserva++){
        if(reservas[reserva].style.display == 'block'){
            reser.push(reservas[reserva]);
        }
    }
    reservas = reser;
    if(listtrabajadores != 'All' && listtrabajadores != '' && listtrabajadores != undefined && listtrabajadores != 'Todas'){
        for(reserva = 0; reserva < reservas.length; reserva++){
            if(reservas[reserva].textContent.includes(listtrabajadores)){
                arr.push(reservas[reserva]);
                reservas[reserva].style.display = 'block';
            }else{
                reservas[reserva].style.display = 'none';
            }
        }
    }

    if(arr.length!=0){
        reservas = arr;
    }
    arr = [];
    var reser=[];
    for(reserva = 0; reserva < reservas.length; reserva++){
        if(reservas[reserva].style.display == 'block'){
            reser.push(reservas[reserva]);
        }
    }
    reservas = reser;
    if(listcliente != 'All' && listcliente != '' && listcliente != undefined && listcliente != 'Todas'){
        for(reserva = 0; reserva < reservas.length; reserva++){
            if(reservas[reserva].textContent.includes(listcliente)){
                arr.push(reservas[reserva]);
                reservas[reserva].style.display = 'block';
            }else{
                reservas[reserva].style.display = 'none';
            }
        }
    }

    if(arr.length!=0){
        reservas = arr;
    }
    arr = [];
    var reser=[];
    for(reserva = 0; reserva < reservas.length; reserva++){
        if(reservas[reserva].style.display == 'block'){
            reser.push(reservas[reserva]);
        }
    }
    reservas = reser;
    if(listfecha != 'All' && listfecha != '' && listfecha != undefined && listfecha != 'Todas'){
        for(reserva = 0; reserva < reservas.length; reserva++){
            if(reservas[reserva].textContent.includes(listfecha)){
                arr.push(reservas[reserva]);
                reservas[reserva].style.display = 'block';
            }else{
                reservas[reserva].style.display = 'none';
            }
        }
    }

    if(arr.length!=0){
        reservas = arr;
    }
    arr = [];
    var reser=[];
    for(reserva = 0; reserva < reservas.length; reserva++){
        if(reservas[reserva].style.display == 'block'){
            reser.push(reservas[reserva]);
        }
    }
    reservas = reser;
    if(listhoras != 'All' && listhoras != '' && listhoras != undefined && listhoras != 'Todas'){
        for(reserva = 0; reserva < reservas.length; reserva++){
            if(reservas[reserva].textContent.includes(listhoras)){
                arr.push(reservas[reserva]);
                reservas[reserva].style.display = 'block';
            }else{
                reservas[reserva].style.display = 'none';
            }
        }
    }
    reservas = document.getElementsByName('reser');
    if((listhoras == 'All' || listhoras == '' || listhoras == 'Todas' || listhoras == undefined ) && ( listfecha == 'All' || listfecha == '' || listfecha == 'Todas' || listfecha == undefined ) && ( listcliente == 'All' || listcliente == '' || listcliente == 'Todas' || listcliente == undefined ) && ( listtrabajadores == 'All' || listtrabajadores == '' || listtrabajadores == 'Todas' || listtrabajadores == undefined ) && ( listservicios == 'All' || listservicios == '' || listservicios == 'Todas'  || listservicios == undefined)){
        for(reserva = 0; reserva < reservas.length; reserva++){
            reservas[reserva].style.display = 'block';
        }
    }
}
$(document).ready(function () {
    var URLactual = window.location.toString();
    if(URLactual.includes('#Home')){
        $('.home').click();
        $('.menu_toggler').click();
    }else if(URLactual.includes('#Services')){
        $('.services').click();
        $('.menu_toggler').click();
    }else if(URLactual.includes('#Galery')){
        $('.galery').click();
        $('.menu_toggler').click();
    }else if(URLactual.includes('#Contact')){
        $('.contact').click();
        $('.menu_toggler').click();
    }else if(URLactual.includes('#Redes')){
        $('.redes').click();
        $('.menu_toggler').click();
    }else if(URLactual.includes('#Politica')){
        $('.politica').click();
        $('.menu_toggler').click();
    }
    setTimeout(function () {
        $('.loading').hide().ajaxStart(function() { 
            $(this).show(); 
           }).ajaxStop(function() { 
            $(this).hide(); 
           });
      }, 2000);
});
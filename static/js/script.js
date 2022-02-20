// validation formulaire de connexion  

function validateFormConnex() {
  var username = document.forms["formConnexion"]["username"];       
  var password = document.forms["formConnexion"]["password"];

  if (username.value == ""){ 
      document.getElementById('error_username').innerHTML="*veuillez saisir votre d'utilisateur";  
      username.focus();
      // document.querySelector('.usernameC').classList.add('err');
      username.classList.add('err');
      return false; 
  }else{
      username.classList.remove('err');
      document.getElementById('error_username').innerHTML="";  
  }

  if (password.value == ""){ 
    document.getElementById('error_password').innerHTML="*veuillez saisir un votre mot de passe";  
    password.focus();
    password.classList.add('err');
    return false; 
  }else{
    password.classList.remove('err');
    document.getElementById('error_password').innerHTML="";  
  }
}





// choix du formulaire en fonction du type d'utilisateur

// function choisirFoum() {
//   var type_user = document.forms["formRegister"]["type_user"];

//   type = document.querySelector('#type');
//   type.innerHTML = type_user.value;
//   type.style.display="";
  
//   formRep = document.querySelector('.formRep')
//   formCli = document.querySelector('.formCli')
//   formPreview = document.querySelector('.formPreview')
//   etape2 = document.getElementById('etape2');
//   etape1 = document.getElementById('etape1');
  
//   if (type_user.value == "élève" || type_user.value == "parent") {
//     formRep.style.display="none";
//     formPreview.style.display="none";
//     formCli.style.display=""; 
//   }else{
//     formRep.style.display="";
//     formCli.style.display="none"; 
//     formPreview.style.display="none";
    
    
//   }

// }


// effect collpase (Test)
const label = document.getElementsByClassName('label');
const accordion = document.getElementsByClassName('contentBx');
for (let i = 0; i < label.length; i++) {
  label[i].addEventListener('click', function(){
    accordion[i].classList.toggle('active');
    accordion[i+1].classList.toggle('active');
  });
}


// fonctions de vérification du formulaire



function valChapmsText(champs, errClass) {
  if (champs.value == "") {
    errClass.innerHTML="*veuillez remplir ce champs";
    champs.focus();
    champs.classList.add('err');
    return false;
  } else {
    errClass.innerHTML="";
    champs.classList.remove('err');
    return true;
  }
}
function valChapmsAge(champs, errClass) {
  if (champs.value == "") {
    errClass.innerHTML="*veuillez entrer un nombre";
    champs.focus();
    champs.classList.add('err');
    return false;
  } else {
    errClass.innerHTML="";
    champs.classList.remove('err');
    return true;
  }
}
function valChapmsEmail(champs, errClass) {
  if (champs.value == "") {
    errClass.innerHTML="*veuillez remplir une addrese correcte";
    champs.focus();
    champs.classList.add('err');
    return false;
  } else {
    errClass.innerHTML="";
    champs.classList.remove('err');
    return true;
  }
}
function valChapmsTel(champs, errClass) {
  if (champs.value == "") {
    errClass.style.display="";
    errClass.innerHTML="*veuillez entrer un numéro correct";
    champs.focus();
    champs.classList.add('err');
    return false;
  } else {
    errClass.innerHTML="";
    champs.classList.remove('err');
    return true;
  }
}



//  enregistrement REPETITEUR


// etape 2

var last_nameRep = document.getElementById('id_last_name');
var error_last_nameRep = document.getElementById('error_last_nameRep');

var first_nameRep = document.getElementById('id_first_name');
var error_first_nameRep = document.getElementById('error_first_nameRep');

var ageRep = document.getElementById('id_age');
var error_ageRep = document.getElementById('error_ageRep');

var telephone1Rep = document.getElementById('id_telephone1');
var error_telephone1Rep = document.getElementById('error_telephone1Rep');

function valER2() {
  if (valChapmsText(last_nameRep, error_last_nameRep) 
      && valChapmsText(first_nameRep, error_first_nameRep)
      && valChapmsAge(ageRep, error_ageRep)
      && valChapmsTel(telephone1Rep, error_telephone1Rep)) 
  {
    return true;
  } else {
    return false
  }
}

//  etape 3

var niveauEtudeRep = document.getElementById('id_niveauEtude');
var error_niveauEtudeRep = document.getElementById('error_niveauEtudeRep');

var telephone2Rep = document.getElementById('id_telephone2');
var error_telephone2Rep = document.getElementById('error_telephone2Rep');

var emailRep = document.getElementById('id_email');
var error_emailRep = document.getElementById('error_emailRep');

var villeRep = document.getElementById('id_ville');
var error_villeRep = document.getElementById('error_villeRep');

var quartierRep = document.getElementById('id_quartier');
var error_quartierRep = document.getElementById('error_quartierRep');

function valER3() {
  if (valChapmsText(niveauEtudeRep, error_niveauEtudeRep) 
      && valChapmsTel(telephone2Rep, error_telephone2Rep)
      && valChapmsEmail(emailRep, error_emailRep)
      && valChapmsText(villeRep, error_villeRep)
      && valChapmsText(quartierRep, error_quartierRep)) 
  {
    return true;
  } else {
    return false
  }
}


// suivant
const suivantRep = document.getElementsByClassName('suivantRep');
const etapeRep = document.getElementsByClassName('etapeRep');
for (let i = 0; i < suivantRep.length; i++) {
  suivantRep[i].addEventListener('click', function(){
    
    
    if (i == 0) {
      if (valER2()){
        etapeRep[i+1].classList.toggle('active');
        etapeRep[i+2].classList.toggle('active');
      }
    }
    if (i == 1) {
      if (valER3()){
        etapeRep[i+1].classList.toggle('active');
        etapeRep[i+2].classList.toggle('active');
      }
    }
  });
}




// précédent
const precedentRep = document.getElementsByClassName('precedentRep');
for (let i = 0; i < precedentRep.length; i++) {
  precedentRep[i].addEventListener('click', function(){
    etapeRep[i+2].classList.toggle('active');
    etapeRep[i+1].classList.toggle('active');
  });
}





//  enregistrement ÉLÈVE/PARENT


// ETAPE 2 CLI

var last_nameCli = document.getElementById('id_last_name');
var error_last_nameCli = document.getElementById('error_last_nameCli');

var first_nameCli = document.getElementById('id_first_name');
var error_first_nameCli = document.getElementById('error_first_nameCli');

var telephone1Cli = document.getElementById('id_telephone1');
var error_telephone1Cli = document.getElementById('error_telephone1Cli');

var emailCli = document.getElementById('id_email');
var error_emailCli = document.getElementById('error_emailCli');

function valEC2() {
  if (valChapmsText(last_nameCli, error_last_nameCli) 
      && valChapmsText(first_nameCli, error_first_nameCli)
      && valChapmsTel(telephone1Cli, error_telephone1Cli)
      && valChapmsEmail(emailCli, error_emailCli)) 
  {
    return true;
  } else {
    return false
  }
}

// ETAPE 3 CLI

var villeCli = document.getElementById('id_ville');
var error_villeCli = document.getElementById('error_villeCli');

var quartierCli = document.getElementById('id_quartier');
var error_quartierCli = document.getElementById('error_quartierCli');

function valEC3() {
  if (valChapmsText(villeCli, error_villeCli)
      && valChapmsText(quartierCli, error_quartierCli)) 
  {
    return true;
  } else {
    return false
  }
}



// suivant cli
const suivantCli = document.getElementsByClassName('suivantCli');
const etapeCli = document.getElementsByClassName('etapeCli');
for (let i = 0; i < suivantCli.length; i++) {
  suivantCli[i].addEventListener('click', function(){
    

    if (i == 0) {
      if (valEC2()){
        etapeCli[i+1].classList.toggle('active');
        etapeCli[i+2].classList.toggle('active');
      }
    }
    if (i == 1) {
      if (valEC3()){
        etapeCli[i+1].classList.toggle('active');
        etapeCli[i+2].classList.toggle('active');
      }
    }
  });
}


// précédent cli
const precedentCli = document.getElementsByClassName('precedentCli');
for (let i = 0; i < precedentCli.length; i++) {
  precedentCli[i].addEventListener('click', function(){
    etapeCli[i+2].classList.toggle('active');
    etapeCli[i+1].classList.toggle('active');
  });
}
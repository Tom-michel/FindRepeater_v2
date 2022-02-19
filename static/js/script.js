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

function choisirFoum() {
  var type_user = document.forms["formRegister"]["type_user"];

  // document.querySelector('.e1').style.display="none"
  type = document.querySelector('#type');
  type.innerHTML = type_user.value;
  type.style.display="";
  
  formRep = document.querySelector('.formRep')
  formCli = document.querySelector('.formCli')
  formPreview = document.querySelector('.formPreview')
  etape2 = document.getElementById('etape2');
  etape1 = document.getElementById('etape1');
  
  // alert(type_user.value);
  if (type_user.value == "élève" || type_user.value == "parent") {
    formRep.style.display="none";
    formPreview.style.display="none";
    formCli.style.display=""; 
  }else{
    formRep.style.display="";
    formCli.style.display="none"; 
    formPreview.style.display="none";
    
    
  }

}


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


//  enregistrement REPETITEUR


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


// etape 2

var last_nameRep = document.getElementById('last_nameRep');
var error_last_nameRep = document.getElementById('error_last_nameRep');

var first_nameRep = document.getElementById('first_nameRep');
var error_first_nameRep = document.getElementById('error_first_nameRep');

var ageRep = document.getElementById('ageRep');
var error_ageRep = document.getElementById('error_ageRep');

var telephone1Rep = document.getElementById('telephone1Rep');
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

var niveauEtudeRep = document.getElementById('niveauEtudeRep');
var error_niveauEtudeRep = document.getElementById('error_niveauEtudeRep');

var telephone2Rep = document.getElementById('telephone2Rep');
var error_telephone2Rep = document.getElementById('error_telephone2Rep');

var emailRep = document.getElementById('emailRep');
var error_emailRep = document.getElementById('error_emailRep');

var villeRep = document.getElementById('villeRep');
var error_villeRep = document.getElementById('error_villeRep');

var quartierRep = document.getElementById('quartierRep');
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


// etape 4

var usernameRep = document.getElementById('usernameRep');
var error_usernameRep = document.getElementById('error_usernameRep');

var password1Rep = document.getElementById('password1Rep');
var error_password1Rep = document.getElementById('error_password1Rep');

var password2Rep = document.getElementById('password2Rep');
var error_password2Rep = document.getElementById('error_password2Rep');

function valER4() {
  if (valChapmsText(usernameRep, error_usernameRep) 
      && valChapmsText(password1Rep, error_password1Rep)) 
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
      etapeRep[i].classList.toggle('active');
      etapeRep[i+1].classList.toggle('active');
    }
    if (i == 1) {
      if (valER2()){
        etapeRep[i].classList.toggle('active');
        etapeRep[i+1].classList.toggle('active');
      }
    }
    if (i == 2) {
      if (valER3()){
        etapeRep[i].classList.toggle('active');
        etapeRep[i+1].classList.toggle('active');
      }
    }
    if (i == 3) {
      if (valER4()){
        etapeRep[i].classList.toggle('active');
        etapeRep[i+1].classList.toggle('active');
      }
    }
    // etapeRep[i].classList.toggle('active');
    // etapeRep[i+1].classList.toggle('active');
  });
}


// précédent
const precedentRep = document.getElementsByClassName('precedentRep');
for (let i = 0; i < precedentRep.length; i++) {
  precedentRep[i].addEventListener('click', function(){
    etapeRep[i].classList.toggle('active');
    etapeRep[i-1].classList.toggle('active');
  });
}





// validation formulaire d'enregistrement

// ETAPE 1 PROF
// function valProfE2() {
//   var etape2 = document.getElementById('etape2');
//   // var etape3 = document.querySelector('#etape3');

//   var last_nameRep = document.getElementById('last_nameRep');
  
  // var last_name = document.forms["formRegister"]["last_name"];       
  // var first_name = document.forms["formRegister"]["first_name"];       
  // var age = document.forms["formRegister"]["age"];       
  // var telephone1 = document.forms["formRegister"]["telephone1"];       
  // var telephone2 = document.forms["formRegister"]["telephone2"];       
  // var email = document.forms["formRegister"]["email"];

//   if (last_nameRep.value == ""){ 
//     document.getElementById('error_last_name').innerHTML="*veuillez saisir votre Nom";  
//     last_nameRep.focus();
//     last_nameRep.classList.add('err');
//     etape2.classList.remove('etape2-3');
//     // etape3.classList.remove('etape2-3');
//     return false; 
//   }else{
//     etape2.classList.add('etape2-3');
//     // alert('le Nom a été rempli');
//   }  
// }

// ETAPE 3 PROF
function valProfE3() {
  
}

// ETAPE 1 CLI
function valCliE2() {

}

// ETAPE 3 CLI
function valCliE3() {
  
}


// ETAPE 4 PROF ET CLI
function valProfCliE4() {
  
}


function validateFormEnreg() {
  var type_user = document.forms["formRegister"]["type_user"];
  
  if (type_user.value == "élève" || type_user.value == "parent") {

  }else{    
    return valER4();
  }
}
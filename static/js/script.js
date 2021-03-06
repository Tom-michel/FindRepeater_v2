// baisser le menu lorsqu'on clique ailleur sur l'ecran

// var navbarNavDropdown = document.getElementById('navbarNavDropdown');
// window.addEventListener('click', function(e){
//   if (!menuO.contains(e.target)) {
//       if (navbarNavDropdown.classList.contains("show") == true) {
//         navbarNavDropdown.classList.remove("show");
//         menuC.classList.toggle('cliq');
//         menuO.classList.toggle('cliq');
//       }
//   }
// });


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
function valChapmsSelect(champs, errClass) {
  if (champs.value == "") {
    errClass.innerHTML="*veuillez choisir un élément de la liste";
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
  } else if (champs.value <= "0" || champs.value >= "50") {
    errClass.innerHTML="*entrez un âge correct (<50)";
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
  var valeursAcceptees = /^[\w\-\.\+]+\@[a-zA-Z0-9\.\-]+\.[a-zA-z0-9]{2,4}$/;
  if (champs.value == "") {
    errClass.innerHTML="*veuillez entrer une addrese mail";
    champs.focus();
    champs.classList.add('err');
    return false;
  } else if ( ! champs.value.match(valeursAcceptees)) {
    errClass.innerHTML="*veuillez entrer une addrese mail valide";
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
  } else if (champs.value.charAt(0)!="+" || champs.value.charAt(1)!="2" || champs.value.charAt(2)!="3" || champs.value.charAt(3)!="7") {
    errClass.style.display="";
    errClass.innerHTML="*le numéro doit débuter par '+237'";
    champs.focus();
    champs.classList.add('err');
    return false;
  } else if (champs.value.length != 13) {
    errClass.style.display="";
    errClass.innerHTML="*veuillez entrer un numéro correct (12 chiffres)";
    champs.focus();
    champs.classList.add('err');
    return false;
  }  else {
    for (let i = 1; i < champs.value.length; i++) {
      if (champs.value.charAt(i) < "0" || champs.value.charAt(i) > "9") {
        errClass.style.display="";
        errClass.innerHTML="*veuillez entrer un numéro correct";
        champs.focus();
        champs.classList.add('err');
        return false;
      }
    }
  }
  
  errClass.innerHTML="";
  champs.classList.remove('err');
  return true;
  
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
var professionRep = document.getElementById('id_profession');
var error_professionRep = document.getElementById('error_professionRep');

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
  if (valChapmsText(professionRep, error_professionRep) 
      &&valChapmsText(niveauEtudeRep, error_niveauEtudeRep) 
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

var emailCli = document.getElementById('id_email');
var error_emailCli = document.getElementById('error_emailCli');

var classeCli = document.getElementById('id_classe');
var error_classeCli = document.getElementById('error_classeCli');

var villeCli = document.getElementById('id_ville');
var error_villeCli = document.getElementById('error_villeCli');

var quartierCli = document.getElementById('id_quartier');
var error_quartierCli = document.getElementById('error_quartierCli');

var telephone1Cli = document.getElementById('id_telephone1');
var error_telephone1Cli = document.getElementById('error_telephone1Cli');

function valEC2() {
  if (valChapmsEmail(emailCli, error_emailCli)
      &&valChapmsSelect(classeCli, error_classeCli)
      &&valChapmsText(villeCli, error_villeCli)
      && valChapmsText(quartierCli, error_quartierCli)
      && valChapmsTel(telephone1Cli, error_telephone1Cli)) 
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
    // if (i == 1) {
    //   if (valEC3()){
    //     etapeCli[i+1].classList.toggle('active');
    //     etapeCli[i+2].classList.toggle('active');
    //   }
    // }
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


// valider l'ajout d'une matière

function valAjoutMatiere(){
  var intitule = document.getElementById('id_intitule');
  var error_intituleCours = document.getElementById('error_intituleCours');
  if (valChapmsText(intitule, error_intituleCours)) {
    return true;
  }else {
    return false;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
  }
}


// valider l'ajout d'une classe

function valAjoutClasse(){
  var niveau = document.getElementById('id_niveau');
  var error_niveauClasse = document.getElementById('error_niveauClasse');
  if (valChapmsText(niveau, error_niveauClasse)) {
    return true;
  }else {
    return false;                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                          
  }
}
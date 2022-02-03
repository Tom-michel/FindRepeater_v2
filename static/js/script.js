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

// DÉBUTonsubmit="return validateForm()"
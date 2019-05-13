function getCookie(sName){
  var aCookie=document.cookie.split("; ");
  for(var i=0;i<aCookie.length;i++){
    var aCrumb=aCookie[i].split("=");if(sName==aCrumb[0])
    return(aCrumb[1]);
  }
  return null;
}

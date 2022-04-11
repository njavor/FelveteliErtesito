document.addEventListener("DOMContentLoaded", main);

function main(){
    
    
    let nev = document.querySelector('.nev');
    if (nev != null){
        let eredmenyek = document.querySelector('.eredmenyek');
        setTimeout(function () {
            nev.classList.add('nev-be');
        }, 250);
        setTimeout(function () {
            eredmenyek.classList.add('see');
        }, 1500)
    }
}
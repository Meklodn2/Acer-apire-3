let togglebtn = document.querySelector("#toggle");

function LoadTheme() {
    const currentTheme = localStorage.getItem('theme');
    if (currentTheme === 'dark') {
        document.body.classList.add('dark-mode');

    } else {
        document.body.classList.add('light-mode');
    }
}

function toggleTheme(){
    document.body.classList.toggle('dark-mode');
    document.body.classList.toggle('light-mode');

   if (document.body.classList.contains('dark-mode')){
    localStorage.setItem('theme','dark');

   } else {
    localStorage.setItem('theme','light');
   }
}

togglebtn.addEventListener('click', toggleTheme)

LoadTheme()
document.addEventListener("DOMContentLoaded", () => {
    const footerP = document.querySelector(".main-footer p");
    if(footerP) footerP.innerHTML = `&copy; ${new Date().getFullYear()} Patrícia Lourenço`;
});
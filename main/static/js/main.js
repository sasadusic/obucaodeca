
const menuBtn = document.querySelector(".fa-bars")
const side = document.querySelector('#side')

menuBtn.onclick = () => {
    menuBtn.classList.toggle('fa-times')
    side.classList.toggle('active')
}
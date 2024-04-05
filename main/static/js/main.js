// alert('test')
console.log('test')
const menuBtn = document.querySelector(".fa-bars")
const side = document.querySelector('#side')

menuBtn.onclick = () => {
    menuBtn.classList.toggle('fa-times')
    side.classList.toggle('active')
}

const arrowleft = document.querySelector('#arrow-left')
const arrowRight = document.querySelector('#arrow-right')
const detailImages = document.querySelectorAll('.img-detail')
const detailimageNum = detailImages.length

let curImage = 1

arrowleft.onclick = () => {
    alert('left')
    console.log('left')
    document.querySelector(`.img-detail-${curImage}`).style.display = 'none'
    curImage--
    curImage = curImage < 1 ? detailimageNum : curImage
    document.querySelector(`.img-detail-${curImage}`).style.display = 'block'
}

arrowFight.onclick = () => {
    alert('right')
    console.log('right')
    document.querySelector(`.img-detail-${curImage}`).style.display = 'none'
    curImage++
    curImage = curImage > detailimageNum ? 1 : curImage
    document.querySelector(`.img-detail-${curImage}`).style.display = 'block'
}
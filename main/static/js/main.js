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
    // alert('left')
    // console.log('left')
    document.querySelector(`.img-detail-${curImage}`).style.display = 'none'
    curImage--
    curImage = curImage < 1 ? detailimageNum : curImage
    document.querySelector(`.img-detail-${curImage}`).style.display = 'block'
}

arrowRight.onclick = () => {
    // alert('right')
    // console.log('right')
    document.querySelector(`.img-detail-${curImage}`).style.display = 'none'
    curImage++
    curImage = curImage > detailimageNum ? 1 : curImage
    document.querySelector(`.img-detail-${curImage}`).style.display = 'block'
}

// Modal
const imageModal = document.querySelector('[data-modal-image]')
const imageModalOpen = document.querySelectorAll('.image-modal-open')
const closeImageModal = document.querySelector('.modal-close')

imageModalOpen.forEach(open => {

    open.onclick = () => {
        console.log('open')
        if(window.innerWidth > 768){
            imageModal.showModal()
        }
    }
})

closeImageModal.onclick = () => {
    console.log('close')
    imageModal.close()
}

const modalLeft = document.querySelector('#previous')
const modalRight = document.querySelector('#next')
const modalImages = document.querySelectorAll('.modal-item')
const modalimageNum = modalImages.length

let curModalImage = 1

modalLeft.onclick = () => {
    // alert('left')
    // console.log('left')
    document.querySelector(`.modal-item-${curModalImage}`).style.display = 'none'
    curModalImage--
    curModalImage = curModalImage < 1 ? modalimageNum : curModalImage
    document.querySelector(`.modal-item-${curModalImage}`).style.display = 'block'
}

modalRight.onclick = () => {
    // alert('left')
    // console.log('left')
    document.querySelector(`.modal-item-${curModalImage}`).style.display = 'none'
    curModalImage++
    curModalImage = curModalImage > modalimageNum ? 1 : curModalImage
    document.querySelector(`.modal-item-${curModalImage}`).style.display = 'block'
}
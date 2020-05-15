var addGame = document.querySelector('.add-talk-js')
addGame.addEventListener('click', function () {
    document.querySelector('.popup').style.display = 'flex'
})

document.querySelector('.close').addEventListener('click', function () {
    document.querySelector('.popup').style.display = 'none'
    document.querySelector('wrapper').style.overflow = 'visible'
})
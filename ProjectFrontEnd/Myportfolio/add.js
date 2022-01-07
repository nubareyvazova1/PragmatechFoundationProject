function getScrollAmount(){
    if(window.scrollY > 150){
        document.querySelector('.navbar').style.background='black'
    }else{
        document.querySelector('.navbar').style.background='transparent'
        ocument.querySelector('.navbar').style.color='#fff'
    }
}
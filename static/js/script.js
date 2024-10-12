const buttons = document.querySelectorAll('button[data-id')

buttons.forEach(button => {
    
    button.addEventListener('click', ()=>{

        const item = document.getElementById(`item_${button.getAttribute('data-id')}`)
        if(item.style.display === 'none' || item.style.display === ''){
            item.style.display = 'flex'
        }else{
            item.style.display = 'none'
        }

    })

});
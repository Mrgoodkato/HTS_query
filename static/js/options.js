const optionBtns = document.querySelectorAll('[data-option]');
const optionContainers = document.querySelectorAll('[data-optionContainer');

function toggleOptions(selectedBtn){

    optionBtns.forEach(button => {
        if(button.getAttribute('data-option') == selectedBtn){
            optionContainers.forEach(container => {
                if(container.getAttribute('data-optionContainer') == selectedBtn){
                    container.style.display = 'block';
                }else{
                    container.style.display = 'none';
                }
            });
        }
    });

}

optionBtns.forEach(button => {
    button.addEventListener('click', ()=>{

        toggleOptions(button.getAttribute('data-option'));

    });
});
const optionBtns = document.querySelectorAll('[data-option]');
const optionContainers = document.querySelectorAll('[data-optionContainer');


function toggleDisplayBtn(container){

    if(container.style.display == 'flex') container.style.display = 'none';
    else container.style.display = 'flex';

}

function toggleOptions(selectedBtn){

    optionBtns.forEach(button => {
        if(button.getAttribute('data-option') == selectedBtn){
            optionContainers.forEach(container => {
                if(container.getAttribute('data-optionContainer') == selectedBtn){
                    toggleDisplayBtn(container);
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
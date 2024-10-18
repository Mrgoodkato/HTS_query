const txtArea = document.getElementById('hts_txt_area');
const warning = document.getElementById('warning_input');
const modalErrors = document.getElementById('warning_modal');
const errorList = document.getElementById('error_list');

const validCharacters = /^[0-9.\n]*$/g;
const linePattern = /(?:^[\d]{4}(?:\.[\d]{2}){1,3}$)|(?:^[\d]{4,10})/gm;
let isPasting =false;

function validateInput(value){

    return validCharacters.test(value)

}

txtArea.addEventListener('input', ()=>{

    if(!validateInput(txtArea.value)){
        let input = txtArea.value
        txtArea.value = input.replace(/[^0-9.\n]/g, '')
        warning.style.display = 'block';
    }
    else warning.style.display = 'none';

})

txtArea.addEventListener('paste', ()=>{

    isPasting = true;

    if(!validateInput(txtArea.value)){
        console.log('modal')
        modalErrors.style.display = 'flex';
    }
    
    isPasting = false;

})
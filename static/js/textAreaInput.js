const txtArea = document.getElementById('hts_txt_area');
const warning = document.getElementById('warning_input');
const modalErrors = document.getElementById('warning_modal');
const errorList = document.getElementById('error_list');

const validCharacters = /^[0-9.\n]*$/g;
const linePattern = /(?:^[\d]{4}(?:\.[\d]{2}){1,3}$)|(?:^[\d]{4,10})/gm;
let isPasting =false;

txtArea.addEventListener('input', ()=>{
    isValid = !!txtArea.value.match(validCharacters)
    if(!isValid && !isPasting){
        let input = txtArea.value
        txtArea.value = input.replace(/[^0-9.\n]/g, '')
        warning.style.display = 'block';
    }
    else warning.style.display = 'none';

})

txtArea.addEventListener('paste', (event)=>{
    
    isPasting = true;
    isValid = !!event.clipboardData.getData('text/plain').match(validCharacters);
    if(!isValid && isPasting){
        modalErrors.style.display = 'block';
        errorList.append(event.clipboardData.getData('text'))
    }

    isPasting = false;


})
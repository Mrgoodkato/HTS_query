const txtArea = document.getElementById('hts_txt_area');
const warning = document.getElementById('warning_input');
const errorArea = document.getElementById('error_container');
const errorList = document.getElementById('error_list');
const closeErrors = document.getElementById('close_errors');

const htsPattern = /(?:^[\d]{4}\.[\d]{2}\.[\d]{2}\.[\d]{2}$|\\r)|(?:^[\d]{4}\.[\d]{2}\.(?:[\d]{2}|[\d]{4})$|\\r)|(?:^[\d]{4}\.(?:[\d]{2}|[\d]{4}|[\d]{6})$)|(?:^[\d]{4}$|\\r)|(?:^[\d]{6}$|\\r)|(?:^[\d]{8}$|\\r)|(?:^[\d]{10}$|\\r)/;
const validCharacters = /^[0-9.\n]*$/g;
const linePattern = /(?:^[\d]{4}(?:\.[\d]{2}){1,3}$)|(?:^[\d]{4,10})/gm;
let isPasting =false;

txtArea.addEventListener('input', ()=>{
    let isValid = !!txtArea.value.match(validCharacters);
    if(!isValid && !isPasting){
        let input = txtArea.value;
        txtArea.value = input.replace(/[^0-9.\n]/g, '');
        warning.style.display = 'block';
    }
    else warning.style.display = 'none';

})

txtArea.addEventListener('keydown', (event)=>{
    const textArray = txtArea.value.split('\n')
    if(event.key == 'Enter'){
        
        
        textArray.forEach(text => {
            if(!text.match(htsPattern)){
                event.preventDefault();
                warning.style.display = 'block';
            }
            else{
                warning.style.display = 'none';
            }
        });

    }

})

txtArea.addEventListener('paste', (event)=>{
    
    isPasting = true;
    let isValid = !!event.clipboardData.getData('text/plain').match(validCharacters);
    if(!isValid && isPasting){
        errorArea.style.display = 'flex';
        errorList.textContent = event.clipboardData.getData('text');
    }

    isPasting = false;


})

closeErrors.addEventListener('click', ()=>{

    errorList.textContent = '';
    errorArea.style.display = 'none';

})

function grabTextAreaInput(value){

    const textArray = value.split('\n');
    const invalidText = [];
    textArray.forEach(text => {
        if(!text.match(htsPattern)) invalidText.push(text);
    });
    return invalidText;

}
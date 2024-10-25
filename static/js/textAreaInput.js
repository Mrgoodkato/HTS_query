const txtArea = document.getElementById('hts_txt_area');
const warning = document.getElementById('warning_input');
const errorArea = document.getElementById('error_container');
const errorList = document.getElementById('error_list');

const htsPattern = /(?:^[\d]{4}\.[\d]{2}\.[\d]{2}\.[\d]{2}$|\\r)|(?:^[\d]{4}\.[\d]{2}\.(?:[\d]{2}|[\d]{4})$|\\r)|(?:^[\d]{4}\.(?:[\d]{2}|[\d]{4}|[\d]{6})$)|(?:^[\d]{4}$|\\r)|(?:^[\d]{6}$|\\r)|(?:^[\d]{8}$|\\r)|(?:^[\d]{10}$|\\r)/;
const validCharacters = /^[0-9.\n]*$/g;
const linePattern = /(?:^[\d]{4}(?:\.[\d]{2}){1,3}$)|(?:^[\d]{4,10})/gm;
let isPasting =false;

function grabTextAreaInput(value){

    const textArray = value.split('\n');
    const parsedText = {
        valid: [],
        errors: []
    };
    textArray.forEach(text => {
        
        if(!text.match(htsPattern)) parsedText.errors.push(text);
        else parsedText.valid.push(text);
    });
    return parsedText;

}

function populateErrorArea(errors){
    
    errors.forEach(error => {
        const paragraph = document.createElement('p');
        paragraph.textContent = error;
        errorList.append(paragraph);
    })
}

function populateTextArea(text){

    text.forEach(txt =>{
        console.log(txt)
        txtArea.value += txt + '\n';
    })

}

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
    if(event.key == 'Enter'){
        const parsedText = grabTextAreaInput(txtArea.value);
        
        if(parsedText.errors){
            event.preventDefault();
            errorList.replaceChildren();
            populateErrorArea(parsedText.errors);
            populateTextArea(parsedText.valid);
        }
    }

})

txtArea.addEventListener('paste', (event)=>{
    
    isPasting = true;
    const isValid = !!event.clipboardData.getData('text/plain').match(validCharacters);
    const parsedText = grabTextAreaInput(event.clipboardData.getData('text'));
    if(!isValid && isPasting && parsedText.errors){
        console.log(parsedText)
        event.preventDefault();
        errorList.replaceChildren();
        populateErrorArea(parsedText.errors);
        populateTextArea(parsedText.valid);
    }

    isPasting = false;


})


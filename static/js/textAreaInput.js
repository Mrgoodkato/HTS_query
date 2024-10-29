const txtArea = document.getElementById('hts_txt_area');
const manualArea = document.querySelector('[data-htsinput]');
console.log(manualArea)
const warning = document.getElementById('warning_input');
const errorArea = document.getElementById('error_container');
const errorList = document.getElementById('error_list');
const punctuationErrorList = document.getElementById('punctuation_error_list');
const allowedKeys = [
    "Backspace",
    "Tab",
    "Escape",
    "ArrowUp",
    "ArrowDown",
    "ArrowLeft",
    "ArrowRight",
    "Delete",
    "Insert",
    "Home",
    "End",
    "PageUp",
    "PageDown",
    "Shift",
    "Control",
    "Alt",
    "CapsLock",
    "NumLock",
    "ScrollLock",
    "F1",
    "F2",
    "F3",
    "F4",
    "F5",
    "F6",
    "F7",
    "F8",
    "F9",
    "F10",
    "F11",
    "F12"
  ];;

const htsPattern = /(?:^[\d]{4}\.[\d]{2}\.[\d]{2}\.[\d]{2}$|\\r)|(?:^[\d]{4}\.[\d]{2}\.(?:[\d]{2}|[\d]{4})$|\\r)|(?:^[\d]{4}\.(?:[\d]{2}|[\d]{4}|[\d]{6})$)|(?:^[\d]{4}$|\\r)|(?:^[\d]{6}$|\\r)|(?:^[\d]{8}$|\\r)|(?:^[\d]{10}$|\\r)/;
const validCharacters = /^[0-9.\n]*$/g;
const linePattern = /(?:^[\d]{4}(?:\.[\d]{2}){1,3}$)|(?:^[\d]{4,10})/gm;
const punctuationPattern = /[ \r!\"#$%&\'()*+,-./:;<=>?@\[\]\^_`{|}~—]/g;
const patternManualInput = /[a-zA-Z \r!\"#$%&\'()*+,\-:;<=>?@\[\]\^_`{|}~—\\]/g;

//TEXT AREA LOGIC
function grabTextAreaInput(value){

    const punctuationErrors = value.match(punctuationPattern);
    const cleanedText = value.replace(punctuationPattern, '');
    const textArray = cleanedText.split('\n');
    const parsedText = {
        valid: [],
        errors: [],
        invalidPunctuation: null
    };
    if(punctuationErrors){
        const errSet = new Set(punctuationErrors);
        if(errSet.has('.')) errSet.delete('.');
        parsedText.invalidPunctuation =([...errSet].join(' '));
    }
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
        txtArea.value += txt + '\n';
    })

}

function populatePunctuationErrors(text){
    const paragraph = document.createElement('p');
    paragraph.textContent =text;
    punctuationErrorList.replaceChildren(paragraph);
}

txtArea.addEventListener('input', (event)=>{
    
    event.preventDefault();

})

txtArea.addEventListener('paste', (event)=>{
    const isValid = !!event.clipboardData.getData('text/plain').match(validCharacters);
    const parsedText = grabTextAreaInput(event.clipboardData.getData('text'));
    if(!isValid && parsedText.errors){
        event.preventDefault();
        if(parsedText.invalidPunctuation) {
            populatePunctuationErrors(parsedText.invalidPunctuation);           
        }
        errorList.replaceChildren();
        populateErrorArea(parsedText.errors);
        populateTextArea(parsedText.valid);
    }
})

//INPUT AREA LOGIC

manualArea.addEventListener('keydown', (event)=>{
    //Prevents backtick behavior causing problems
    if (event.key === "`") {
        event.preventDefault();
    }
    //Prevents special function keys, and copy paste as well as auto fill to trigger error
    if(allowedKeys.includes(event.key) || event.ctrlKey || event.key == undefined) {
        warning.style.display = 'none';
        return;
    }
    //Prevents letters and wrong characters input in the field
    if(event.key.match(patternManualInput)){
        event.preventDefault();
        warning.style.display = 'block';
    }else warning.style.display = 'none';
})


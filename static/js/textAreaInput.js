const txtArea = document.getElementById('hts_txt_area');
const errorList = document.getElementById('error_list');
const errorArea = document.getElementById('error_container');
const punctuationErrorList = document.getElementById('punctuation_error_list');

import {htsPattern, punctuationPattern} from './util/globalVars.js'


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


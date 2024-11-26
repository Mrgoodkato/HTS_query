const txtArea = document.getElementById('hts_txt_area');
const errorContainer = document.getElementById('error_container');
const errorList = document.getElementById('error_list');
const clearAllBtn = document.getElementById('clear_all');
const copyBtn = document.getElementById('copy');
const punctuationErrorList = document.getElementById('punctuation_error_list');

import {htsPattern, htsFPattern, validCharacters, punctuationPattern} from './util/globalVars.js'


//TEXT AREA LOGIC

//Grabs the text area input value from clipboard and converts it to a JS object with errors and invalid punctuation if present
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
        else {
            const formattedHTS = text.replace(htsFPattern, (raw, f1,f2,f3,f4,sf1,sf2,sf3,sh1,sh2,c1) =>{
                if(c1) return `${c1}`;
                if(sh1) return `${sh1}.${sh2}`;
                if(sf1) return `${sf1}.${sf2}.${sf3}`;
                if(f1) return `${f1}.${f2}.${f3}.${f4}`

            })
            parsedText.valid.push(formattedHTS);
        }
    });
    return parsedText;

}

//Appends the error codes to the errorList element in the page if they are found
function populateErrorArea(errors){
    
    errors.forEach(error => {
        const paragraph = document.createElement('p');
        paragraph.textContent = error;
        errorList.append(paragraph);
    })
}

//Populates the text area with the string array (text) provided separating with a new line each string
function populateTextArea(text){

    text.forEach(txt =>{
        txtArea.value += txt + '\n';
    })

}

//Populates the punctuationErrorList element with the set of found punctuation signs found that are not allowed
function populatePunctuationErrors(text){
    const paragraph = document.createElement('p');
    paragraph.textContent =text;
    punctuationErrorList.replaceChildren(paragraph);
}

//Defines the behavior of the txtArea element
txtArea.addEventListener('paste', (event)=>{
    txtArea.value = '';
    errorContainer.style.display = 'none';
    const isValid = !!event.clipboardData.getData('text/plain').match(validCharacters);
    const parsedText = grabTextAreaInput(event.clipboardData.getData('text'));
    if(!isValid || parsedText.errors){
        event.preventDefault();
        errorContainer.style.display = 'flex';
        if(parsedText.invalidPunctuation) {
            populatePunctuationErrors(parsedText.invalidPunctuation);           
        }
        errorList.replaceChildren();
        populateErrorArea(parsedText.errors);
        populateTextArea(parsedText.valid);
        return;
    }
})

//Defines the behavior of the clearAllBtn eleemnt
clearAllBtn.addEventListener('click', ()=>{txtArea.value = '';});

//Defines the behavior of the copyBtn element
copyBtn.addEventListener('click', ()=>{

    const text = txtArea.value;
    navigator.clipboard.writeText(text).then(()=>{
        alert('Copied values to Clipboard');
    }).catch(err =>{
        alert('Error copying the text to the clipboard, please try again');
    });


});
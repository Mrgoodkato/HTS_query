const txtArea = document.getElementById('hts_txt_area');
const errorList = document.getElementById('error_list');
const errorArea = document.getElementById('error_container');
const punctuationErrorList = document.getElementById('punctuation_error_list');

import {htsPattern, htsFPattern, validCharacters, punctuationPattern} from './util/globalVars.js'


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
        else {
            const formattedHTS = text.replace(htsFPattern, (raw, f1,f2,f3,f4,sf1,sf2,sf3,sh1,sh2,c1) =>{
                console.log(f1, f2, f3, f4, sf1, sf2, sf3, sh1, sh2, c1);   
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
        return;
    }




})


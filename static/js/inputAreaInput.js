const manualArea = document.querySelector('[data-htsinput]');
const manualContainer = document.getElementById('manual_input_container');
const warning = document.getElementById('warning_input');


import { allowedKeys, htsPattern, patternManualInput } from "./util/globalVars.js";

//INPUT AREA LOGIC

function createNewInputField(manualContainer, currentInputs, element){

    const newInput = document.createElement('input');
    const newInputDataVal = currentInputs.length;
    const focusInput = parseInt(element.getAttribute('data-htsinput'));

    newInput.setAttribute('data-htsinput', newInputDataVal.toString());    
    newInput.setAttribute('name', 'user_input');
    addEventListenerToInput(newInput);
    manualContainer.appendChild(newInput);
    const updatedCurrentInputs = document.querySelectorAll('[data-htsinput]')
    updatedCurrentInputs[focusInput+1].focus()

    return newInput;

}

function deleteCurrentInput(element){

    const currentInputs = document.querySelectorAll('[data-htsinput]');
    const inputNumber = parseInt(element.getAttribute('data-htsinput'));
    element.remove()
    currentInputs[inputNumber-1].focus()
    rearrangeInputs(currentInputs);

}

function rearrangeInputs(currentInputs){
    
    let index = 0
    currentInputs.forEach(input => {
        console.log(input.getAttribute('data-htsinput'))
        input.setAttribute('data-htsinput', index.toString());
        index++;
    });

}

function addEventListenerToInput(element){

    element.addEventListener('keydown', (event)=>{
        //Removes the previous input field
        if(event.key == 'Backspace' && element.value == ''){
            if(element.getAttribute('data-htsinput') == 0) return;
            event.preventDefault();
            deleteCurrentInput(element);
        }
        //Enter behavior
        if(event.key == 'Enter'){
            event.preventDefault();
            const currentInputs = document.querySelectorAll('[data-htsinput]');
            createNewInputField(manualContainer, currentInputs, element);
            return;
        }
        //Prevents backtick behavior causing problems
        if (event.key === "`") {
            event.preventDefault();
            return;
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
            return;
        }else {
            warning.style.display = 'none';
            return;
        }
    })

}

addEventListenerToInput(manualArea);
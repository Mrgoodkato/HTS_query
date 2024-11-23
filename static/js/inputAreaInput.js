const manualArea = document.querySelector('[data-htsinput]');
const manualContainer = document.getElementById('manual_input_container');
const warning = document.getElementById('warning_input');


import { allowedKeys, htsIPattern, validInputCharacters, patternManualInput } from "./util/globalVars.js";

//INPUT AREA LOGIC

function createNewInputField(manualContainer, currentInputs, element){

    const newInputDataVal = currentInputs.length;
    const focusInput = parseInt(element.getAttribute('data-htsinput'));

    if(newInputDataVal == focusInput+1){
        const newInputElement = armInputContainer(newInputDataVal.toString());
        manualContainer.appendChild(newInputElement);
        const updatedCurrentInputs = document.querySelectorAll('[data-htsinput]')
        updatedCurrentInputs[focusInput+1].focus();
        return;
    }
    const newInputElement = armInputContainer('new_input');
    const anchorNode = document.querySelector(`[data-container="${(focusInput+1).toString()}"]`);
    manualContainer.insertBefore(newInputElement, anchorNode);
    document.querySelector('[data-htsinput="new_input"]').focus();
    rearrangeInputs(document.querySelectorAll('[data-htsinput]'), document.querySelectorAll('[data-container]'));

    return;

}

function armInputContainer(newInputDataVal){

    const inputContainer = document.createElement('div');
    const newInput = document.createElement('input');
    const closeBtn = document.createElement('button');

    inputContainer.setAttribute('class', 'input_field');
    inputContainer.setAttribute('data-container', newInputDataVal);
    newInput.setAttribute('data-htsinput', newInputDataVal);
    newInput.setAttribute('name', 'user_input');
    addEventListenerToInput(newInput);

    closeBtn.setAttribute('type', 'button');
    closeBtn.textContent = 'Delete';
    closeBtn.addEventListener('click', ()=>{
        inputContainer.remove();
        rearrangeInputs(document.querySelectorAll('[data-htsinput]'), document.querySelectorAll('[data-container'));
    });

    inputContainer.append(newInput, closeBtn);
    
    return inputContainer;

}

function deleteCurrentInput(element){

    const currentInputs = document.querySelectorAll('[data-htsinput]');
    const currentContainers = document.querySelectorAll('[data-container]');
    const inputNumber = parseInt(element.getAttribute('data-htsinput'));
    currentContainers[inputNumber].remove()
    currentInputs[inputNumber-1].focus()
    rearrangeInputs(currentInputs, document.querySelectorAll('[data-container]'));

}

function rearrangeInputs(currentInputs, currentContainers){
    
    currentInputs.forEach((input, index) => input.setAttribute('data-htsinput', index.toString()));
    currentContainers.forEach((container, index) => container.setAttribute('data-container', index.toString()));
}

function formatInputBox(inputValue){

    const formattedHTS = inputValue.replace(htsIPattern, (raw, sg1, sg2, sg3) =>{
        if(sg1) return `${sg1}.`;
        if(sg2) return `${sg2}.`;
        if(sg3) return `${sg3}.`;
        
    })
    return formattedHTS;

}

function addEventListenerToInput(element){

    element.addEventListener('keydown', (event)=>{
        
        //Prevents more than 13 characters in hts code (taking into consideration the periods)
        if(element.value.length == 13 && !allowedKeys.includes(event.key)) event.preventDefault();

        //Active input formatter for periods
        if(element.value.match(htsIPattern) && event.key != 'Backspace' && event.key != 'Enter'){
            element.value = formatInputBox(element.value);
        }

        //Removes the previous input field
        if(event.key == 'Backspace' && element.value == ''){
            if(element.getAttribute('data-htsinput') == 0) return;
            event.preventDefault();
            deleteCurrentInput(element);
            rearrangeInputs(document.querySelectorAll('[data-htsinput]'));
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
        //Allows copying inputs
        if(event.ctrlKey && event.key == 'c') return;
        
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

    element.addEventListener('paste', (event) =>{
        event.preventDefault();
        const text = event.clipboardData.getData('text').match(validInputCharacters);
        if(text.length > 10){
            warning.style.display = 'block';
            return;
        }
        let htsCode = '';
        for (let index = 0; index < text.length; index++) {
            htsCode += text[index];
            if(index == 3 || index == 5 || index == 7) htsCode += '.';
            
        }
        element.value = htsCode;

    })

}

addEventListenerToInput(manualArea);
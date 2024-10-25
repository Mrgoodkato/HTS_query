const inputContainer = document.getElementById('manual_input_container');
const inputFiled = document.getElementById('hts_input_area');

const dotPattern = /[\.]/g

inputFiled.addEventListener('input', (event)=>{

    if(event.key == 'Enter'){
        const newInput = document.createElement('input');
        newInput.type = 'text';
    }

})
import config from "./config.js";
const submitPaste = document.getElementById('submit_paste');
const textArea = document.getElementById('hts_txt_area');
const submitManuel = document.getElementById('submit_manual');
const submitFile = document.getElementById('submit_file');

submitPaste.addEventListener('click', () => {
    
    const endpointURL = `${config.API_BASE_URL}/process_query`;
    fetch(endpointURL, {
        method: 'POST',
        headers: { 'Content-Type': 'application/json' },
        body: JSON.stringify({user_input: textArea.value})
    })
    .then(response => response.json())
    .then(result => console.log('Success!', result))
    .catch(error => console.log('Error', error));

});
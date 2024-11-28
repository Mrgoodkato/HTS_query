const submitPaste = document.getElementById('submit_paste');
const submitManuel = document.getElementById('submit_manual');
const submitFile = document.getElementById('submit_file');

submitPaste.addEventListener('click', () => {
    
    const textArea = document.getElementById('hts_txt_area');
    const formData = new FormData();
    formData.set('user_input', textArea.value);
    
    

});
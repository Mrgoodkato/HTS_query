const txtArea = document.getElementById('hts_txt_area');

txtArea.addEventListener('input', ()=>{

    let input = txtArea.value;

    const validCharacters = /^[0-9.\n]*$/g;

    if(!validCharacters.test(input)){
        txtArea.value = input.replace(/[^0-9.\n]/g, '')
        console.log('Replaced' )
    }

})
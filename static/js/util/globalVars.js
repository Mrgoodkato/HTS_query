export const allowedKeys = [
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

export const htsPattern = /(?:^[\d]{4}\.[\d]{2}\.[\d]{2}\.[\d]{2}$|\\r)|(?:^[\d]{4}\.[\d]{2}\.(?:[\d]{2}|[\d]{4})$|\\r)|(?:^[\d]{4}\.(?:[\d]{2}|[\d]{4}|[\d]{6})$)|(?:^[\d]{4}$|\\r)|(?:^[\d]{6}$|\\r)|(?:^[\d]{8}$|\\r)|(?:^[\d]{10}$|\\r)/;
export const htsFPattern = /(^[\d]{4})((?<=\1)[\d]{2})((?<=\2)[\d]{2})((?<=\3)[\d]{2}$)|(^[\d]{4})((?<=\1)[\d]{2})((?<=\2)[\d]{2}$)|(^[\d]{4})((?<=\1)[\d]{2}$)|(^[\d]{4}$)/
export const validCharacters = /^[0-9.\n]*$/g;
export const linePattern = /(?:^[\d]{4}(?:\.[\d]{2}){1,3}$)|(?:^[\d]{4,10})/gm;
export const punctuationPattern = /[ \r!\"#$%&\'()*+,-./:;<=>?@\[\]\^_`{|}~—]/g;
export const patternManualInput = /[a-zA-Z \r!\"#$%&\'()*+,\-:;<=>?@\[\]\^_`{|}~—\\]/g;
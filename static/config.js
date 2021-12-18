let language = document.getElementById('language');
Storedlang = localStorage.getItem('language')

if(Storedlang != undefined){
    language.value =Storedlang;
}

let editor;
window.onload = function() {
    editor = ace.edit("editor");
    editor.setTheme("ace/theme/twilight");
    editor.session.setMode("ace/mode/python");
}
function changetheme()
{
    let theme=document.getElementById('theme').value
    console.log(theme)
    
    if(theme == 'twilight')editor.setTheme("ace/theme/twilight");
    else if(theme == 'monokai')editor.setTheme("ace/theme/monokai");
    else if(theme == 'solarized_dark')editor.setTheme("ace/theme/solarized_dark");
    else if(theme == 'solarized_light')editor.setTheme("ace/theme/solarized_light");
}
function changeLanguage() {

    let lang = document.getElementById('language').value
    console.log(language)

    if(lang == 'cpp' || lang == 'cpp')editor.session.setMode("ace/mode/c_cpp");
    else if(lang == 'py')editor.session.setMode("ace/mode/python");
    else if(lang == 'c')editor.session.setMode("ace/mode/c_cpp");
    else if(lang == 'java')editor.session.setMode("ace/mode/java");
}

function sendData(lang,code,input) {
    const XHR  = new XMLHttpRequest(),
    formData = new FormData();

    formData.append('language',lang)
    formData.append('code_area',code)
    formData.append('input_area',input)
    XHR.addEventListener('load',function(event) {
        console.log('Data send')
    })
    XHR.onreadystatechange = function() {
        if(XHR.readyState === XMLHttpRequest.DONE) {
            console.log(XHR.responseText)
            document.getElementById('output-area').value = XHR.responseText
        }
    }
    XHR.open('POST','127.0.0.1:8000/run')
    XHR.send(formData)
}

document.getElementById('run-code').onclick = function(e) {
    e.preventDefault()
    let l = document.getElementById('language');
    localStorage.setItem("language",l.value)
    code = editor.getSession().getValue()
    input = document.getElementById('input_part')
    sendData(language.value,code,input.value)
}

function download(){
    code = editor.getSession().getValue()
    let langi = document.getElementById('language').value;
    const blob = new Blob([code],{type:"text/plain"});
    filename = "file.py"
    if(langi == 'cpp' ){filename="file.cpp";}
    else if(langi == 'c'){filename="file.c";}
    else if(langi == 'java'){filename="file.java";}
    downloadFile(blob,filename);
}
function downloadFile(blob,filename){
    const url= window.URL.createObjectURL(blob);
    const a = document.createElement("a");
    a.href=url;
    a.download=filename;
    a.click();
    a.remove();
    document.addEventListener("focus",w=>{window.URL.revokeObjectURL(blob)});

}


const moduleForm = document.getElementById("moduleForm")
const module_alert = document.getElementById("module-alert")
const module_title = document.getElementById('id_title')
const module_content = document.getElementById('id_content')
const module_video = document.getElementById('id_video')
const module_notes = document.getElementById('id_notes')
const module_ppt = document.getElementById('id_ppt')
const section = document.getElementById("section")
const module_csrf = document.getElementsByName("csrfmiddlewaretoken")


moduleForm.addEventListener('submit',(e)=>{
    e.preventDefault()
    const fd = new FormData()
    fd.append('title',module_title.value)
    fd.append('content',module_content.code)
    fd.append('video',module_video.value)
    fd.append('notes',module_notes.files[0])
    fd.append('ppt',module_ppt.files[0])
    fd.append('csrfmiddlewaretoken',module_csrf[0].value)
    fd.append('section',section.value)

    $.ajax({
        type:'POST',
        url:'/module/create/',
        enctype:'multipart/form-data',
        data:fd,
        success:function(response){
            if(response.status == 'ok'){
                module_alert.innerHTML = `<div class="alert alert-info">${response.message}!</div>`
                moduel_title.value=""
            }else{
                module_alert.innerHTML = `<div class="alert alert-danger">${response['message']['title']}!</div>`
                console.log(response);
                module_title.value=""
            }
        },
        error:function(error){
            moduel_alert.innerHTML = `<div class="alert alert-danger">${error.status}:${error.statusText}</div>`
        },
        cache:false,
        contentType:false,
        processData:false,
    })
})

function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}
const csrftoken = getCookie('csrftoken');
console.log(csrftoken)


let followBtn = document.querySelector("#follow-btn")
let likeBtn = document.querySelector("#like-btn")
const likeUrl = document.location.protocol+document.location.host+'/accounts/'+'user-like';
const followUrl = document.location.protocol+document.location.host+'/accounts/'+'user-follow';
const followerscCount = document.querySelector("#followers--count")
const likeCount = document.querySelector("#likes--count")
const userAction = async (type,userId)=>{

    let data = new FormData()
    data.append("user_id",userId)
const config ={
    method:'POST',
    headers:{
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
},
body: data
}   

 if(type=='follow'){
    let resData =  await fetch('http://127.0.0.1:8000/accounts/user-follow',config)
    return resData.json()
}else{
    let resData =  await fetch('http://127.0.0.1:8000/accounts/user-like',config)
    return resData.json()
}





}

likeBtn.addEventListener("click",async ()=>{

    let res_data = await userAction('like',likeBtn.getAttribute("user"));
    console.log(res_data)
    likeCount.textContent = 'people liked him '+res_data.count
    if(res_data.operation=='adding'){
    likeBtn.classList.add("cancel");
    likeBtn.textContent='dislike';
    
}else{
    likeBtn.classList.remove("cancel");
    likeBtn.textContent='follow';
}
})


followBtn.addEventListener("click",async ()=>{

    let res_data = await userAction('follow',followBtn.getAttribute("user"));
    followerscCount.textContent = 'followers '+res_data.count
    if(res_data.operation=='adding'){
    followBtn.classList.add("cancel");
    followBtn.textContent='unfollow';
    
}else{
    followBtn.classList.remove("cancel");
    followBtn.textContent='follow';
}
})

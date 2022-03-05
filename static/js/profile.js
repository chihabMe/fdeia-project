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

const userAction = (url,userId)=>{

    console.log(url)
    let d = new FormData()
    d.append("user_id",userId)
const config ={
    method:'POST',
    headers:{
        'Accept': 'application/json',
        'X-Requested-With': 'XMLHttpRequest', //Necessary to work with request.is_ajax()
        'X-CSRFToken': csrftoken,
},
body: d
}

    fetch('http://127.0.0.1:8000/accounts/user-follow',config).then((res)=>{return res.json() }).then((data)=>{
        console.log(data)
        followerscCount.textContent="follwers "+data.count

    })
    




}

    let follwed  = false 
followBtn.addEventListener("click",()=>{
    userAction(followUrl,followBtn.getAttribute("user"));
    if(!follwed){
    followBtn.classList.add("cancel");
    followBtn.textContent='follow';
}else{
    followBtn.classList.remove("cancel");
    followBtn.textContent='follow';
}
follwed=!follwed;
})

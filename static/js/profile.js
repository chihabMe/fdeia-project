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

//variables 
let followBtn = document.querySelector("#follow-btn")
let likeBtn = document.querySelector("#like-btn")
const likeUrl = document.location.protocol+document.location.host+'/accounts/'+'user-like';
const followUrl = document.location.protocol+document.location.host+'/accounts/'+'user-follow';
const followerscCount = document.querySelector("#followers--count")
const likeCount = document.querySelector("#likes--count")
const profileUserImage = document.querySelector("#profile--user--image")
let userId = likeBtn!=null ?  followBtn.getAttribute("userId"):null
//
const userAction = async (type,userId=null,image=null)=>{

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
    if(userId){
 if(type=='follow'){
    let resData =  await fetch('http://127.0.0.1:8000/accounts/user-follow',config)
    return resData.json()
}else if(type=='like'){
    let resData =  await fetch('http://127.0.0.1:8000/accounts/user-like',config)
    return resData.json()

}
}
if(image){
    console.log('runn')
 if(type=='imageChange'){
    console.log(image)
    data.append('image',image)
    config.body=data
        let resData =  await fetch('http://127.0.0.1:8000/accounts/user-profile-image-change',config)
        
        return resData.json()
}

}
}


// profile image change 

const profileImage = document.querySelector('#chose--image')
console.log(profileImage)
profileImage.addEventListener("change",async ()=>{
    let image = profileImage.files[0]

    if(image){
        const res_data = await userAction('imageChange',null,image)

        console.log(res_data)
        if(res_data.success){
            profileUserImage.src=res_data.imageUrl
        }

    }

})

//









likeBtn && likeBtn.addEventListener("click",async ()=>{

    let res_data = await userAction('like',userId);
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


followBtn && followBtn.addEventListener("click",async ()=>{

    let res_data = await userAction('follow',userId);
    followerscCount.textContent = 'followers '+res_data.count
    if(res_data.operation=='adding'){
    followBtn.classList.add("cancel");
    followBtn.textContent='unfollow';
    
}else{
    followBtn.classList.remove("cancel");
    followBtn.textContent='follow';
}
})

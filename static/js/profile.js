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
let base_url = window.location.protocol+'//'+window.location.host
const csrftoken = getCookie('csrftoken');
//variables 
let followBtn = document.querySelector("#follow-btn")
let likeBtn = document.querySelector("#like-btn")
const likeUrl = document.location.protocol+document.location.host+'/accounts/'+'user-like';
const followUrl = document.location.protocol+document.location.host+'/accounts/'+'user-follow';
const followerscCount = document.querySelector("#followers--count")
const likeCount = document.querySelector("#likes--count")
const profileUserImage = document.querySelector("#profile--user--image")
let userId = followBtn!=null ?  followBtn.getAttribute("user"):null
//
const userAction = async (type,userId=null,image=null,bioBody=null,postBody=null)=>{

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
    let resData =  await fetch(`${base_url}/accounts/user-follow`,config)
    return resData.json()
}else if(type=='like'){
    let resData =  await fetch(`${base_url}/accounts/user-like`,config)
    return resData.json()

}
}
if(image){
 if(type=='imageChange'){
    data.append('image',image)
    config.body=data
        let resData =  await fetch(`${base_url}/accounts/user-profile-image-change`,config)
        
        return resData.json()
}

}
if(type=='bioEdit'){

    data.append('bioBody',bioBody)
    config.data=data
    let resData = await fetch(`${base_url}/accounts/user-profile-boi-change`,config)
    return resData.json()
}
if(postBody){ 
    let newData = new FormData();
    newData.append("postBody",postBody);
    config.body = newData;
    console.log(config)
    let resData = await fetch(`${base_url}/post-add`,config)
    return resData.json();
}
 }
//profile boi eddit
let hiddenBoiText = document.querySelector("#profile--user--bio--eddit")
let BoiText = document.querySelector("#profile--user--bio")
let showHideHiddenTextButton = document.querySelector("#bio--eddit--button")
let showHideHiddenBoiText = false 
showHideHiddenTextButton && showHideHiddenTextButton.addEventListener('click',async()=>{
    if(!showHideHiddenBoiText){
        hiddenBoiText.style.display='block';
        showHideHiddenTextButton.innerHTML=`
        <svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M8 7H5a2 2 0 00-2 2v9a2 2 0 002 2h14a2 2 0 002-2V9a2 2 0 00-2-2h-3m-1 4l-3 3m0 0l-3-3m3 3V4" />
</svg>
`

    }else{
        
        let boiBody = hiddenBoiText.value
        
        hiddenBoiText.style.display='none'
       showHideHiddenTextButton.innerHTML= `<svg xmlns="http://www.w3.org/2000/svg" class="h-6 w-6" fill="none" viewBox="0 0 24 24" stroke="currentColor" stroke-width="2">
  <path stroke-linecap="round" stroke-linejoin="round" d="M11 5H6a2 2 0 00-2 2v11a2 2 0 002 2h11a2 2 0 002-2v-5m-1.414-9.414a2 2 0 112.828 2.828L11.828 15H9v-2.828l8.586-8.586z" />
</svg>`
    BoiText.textContent=boiBody    
    let res_data = await userAction('bioEdit',null,null,boiBody)
    
    }
    showHideHiddenBoiText=!showHideHiddenBoiText
})
//

// profile image change 

const profileImage = document.querySelector('#chose--image')
profileImage && profileImage.addEventListener("change",async ()=>{
    let image = profileImage.files[0]

    if(image){
        const res_data = await userAction('imageChange',null,image)

        if(res_data.success){
            profileUserImage.src=res_data.imageUrl
        }

    }

})

//









likeBtn && likeBtn.addEventListener("click",async ()=>{
    let res_data = await userAction('like',userId,null,null);
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


//porofile post add 

let profilePostButton = document.querySelector("#profile-post-form-button")
let profilePostForm = document.querySelector("#profile-post-form")
let profilePostInput = document.querySelector("#profile-post-input")
profilePostForm.addEventListener("submit",async(e)=>{
    e.preventDefault();
    let body = profilePostInput.value;
    let res_data = await userAction('postAdd',null,null,null,postBody=body);
    console.log(res_data)
 }
  )


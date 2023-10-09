document.addEventListener("DOMContentLoaded",()=>{
    console.log("scout page loaded")

    // New, Pending, Active, Sold, Rejected section
    // Grabbing html elements 
    let newButton = document.querySelector('#new');
    let pendingButton = document.querySelector('#pending');
    let activeButton = document.querySelector('#active');
    let soldButton = document.querySelector('#sold');
    let rejectedButton = document.querySelector('#rejected');

    let newDiv = document.querySelector('#newDiv');
    let pendingDiv = document.querySelector('#pendingDiv');
    let activeDiv = document.querySelector('#activeDiv');
    let soldDiv = document.querySelector('#soldDiv');
    let rejectedDiv = document.querySelector('#rejectedDiv');

    displayNew()


    // Event Listeners to toggle display
    newButton.addEventListener('click', ()=>displayNew())
    pendingButton.addEventListener('click', ()=>{displayPending()})
    activeButton.addEventListener('click', ()=>{displayActive()})
    soldButton.addEventListener('click', ()=>{displaySold()})
    rejectedButton.addEventListener('click', ()=>displayRejected())





    let submit = document.querySelector('#formSubmitInput')
    submit.addEventListener("submit", ()=>{
        console.log("FORM HAS BEEN SUBMITTED")
    })

    // Hide/show the estate input element depending on what is selected.
    let inEstateInput = document.querySelector('#inEstate');
    let estateNameDiv = document.querySelector('#estateNameDiv');
    let estateName = document.querySelector('#estateName');


    estateNameDiv.style.display = "none";
    estateName.required = false;

    inEstateInput.addEventListener("change", ()=>{
        if(inEstateInput.value==="yes"){
            estateNameDiv.style.display = "block"
            estateName.required = true;

        }else{
            estateNameDiv.style.display = "none";
            estateName.required = false;

        }
    })

     // Hide/show the street input element depending on what is selected.
    // let streetdiv = document.querySelector('#streetdiv');
    // streetdiv.style.display = "none";

    // let streetSelect = document.querySelector('#street');
    // streetSelect.addEventListener("change", ()=>{
    //     if(streetSelect.value==="other"){
    //         streetdiv.style.display = "block";
    //     }else{
    //         streetdiv.style.display = "none";
    //     }
    // })

    // Hide/show manager/owner input based on select option dropdown
    let bannerSelect = document.querySelector('#banner');
    let ownerManagerDiv = document.querySelector('#ownerManagerDiv')
    let uploadDiv = document.querySelector('#uploadDiv');

    ownerManagerDiv.style.display = "none";
    uploadDiv.style.display = "none";

    let managerName = document.querySelector('#managerName');
    let managerTel = document.querySelector('#managerTel');
    let bannerpic = document.querySelector('#bannerpic');

    // ownermanagername.required = false;
    // ownermanagertel.required = false;
    // uploadDiv.style.display = "block";

    bannerSelect.addEventListener("change", ()=>{
        if (bannerSelect.value=="no"){
            console.log("upload div should not show")
            uploadDiv.style.display = "none";
            bannerpic.required = false
            ownerManagerDiv.style.display = "block";
            managerName.required = true;
            managerTel.required = true;
        }else{
            console.log("upload div showwww!")
            ownerManagerDiv.style.display = "none";
            uploadDiv.style.display = "block";
            bannerpic.required = true;
            managerName.required = false;
            managerTel.required = false;    

        }
    })

    // property manager and property owner dynamic rendering

    let propManager = document.querySelector('#propManager');
    let propOwner = document.querySelector('#propOwner');
    let propManagerDiv = document.querySelector('#propManagerDiv');
    let propOwnerDiv = document.querySelector('#propOwnerDiv');
    // let managerName = document.querySelector('#managerName');
    // let managerTel = document.querySelector('#managerTel');
    let ownerName = document.querySelector('#ownerName');
    let ownerTel = document.querySelector('#ownerTel');


    // propOwnerDiv.style.display="none"
    // ownerName.required = false;
    // ownerTel.required = false;

    // if (propManager.checked){
    //     propManagerDiv.style.display="block";
    //     managerName.required = true;
    //     managerTel.required = true;  
    // }else{
    //     propManagerDiv.style.display="none";
    //     managerName.required = false;
    //     managerTel.required = false; 
    // }

    // if (propOwner.checked){

    //     propOwnerDiv.style.display="block"
    //     ownerName.required = true;
    //     ownerTel.required = true;
    // }else{
    //     propOwnerDiv.style.display="block";
    //     ownerName.required = false;
    //     ownerTel.required = false;
    // }
        






    function displayNew(){
        // e.preventDefault()
        newDiv.style.display="block";
        pendingDiv.style.display="none";
        activeDiv.style.display="none";
        soldDiv.style.display="none";
        rejectedDiv.style.display="none";
    }

    function displayPending(){
        // e.preventDefault()
        newDiv.style.display="none";
        pendingDiv.style.display="block";
        activeDiv.style.display="none";
        soldDiv.style.display="none";
        rejectedDiv.style.display="none";
    }

    function displayActive(){
        // e.preventDefault()
        newDiv.style.display="none";
        pendingDiv.style.display="none";
        activeDiv.style.display="block";
        soldDiv.style.display="none";
        rejectedDiv.style.display="none";
    }

    function displaySold(){
        // e.preventDefault()
        newDiv.style.display="none";
        pendingDiv.style.display="none";
        activeDiv.style.display="none";
        soldDiv.style.display="block";
        rejectedDiv.style.display="none";
    }

    function displayRejected(){
        // e.preventDefault()
        newDiv.style.display="none";
        pendingDiv.style.display="none";
        activeDiv.style.display="none";
        soldDiv.style.display="none";
        rejectedDiv.style.display="block";
    }

})


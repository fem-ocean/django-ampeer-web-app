document.addEventListener('DOMContentLoaded', ()=>{
    console.log("I AM WORKING")
    let acceptForm = document.getElementById('acceptForm');
    let scoutListings = document.getElementById('scoutListings');

    acceptForm.style.display = "none"
    scoutListings.style.display = "block";



    let submitButton = document.querySelector('#newListingSubmitButton');

    let video1 = document.getElementById('intVid');
    let video2 = document.getElementById('streetVid');
    let video3 = document.getElementById('compoundVid');



    let landlordReg = document.querySelector('#landlordReg');
    let selectOwnerOwner = document.querySelector('#selectOwnerOwner');
    let selectManager = document.querySelector('#selectManager');
    let dobMan = document.querySelector('#dobMan');


    let price = document.querySelector('#price');
   




    // VIDEO PREVIEW FUNCTIONALITY


    let videoContainer = document.querySelectorAll('.vidCont');
    // console.log(videoContainer)

    
    videoContainer.forEach(vidDiv=>{
        vidDiv.addEventListener('mouseenter', function () {
            const propertyID = this.getAttribute('data-propertyId')
            console.log(`property-ID:${propertyID}`)
            console.log(`I am In the Vid div with id ${propertyID}`);

            const videoElement = this.querySelector('video');
            const videoPreview = this.querySelector('.video-preview');

            videoPreview.style.display = 'none';
            videoElement.style.display = 'block';
            videoElement.play();

        });
    })

    videoContainer.forEach(vid=>{
        vid.addEventListener('mouseleave', function (){
            const propertyID = this.getAttribute(`data-propertyID`);
            console.log(`propertyID mouseleave:${propertyID}`);

            const videoElement = this.querySelector('video');
            const videoPreview = this.querySelector('.video-preview');

            videoElement.style.display = 'none';
            videoElement.pause();
            videoPreview.style.display = 'block';

        });
    })

  
    

    
})



const handleAccept = (...args) => {
    // Once a listing is accepted, hide all scout listings and show the form. 2, change the status of the scouted Listing to active when listingspecialist post the property. 
    
    console.log(args);
    // send the id of the scouted property clicked to d backend through the property info section on d frontend
    const scoutedProperty = parseInt(args[0]);
    // document.querySelector('#scoutedPropertyId').value = scoutedProperty;

    let acceptForm = document.getElementById('acceptForm');
    let scoutListings = document.getElementById('scoutListings');

    acceptForm.style.display = "block"
    scoutListings.style.display = "none";



    // Hide/show registration of New LandlordUser based on select option dropdown
    let landlordReg = document.querySelector('#landlordReg');
    let regNewPropOwnerDiv = document.querySelector('#regNewPropOwnerDiv')
    let ownerSelectDiv = document.querySelector('#ownerSelectDiv');

    // Required field for dropdown selection
    // let selectOwner = document.querySelector('#selectOwner');
    // Required Fields NEw Landlord User Form
    let ownerMaritalStatus = document.querySelector('#ownerMaritalStatus');
    let dob = document.querySelector('#dob');
    let intlpassport = document.querySelector('#intlpassport');
    let govtid = document.querySelector('#govtid');
    let bankname = document.querySelector('#bankname');
    let accountno = document.querySelector('#accountno');
    let street = document.querySelector('#street');
    let housenumber = document.querySelector('#housenumber');

    // Validation
    // selectOwner.required = false;
    // ownerMaritalStatus.required = false;
    // dob.required = false;
    // intlpassport.required = false;
    // govtid.required = false;
    // bankname.required = false;
    // accountno.required = false;
    // street.required = false;
    // housenumber.required = false;



    // Div display
    regNewPropOwnerDiv.style.display = "none";
    ownerSelectDiv.style.display = "none";


    landlordReg.addEventListener("change", ()=>{
        if (landlordReg.value=="no"){
            console.log("select owner hide/ new propowner form show")
            ownerSelectDiv.style.display = "none";
            regNewPropOwnerDiv.style.display = "block";
            // selectOwner.required = false;
            // ownerMaritalStatus.required = true;
            // dob.required = true;
            // intlpassport.required = true;
            // govtid.required = true;
            // bankname.required = true;
            // accountno.required = true;
            // street.required = true;
            // housenumber.required = true;
        }else{
            console.log("select owner show/ new propowner form hide")
            ownerSelectDiv.style.display = "block";
            regNewPropOwnerDiv.style.display = "none";
            // selectOwner.required = true;
            // ownerMaritalStatus.required = false;
            // dob.required = false;
            // intlpassport.required = false;
            // govtid.required = false;
            // bankname.required = false;
            // accountno.required = false;
            // street.required = false;
            // housenumber.required = false;
        }
    })



    // Hide/show registration of New PropertyManagerUser based on select option dropdown
    let propManagerReg = document.querySelector('#propManagerReg');
    let regNewPropManagerDiv = document.querySelector('#regNewPropManagerDiv')
    let managerSelectDiv = document.querySelector('#managerSelectDiv');

    // Required field for dropdown selection
    let selectManager = document.querySelector('#selectManager');
    // Required Fields NEw Property Manager User Form
    let dobMan = document.querySelector('#dobMan');
    let intlpassportMan = document.querySelector('#intlpassportMan');
    let govtidMan = document.querySelector('#govtidMan');
    let banknameMan = document.querySelector('#banknameMan');
    let accountnoMan = document.querySelector('#accountnoMan');
    let companyName = document.querySelector('#companyName');
    let companyAddress = document.querySelector('#companyAddress');

    // Validation
    // selectManager.required = false;
    // dobMan.required = false;
    // intlpassportMan.required = false;
    // govtidMan.required = false;
    // banknameMan.required = false;
    // accountnoMan.required = false;
    // companyName.required = false;
    // companyAddress.required = false;

    // Div display
    regNewPropManagerDiv.style.display = "none";
    managerSelectDiv.style.display = "none";

    propManagerReg.addEventListener("change", ()=>{
        if (propManagerReg.value=="no"){
            console.log("select manager hide/ new manageruser form show")
            managerSelectDiv.style.display = "none";
            regNewPropManagerDiv.style.display = "block";
            // selectManager.required = false;
            // dobMan.required = true;
            // intlpassportMan.required = true;
            // govtidMan.required = true;
            // banknameMan.required = true;
            // accountnoMan.required = true;
            // companyName.required = true;
            // companyAddress.required = true;
        }else{
            console.log("select manager show/ new propmanager form hide")
            managerSelectDiv.style.display = "block";
            regNewPropManagerDiv.style.display = "none";
            // selectManager.required = true;
            // dobMan.required = false;
            // intlpassportMan.required = false;
            // govtidMan.required = false;
            // banknameMan.required = false;
            // accountnoMan.required = false;
            // companyName.required = false;
            // companyAddress.required = false;
        }
    })


    let locationSelect = document.querySelector('#locationSelect');
    let manualLocationDiv = document.querySelector('#manualLocationDiv');

    manualLocationDiv.style.display = "none";

    locationSelect.addEventListener("change", ()=>{
        if (locationSelect.value == "abx"){
            manualLocationDiv.style.display = "block";
        }else{
            manualLocationDiv.style.display = "none";
        }
    })
    

    // Estate
    let inEstate = document.querySelector('#inEstate');
    let estateNameDiv = document.querySelector('#estateNameDiv');

    estateNameDiv.style.display = "none";

    inEstate.addEventListener('change', ()=>{
        if (inEstate.value == "yes"){
            estateNameDiv.style.display = "block";
        }else{
            estateNameDiv.style.display = "none";
        }
    })


    
    let form = document.querySelector('#propForm');

    form.addEventListener("submit", (e)=>{  
        console.log("form has been submitted" + e)
        e.preventDefault();
        
        
        let formData = new FormData(form);

        console.log(`scouted Property has id: ${scoutedProperty}`);

        formData.append("scouted_prop_id", scoutedProperty )

        console.log(formData)
        fetch('/reagency/role/listingspecialist',{
            method:"POST",
            body: formData,
        })
        .then(response=>response.json())
        .then(result=>console.log(result))
        .catch(err=>(console.log(err)))
    })  
}

function handleReject(rejectPropertyId){
    // show a modal that allows listingspecialist to give a reason for rejection. Submits it and stores it in the database

    console.log("reject Button activated");
   

    const rejectForm = document.querySelector(`#rejectPropertyForm`);
    console.log(rejectForm.action);


    const newAction = `rejectproperty/${rejectPropertyId}`
    rejectForm.setAttribute('action', newAction)
    console.log(rejectForm.action)


}

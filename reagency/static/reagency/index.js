document.addEventListener('DOMContentLoaded', ()=>{
  
    // Submit registration form for becoming a scout
    let registerScoutButton = document.querySelector('#scoutsubmit');
    let registerScoutForm = document.querySelector('#scoutform');
    let formButton = document.querySelector('#formSubmitButton');
    
    registerScoutButton.addEventListener('click', ()=>{
        // console.log(registerScoutForm.checkValidity())
        // checks if all fields are valid
        if (registerScoutForm.checkValidity()){
            formButton.click() 
        }else{
            alert("Complete all required fields")
        }
    })


    // Submit registration form for becoming a Listing Specialist
    let registerListingSpecialistButton = document.querySelector('#listingSpecialistSubmit');
    let listingSpecialistForm = document.querySelector('#listingSpecialistForm');
    let listingSpecialist_formSubmitButton = document.querySelector('#listingSpecialist_formSubmitButton');

    
    registerListingSpecialistButton.addEventListener('click', ()=>{
        // checks if all fields are valid
        if (listingSpecialistForm.checkValidity()){
            listingSpecialist_formSubmitButton.click() 
        }else{
            alert("Complete all required fields")      
        }
    })


    // Submit registration form for becoming a Property Manager
    let registerPropertyManagerButton = document.querySelector('#propertyManagerSubmit');
    let propertyManagerForm = document.querySelector('#propertyManagerForm');
    let propertyManager_formSubmitButton = document.querySelector('#propertyManager_formSubmitButton');

    
    registerPropertyManagerButton.addEventListener('click', ()=>{
        // checks if all fields are valid
        if (propertyManagerForm.checkValidity()){
            propertyManager_formSubmitButton.click() 
        }else{
            alert("Complete all required fields")      
        }
    })


    // Submit registration form for becoming a Property Owner
    let registerPropertyOwnerButton = document.querySelector('#propertyOwnerSubmit');
    let propertyOwnerForm = document.querySelector('#propertyOwnerForm');
    let propertyOwner_formSubmitButton = document.querySelector('#propertyOwner_formSubmitButton');

    
    registerPropertyOwnerButton.addEventListener('click', ()=>{
        // checks if all fields are valid
        if (propertyOwnerForm.checkValidity()){
            propertyOwner_formSubmitButton.click() 
        }else{
            alert("Complete all required fields")      
        }
    })


    // Search property form show price options dynamically
    let rentSale = document.getElementById('rentSale');
    let rentPriceSpan = document.getElementById('rentPriceSpan');
    let shortletPriceSpan = document.getElementById('shortletPriceSpan');
    let salePriceSpan = document.getElementById('salePriceSpan');

    rentPriceSpan.style.display = "inline";
    salePriceSpan.style.display = "none";
    shortletPriceSpan.style.display = "none";


    rentSale.addEventListener('change', ()=>{
        if (rentSale.value=="rent"){
            rentPriceSpan.style.display = "inline";
            salePriceSpan.style.display = "none";
            shortletPriceSpan.style.display = "none";
        }else if(rentSale.value=="shortlet"){
            rentPriceSpan.style.display = "none";
            shortletPriceSpan.style.display = "inline";
            salePriceSpan.style.display = "none";
        }else{
            rentPriceSpan.style.display = "none";
            shortletPriceSpan.style.display = "none";
            salePriceSpan.style.display = "inline";
        }
    })


    // let propertySearchDiv = document.getElementById('listingSpecialistProperties');
    // if (propertySearchDiv != ""){
    //     propertySearchDiv.innerHTML=""
    // }



    // location dynamic search
    let locationInput = document.querySelector('#location-input');
    let locationSelect = document.querySelector('#location-select');
    locationSelect.style.display = "none";
    let hiddenLocationValue = document.querySelector('#hiddenLocationValue');

    locationInput.addEventListener('input', ()=>{
        const query = locationInput.value

        fetch(`/reagency/searchaddress?q=${query}`)
        .then(response=>response.json())
        .then(result=>{
            console.log(result)
            locationSelect.style.display = "block";
            locationSelect.innerHTML = '';

            result.forEach(location=>{
                let list = document.createElement('li');
                list.className = "listResult"
                let div = document.createElement('div');
                div.className = "queryResult"
                
                div.innerHTML = `${location.street}, ${location.estate}, ${location.area}`;
                // div.setAttribute("data-locid", `${location.id}`);
                div.onclick = ()=>{
                    // hiddenLocationValue.setAttribute("data-locationid", `${location.id}` )
                    console.log(location.id)
                    hiddenLocationValue.value = location.id
                    locationInput.value = div.textContent;
                    locationSelect.style.display ="none"; 
                    // console.log(location.id)

                    // let locationId = parseInt(location.getAttribe('data-locationid'))                   
                }
                
                list.appendChild(div);

                

                locationSelect.append(list);

                // if(location.estate == 'not in an estate'){
                //     option.value = location.street, location.area
                // }else if(location.estate == 'other'){
                //     option.value = location.street, location.area
                // }else{
                //     option.value = location.street, location.estate_name, location.area
                // }

                // locationSelect.style.display = "inline";
                // let event = new MouseEvent('mousedown', {
                //     bubbles: true,
                //     cancelable: true,
                //     view: window
                // })
                // locationSelect.dispatchEvent(event);
            })

            
        })
    })
    
    // location.addEventListener('keydown', (e)=>{

        // get the key pressed;
        //use the key to perform a regex on the locations on the backend
        //return the locations as a dropdown list
        
        // const locSearchKey = e.key;
        // console.log(locSearchKey);
        // locArray.push(locSearchKey);
        // console.log(locArray)
        // findWithRegex(locArray)
    // })



    // location.addEventListener('input', (e)=>{
    //     const inputVal = e.target.value;
    //     const alphaNumericValue = inputVal.replace(/[^a-zA-Z0-9]/g, '');
    //     findWithRegex(alphaNumericValue)
    // })

    // function findWithRegex(val){
    //    console.log(stringedAddress)
    //    fetch(`/reagency/searchaddress?q=${alphaNumericValue}`)
    //     .then(response=>response.json())
    //     .then(result=>console.log(result))
    // }

    // function findWithRegex(string){
    //    console.log(string);
    //    fetch(`/reagency/searchaddress?q=${string}`)
    //     .then(response=>response.json())
    //     .then(result=>console.log(result))
    // }
    


    // location.addEventListener('keyup', ()=>{
    //     console.log(locArray)
    // })

    let propertyForm = document.querySelector('#propertySearchForm');

    propertyForm.addEventListener('submit', (e)=>{
        e.preventDefault();
        // document.querySelector('#listingSpecialistProperties').innerHTML = ""

    
        let rentSale = document.getElementById('rentSale');
        let location = document.querySelector('#location-input');
        let loc = document.querySelector('#hiddenLocationValue');

        let address = document.getElementById('address');
        let typeOfHouse = document.getElementById('typeOfHouse');
        let numberOfBed = document.getElementById('bed');

        let minPriceRent = document.getElementById('minPriceRent');
        let maxPriceRent = document.getElementById('maxPriceRent');
        let minPriceShortlet = document.getElementById('minPriceShortlet');
        let maxPriceShortlet = document.getElementById('maxPriceShortlet');
        let minPriceBuy = document.getElementById('minPriceBuy');
        let maxPriceBuy = document.getElementById('maxPriceBuy');

        // var locationId;
        // if (loc){
        //     locationId = parseInt(location.getAttribute('data-locationid'))
        //     // console.log(locationId)
            
        // }


        if (rentSale.value == "rent"){
            var min = parseInt(minPriceRent.value);
            var max = parseInt(maxPriceRent.value);
    //         console.log(`Rentmin:${min}`)
    //         console.log(`Rentmax:${max}`)

        }else if(rentSale.value =="shortlet"){
            var min = parseInt(minPriceShortlet.value);
            var max = parseInt(maxPriceShortlet.value);
    //         console.log(`Shortletmin:${min}`)
    //         console.log(`Shortletmax:${max}`)


        }else{
            var min = parseInt(minPriceBuy.value);
            var max = parseInt(maxPriceBuy.value);
    //         console.log(`Buymin:${min}`)
    //         console.log(`Buymax:${max}`)

        }

        const ren = rentSale.value;
        const add = loc.value;
        // console.log(add)
        const typ = typeOfHouse.value;
        const bed = numberOfBed.value;
        const minPrice = min;
        const maxPrice = max;

        // console.log(minPrice);
    //     console.log(maxPrice);


        const userSearchedProperties = document.getElementById('userSearchedProperties');
        fetch(`/reagency/propertysearch?rent=${ren}&loc=${add}&type_of_house=${typ}&bed=${bed}&min=${minPrice}&max=${maxPrice}`)
            .then(response=>response.json())
            .then(result => {
                if(result.results > 0){
                    console.log(result);
                    userSearchedProperties.innerHTML = ""; 
                    
                    // const properties = JSON.parse(result.all_properties);
                    // console.log(properties);

                    // GET ALL THE PROPERTIES SEARCHED FOR BY THE USER
                    result.all_properties.forEach(property=>{
                        var resultDiv = document.createElement('div');
                        resultDiv.classList.add('card', 'listingCard', 'mx-3', 'my-3');
                        resultDiv.style.width = '18rem';
                        resultDiv.style.height = '400px';

                        resultDiv.setAttribute('data-bs-target', '#propertyVideos');
                        resultDiv.setAttribute('data-bs-toggle', 'modal');


                        let firstDiv = document.createElement('div');
                        firstDiv.classList.add('vidCont');

                        let video1 = document.createElement('video');
                        video1.src = `${property.int_vid}`
                        video1.setAttribute('muted', "");
                        video1.setAttribute('loop', "");
                        video1.setAttribute('autoplay', "");
                        video1.classList.add('video-auto');


                        let video2 = document.createElement('video');
                        video2.src = `${property.int_vid}`
                        video2.classList.add('video-preview');
                        video2.setAttribute('muted', "");

                        let secondDiv = document.createElement('div');
                        secondDiv.classList.add('card-body');

                        let heading5 = document.createElement('h5');
                        heading5.classList.add("card-title");

                        let paragraph1 = document.createElement('p');
                        paragraph1.classList.add("card-text");

                        let paragraph2 = document.createElement('p');
                        paragraph2.classList.add("card-text");

                        let priceSpan = document.createElement('span');
                        priceSpan.classList.add('priceTag', 'badge', 'text-bg-danger')

                        let priceChildSpan = document.createElement('span');
                        priceChildSpan.innerHTML = "&#x20A6;"

                        priceSpan.append(priceChildSpan)



                        if (property.is_active) {

                            heading5.textContent = `Area: ${property.prop_location__area_name}`;
                            paragraph1.textContent = `Estate: ${property.prop_location__estate_name}`;
                            priceSpan.append(`${property.price}`)
                            paragraph2.textContent = `Street: ${property.prop_location__street}`;
                        } else {
                            heading5.textContent = "This Property may have been locked by another user. You can check back later."
                        }



                        // let thirdDiv = document.createElement('div');
                        // thirdDiv.classList.add('flex-row', 'justify-content-center', 'mt-2');
                        // thirdDiv.id = "likeUnlike";
                        

                        secondDiv.appendChild(heading5);
                        secondDiv.appendChild(paragraph1);
                        secondDiv.appendChild(paragraph2);

                        firstDiv.appendChild(video1);
                        firstDiv.appendChild(video2);

                        resultDiv.appendChild(firstDiv);
                        resultDiv.appendChild(secondDiv);
                        resultDiv.appendChild(priceSpan)

                            

                        resultDiv.addEventListener('click', function(){
                            if (!property.is_active){
                                alert("This property is currently locked by another user. Check back later")
                                resultDiv.setAttribute('data-bs-toggle', '');
                            }else{
                                // console.log(property.id)
                                let modalHeader1 = document.querySelector(`#propertyVideosLabel1`);
                                let modalHeader2 = document.querySelector(`#propertyVideosLabel2`);
                                let modalHeader3 = document.querySelector(`#propertyVideosLabel3`);

                                let videoIntSelect = document.querySelector('#videoIntSelect');
                                videoIntSelect.src = property.int_vid;
                                videoIntSelect.style.border = '3px solid blue'

                                let videoCompSelect = document.querySelector('#videoCompSelect');
                                videoCompSelect.src = property.ext_vid;

                                let videoStreetSelect = document.querySelector('#videoStreetSelect');
                                videoStreetSelect.src = property.street_vid;


                                let mainVideoDisplay = document.querySelector('#mainVideoDisplay');
                                mainVideoDisplay.src = property.int_vid
                                mainVideoDisplay.classList.add('width', '100%')
                                mainVideoDisplay.classList.add('height', '100%')
                                mainVideoDisplay.classList.add('position', 'absolute')



                                let interiorCard = document.querySelector('#interiorCard');
                                let compoundCard = document.querySelector('#compoundCard');
                                let streetCard = document.querySelector('#streetCard');

                                interiorCard.addEventListener('click', function(){
                                    mainVideoDisplay.src = property.int_vid;
                                    videoCompSelect.style.border = 'none';
                                    videoStreetSelect.style.border = 'none';
                                    videoIntSelect.style.border = '3px solid blue'

                                })

                                compoundCard.addEventListener('click', function(){
                                    mainVideoDisplay.src = property.ext_vid;
                                    videoCompSelect.style.border = '3px solid blue';
                                    videoStreetSelect.style.border = 'none';
                                    videoIntSelect.style.border = 'none'
                                })

                                streetCard.addEventListener('click', function(){
                                    mainVideoDisplay.src = property.street_vid;
                                    videoCompSelect.style.border = 'none';
                                    videoStreetSelect.style.border = '3px solid blue';
                                    videoIntSelect.style.border = 'none'
                                })



                                modalHeader1.textContent = `${property.bed} ${property.type} for ${property.rent_sale}`
                                modalHeader2.textContent = `${property.house_number}, ${property.prop_location__street}, ${property.prop_location__estate_name},  ${property.prop_location__area_name}`
                                modalHeader3.innerHTML= "";
                                // modalHeader3.append(`${property.price}`)
                                modalHeader3.innerHTML = `<span>&#x20A6;</span>${property.price}`

                                // For Flutterwave Payment
                                propertyPaymentButton = document.querySelector('#paymentButton');    
                                propertyPaymentButton.setAttribute("data-propid", property.id);

                                propertyPaymentButton.addEventListener('click', function(){

                                // USING INLINE JAVASCRIPT(FRONTEND FOR PAYMENT PROCESSING)
                                    FlutterwaveCheckout({
                                        public_key: "FLWPUBK_TEST-3c13341f3ee11d92ea71726145c102ce-X",
                                        tx_ref: Date.now(),
                                        amount: property.price * 0.1,
                                        currency: "NGN",
                                        payment_options: "card, account, ussd",
                                        redirect_url: "http:127.0.0.1:8000/reagency/properties_paid",
                                        // meta: {
                                        // consumer_id: 23,
                                        // consumer_mac: "92a3-912ba-1192a",
                                        // },
                                        customer: {
                                            email:result.user_details.email,
                                            phone_number: result.user_details.tel,
                                            name: result.user_details.name,
                                        },
                                        customizations: {
                                            title: "Ampeer",
                                            description: "Deposit 10% to Lock this property",
                                            logo: "https://www.logolynx.com/images/logolynx/22/2239ca38f5505fbfce7e55bbc0604386.jpeg",
                                        },
                                    });

                                    const propertyId = propertyPaymentButton.getAttribute("data-propid")
                                    console.log(propertyId)


                                    fetch(`initiatepayment`,{
                                        method: "POST",
                                        headers: {
                                            'Content-Type': 'application/json'
                                        },
                                        body: JSON.stringify({
                                            propertyid: `${propertyId}`,
                                            amount: `${property.price*0.1}` 
                                        })
                                    })
                                    .then(response=>{   
                                        if (!response.ok){
                                            throw new Error(`HTTP error! Status: ${response.status}`)
                                        }
                                        return response.json()})
                                    .then(result=>{
                                        console.log(result)
                                        if (result.success==true){
                                            window.location.href = result.redirect_url
                                        }else{
                                            alert(result.message)
                                        }

                                    })
                                    .catch(err =>{
                                        console.error(`Fetch error: ${err}`)
                                    })
                                })

                            }
                            
                            
                        })

                            
                        // LIKING AND UNLIKING A PROPERTY
                        var likeSpan;
                        let isInArray;
                        try{
                            isInArray = result.allLikedPropertiesIdList.indexOf(property.id)>=0;
                            console.log(isInArray)
                        }
                        catch(err){
                            console.error('An error occured' + err.message )
                        }

                        if (isInArray){
                            likeSpan = document.createElement('span');
                            likeSpan.classList.add('unlike');
                            likeSpan.id = `like_${property.id}`;
                            likeSpan.addEventListener('click', function(){
                                handleImageLikeUnlike(property.id, result.allLikedPropertiesIdList, isInArray);
                                console.log("I am about to be Unliked")
                            })
                            

                        }else{
                            likeSpan = document.createElement('span');
                            likeSpan.classList.add('like');
                            likeSpan.id = `like_${property.id}`;
                            likeSpan.addEventListener('click', function (){
                                handleImageLikeUnlike(property.id, result.allLikedPropertiesIdList, isInArray);
                                console.log("I am about to be liked")
                            })
                        }

                        resultDiv.appendChild(likeSpan);
                        userSearchedProperties.append(resultDiv);


                        // VIDEO PREVIEW FUNCTIONALITY
                        let videoContainer = document.querySelectorAll('.vidCont');
                        console.log(videoContainer);
                        // videoContainer.setAttribute('data-propertyId', `${property.id}`)

                        videoContainer.forEach(vidDiv=>{
                            vidDiv.addEventListener('mouseenter', function () {
                                // const propertyID = this.getAttribute('data-propertyId')
                                // console.log(`property-ID:${propertyID}`)
                                // console.log(`I am In the Vid div with id ${propertyID}`);

                                const videoElement = this.querySelector('.video-auto');
                                const videoPreview = this.querySelector('.video-preview');

                                videoPreview.style.display = 'none';
                                videoElement.style.display = 'block';
                                videoElement.play();
                            });
                        })

                        videoContainer.forEach(vid=>{
                            vid.addEventListener('mouseleave', function (){
                                // const propertyID = this.getAttribute(`data-propertyID`);
                                // console.log(`propertyID mouseleave:${propertyID}`);

                                const videoElement = this.querySelector('.video-auto');
                                const videoPreview = this.querySelector('.video-preview');

                                videoElement.style.display = 'none';
                                videoElement.pause();
                                videoPreview.style.display = 'block';
                            });
                        })
                        
                    })


                    
                    

                }else{
                    userSearchedProperties.innerHTML = "<p>No properties found. Try a different search parameters.</p>"
                }
                

            })
            // )
            .catch(err => console.log(err))
    })



    // Video Preview Functionality

    // let video = document.querySelectorAll('video');
    // let videoPreview = document.querySelectorAll('.video-preview');

    // videoContainer.addEventListener('mouseenter', () => {
    //     video.style.display = 'block';
    //     video.play();
    //     videoPreview.style.display = 'none';
    // });

    // videoContainer.addEventListener('mouseleave', () => {
    //     video.style.display = 'none';
    //     video.pause();
    //     videoPreview.style.display = 'block';
    // });





    function handleImageLikeUnlike(id, arr, isInArray) {
        console.log(id);
        console.log(arr);
        console.log(isInArray)

        
        // I neeed to make a call to find out if the property id is in the array or not.

        fetch(`likeunlike/${id}`)
            .then(response=>response.json())
            .then(result=>{
                console.log(result);

                arr = result.allLikedPropertiesIdList
                isInArray = arr.indexOf(id)>=0;
                console.log("isInArray2nd" + isInArray)

                // Get the number of likes span and its number
                let numOfLikesSpan = document.querySelector(`#numOfLikesSpan`);
                let numOfLikes = numOfLikesSpan.textContent;

                // if property is liked, reduce the number if liked property and change the image
                let likeSpan = document.querySelector(`#like_${id}`)
                if (isInArray){
                    console.log("property liked is True. Time to Unlike");
                    fetch(`unlike/${id}`)
                        .then(response=>response.json())
                        .then(result=>{
                            console.log(result);
                            console.log(likeSpan)
                            likeSpan.classList.remove('unlike');
                            likeSpan.classList.add('like');
                            numOfLikesSpan.textContent = parseInt(numOfLikes) - 1;

                        })
                }

                if (!isInArray){
                    console.log("property liked is False. Time to Like");
                    fetch(`like/${id}`)
                        .then(response=>response.json())
                        .then(result=>{
                            console.log(result);
                            likeSpan.classList.remove('like');
                            likeSpan.classList.add('unlike');
                            numOfLikesSpan.textContent = parseInt(numOfLikes) + 1;
                        })
                }
            })
        


        // fetch(`/isliked/${id}`)
        // .then(response=> response.json())
        // .then(result => {
        //     console.log(`is_liked is: ${result.is_liked}`)
            
        //     const loveImg = document.getElementById(`like_${id}`);

        //     if (result.is_liked) {
        //         console.log("post liked is true")
        //         fetch(`/unlike/${id}`)
        //             .then(response => response.json())
        //             .then(result => {
        //                 console.log(result.message);
        //                 loveImg.classList.remove('unlike');
        //                 loveImg.classList.add('like');
        //                 numOfLikesSpan.textContent = parseInt(numOfLikes) - 1;

        //             })
        //     } else {
        //         console.log("post liked is false")
        //         fetch(`/like/${id}`)
        //             .then(response => response.json())
        //             .then(result => {
        //                 // console.log(result);
        //                 loveImg.classList.remove('like');
        //                 loveImg.classList.add('unlike');
        //                 if (result.message == "liked successfully"){   
        //                     numOfLikesSpan.textContent = parseInt(numOfLikes) + 1;
        //                     // console.log(numOfLikesSpan)
        //                 }
        //             })
        //     }
        // })

    }

    // FLUTTERWAVE PAYMENT INTEGRATION
        // propertyPaymentButton = document.querySelector('#paymentButton');    

        // propertyPaymentButton.addEventListener('click', function(){
        //     const propertyId = propertyPaymentButton.getAttribute("data-propid")
        //     console.log(propertyId)
            
            // USING BACKEND FOR PAYMENT PROCESSING
            // fetch(`initiatepayment/${propertyId}`)
            //     .then(response=>response.json())
            //     .then(result=>{
            //         console.log(result)
            //     })

            
            // USING INLINE JAVASCRIPT(FRONTEND FOR PAYMENT PROCESSING)
        //         FlutterwaveCheckout({
        //             public_key: "FLWPUBK_TEST-3c13341f3ee11d92ea71726145c102ce-X",
        //             tx_ref: Date.now(),
        //             amount: property.price * 0.1,
        //             currency: "NGN",
        //             payment_options: "card, account, ussd",
        //             redirect_url: "http:127.0.0.1:8000/reagency/properties_paid",
        //             // meta: {
        //             // consumer_id: 23,
        //             // consumer_mac: "92a3-912ba-1192a",
        //             // },
        //             customer: {
        //                 email:result.user_details.email,
        //                 phone_number: result.user_details.tel,
        //                 name: result.user_details.name,
        //             },
        //             customizations: {
        //                 title: "Ampeer",
        //                 description: "Deposit 10% to Lock this property",
        //                 logo: "https://www.logolynx.com/images/logolynx/22/2239ca38f5505fbfce7e55bbc0604386.jpeg",
        //             },
        //         });


        // })

        
                    
    

    
    


})




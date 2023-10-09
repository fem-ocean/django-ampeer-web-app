document.addEventListener('DOMContentLoaded', function(){
    resultDiv = document.querySelectorAll(`.listingCard`)
    console.log(resultDiv)

    resultDiv.forEach(property=>{
    
        property.addEventListener('click', function(){
            console.log("I am working")
            console.log(document.querySelector('.listingCard').getAttribute("data-propertyId"))
            let propertyId = document.querySelector('.listingCard').getAttribute("data-propertyId")

            let modalHeader1 = document.querySelector(`#propertyVideosLabel1`);
            let modalHeader2 = document.querySelector(`#propertyVideosLabel2`);
            let modalHeader3 = document.querySelector(`#propertyVideosLabel3`);  
            let videoIntSelect = document.querySelector('#videoIntSelect');
            let videoExtSelect = document.querySelector('#videoCompSelect');
            let videoStreetSelect = document.querySelector('#videoStreetSelect');


            let videoIntNode = document.querySelector(`#video-${propertyId}`)
            let videoExtNode = document.querySelector(`#extVideo-${propertyId}`);
            let videoStreetNode = document.querySelector(`#streetVideo-${propertyId}`);
            
            videoIntSelect.src = videoIntNode.src;
            videoIntSelect.style.border = '3px solid blue';
            videoExtSelect.src = videoExtNode.src;
            videoStreetSelect.src = videoStreetNode.src;
            
            let mainVideoDisplay = document.querySelector('#mainVideoDisplay');
            mainVideoDisplay.src = videoIntNode.src;
            
            
            let interiorCard = document.querySelector('#interiorCard');
            let compoundCard = document.querySelector('#compoundCard');
            let streetCard = document.querySelector('#streetCard');
            
            interiorCard.addEventListener('click', function(){
                mainVideoDisplay.src = videoIntNode.src;
                videoCompSelect.style.border = 'none';
                videoExtSelect.style.border = 'none';
                videoIntSelect.style.border = '3px solid blue'  
            })
            
            compoundCard.addEventListener('click', function(){
                mainVideoDisplay.src = videoExtNode.src;
                videoExtSelect.style.border = '3px solid blue';
                videoStreetSelect.style.border = 'none';
                videoIntSelect.style.border = 'none'
            })
            
            streetCard.addEventListener('click', function(){
                mainVideoDisplay.src = videoStreetNode.src;
                videoExtSelect.style.border = 'none';
                videoStreetSelect.style.border = '3px solid blue';
                videoIntSelect.style.border = 'none'
            })
            
            let bed = document.querySelector('#propertyBed').textContent;
            let type = document.querySelector('#propertyType').textContent;
            let rentSale = document.querySelector('#propertyRentSale').textContent;
            let houseNumber = document.querySelector('#propertyHouseNumber').textContent;
            let street = document.querySelector('#propertyStreet').textContent;
            let estateName = document.querySelector('#propertyEstateName').textContent;
            let areaName = document.querySelector('#propertyAreaName').textContent;
            let price = document.querySelector('#propertyPrice').textContent;

            
            modalHeader1.textContent = `${bed} ${type} for ${rentSale}`
            modalHeader2.textContent = `${houseNumber}, ${street},
            ${estateName}, ${areaName}`
            modalHeader3.innerHTML= "";
            // modalHeader3.append(`${property.price}`)
            modalHeader3.innerHTML = `<span>&#x20A6;</span>${price}`

        })

        


    })


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


    // FLUTTERWAVE PAYMENT INTEGRATION
    let propertyPaymentButton = document.querySelector('#paymentButton');
    let price = parseInt(document.querySelector('#propertyPrice').textContent);
    

    propertyPaymentButton.addEventListener('click', function(){
        // USING BACKEND FOR PAYMENT PROCESSING
        const propertyId = propertyPaymentButton.getAttribute("data-propid")
        console.log(propertyId)


        fetch(`initiatepayment`,{
            method: "POST",
            headers: {
                'Content-Type': 'application/json'
            },
            body: JSON.stringify({
                propertyid: `${propertyId}`,
                amount: `${price*0.1}` 
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


})


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


})


// import jsonData from "./json/city.json" assert { type: "json" };

window.addEventListener("load", () => {
    // addOptions();
    console.log("adding completed")
   if(navigator.geolocation){
    navigator.geolocation.getCurrentPosition(position => {

        let lat = position.coords.latitude;
        let lon = position.coords.longitude;
        console.log(lat, lon)
        console.log(position)
        const API_KEY = `7f11cdd7f1de8797d5aa63f1c9da4679`
        fetch(`https://api.openweathermap.org/data/2.5/onecall?lat=${lat}&lon=${lon}&exclude={}&appid=${API_KEY}&units=metric`)
        .then( response => {
            return response.json();
        })
        .then(data => {
            console.log(data);
            showWeatherData(data);
        })
       
        // document.getElementById("timezone").innerHTML = data.timezone;
    })
    
   
   }
   else{
    console.log("ERROR")
   }

    function showWeatherData(data){
     //   let {country} = data.sys
        let {temp} = data.current;
        let {timezone, lat, lon} = data;
        let {description , } = data.current.weather[0];
        let {humidity, pressure} = data.current;
        console.log(lon);
        $('#icon').attr("src","http://openweathermap.org/img/wn/"+data.current.weather[0].icon+"@2x.png");

        document.getElementById("timezone").innerHTML = timezone;
        document.getElementById("temp").innerHTML = temp + "°" +"C";
        document.getElementById("humidity").innerHTML = "Humidity: " +humidity +"%";
        //document.getElementById("pressure").innerHTML = "Pressure: " +pressure;
      
        document.getElementById("weatherdesc").innerHTML = capitalize(description); 
       
     }


     document.querySelector("#searchbutton").addEventListener("click" , searchlocation);
     //enter key search 
     $('#search').keypress(function(event){
        var keycode = (event.keyCode ? event.keyCode : event.which);
        if(keycode == '13'){
          searchlocation();
        }
      });
     
    function searchlocation() {
         let search = document.getElementById("search").value;
         if(search != ''){
         console.log(search);
         console.log("search button clicked");
         const API_KEY = `7f11cdd7f1de8797d5aa63f1c9da4679`
         const api =  `https://api.openweathermap.org/data/2.5/weather?q=${search}&appid=${API_KEY}&units=metric`
         fetch(api).then( response => 
            {
             return response.json();
         })
         
         .then(data => {
             console.log(data);
             showWeatherDataByLocation(data);
         })
        }
     }
     
   
     function showWeatherDataByLocation(data) {
        let {name} = data;

        if(name){
            let {temp, humidity, pressure} = data.main;
            let {country} = data.sys
            temp = Math.ceil(temp)
    
            let {description} = data.weather[0];
            $('#icon').attr("src","http://openweathermap.org/img/wn/"+data.weather[0].icon+"@2x.png");
    
            document.getElementById("timezone").innerHTML = name + "," + country;
            document.getElementById("temp").innerHTML = temp + "°" +"C";
             document.getElementById("humidity").innerHTML = "Humidity: " +humidity +"%";
            // document.getElementById("pressure").innerHTML = "Pressure: " +pressure;
            document.getElementById("weatherdesc").innerHTML = capitalize(description); 
        }

        else{
            let error = data.message;
            console.log(error);
            errorMessage();
            
        }
       
       
     }

     function errorMessage(error){
        location.href = "error.html"

     }

     //go back page


   
})

//to capitalize first letter
function capitalize(string){
    const strings = string.charAt(0).toUpperCase() + string.slice(1);
    return strings;

}



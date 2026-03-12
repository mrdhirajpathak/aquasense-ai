function askAI(){

    let q = document.getElementById("question").value;

    fetch("/ask",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({question:q})
    })
    .then(r=>r.json())
    .then(data=>{
        document.getElementById("response").innerText = data.answer;
    });

}


function startVoice(){

    const recognition = new webkitSpeechRecognition();

    recognition.lang = "en-US";

    recognition.start();

    recognition.onresult = function(event){

        document.getElementById("question").value =
        event.results[0][0].transcript;

    }

}


function uploadImage(){

    let file = document.getElementById("imageInput").files[0];

    let formData = new FormData();

    formData.append("image",file);

    fetch("/upload",{
        method:"POST",
        body:formData
    })
    .then(r=>r.json())
    .then(data=>{
        document.getElementById("imageResult").innerText = data.result;
    });

}


function predictRainwater(){

    let city = document.getElementById("city").value;
    let area = document.getElementById("area").value;

    fetch("/rainwater",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            city:city,
            area:area
        })
    })
    .then(r=>r.json())
    .then(data=>{

        document.getElementById("rainResult").innerText =
        "Rainfall: " + data.rainfall_mm +
        " mm | Collectable Water: " + data.water_collectable +
        " L | " + data.recommendation;

    });

}


function calcWater(){

    let people = document.getElementById("people").value;
    let showers = document.getElementById("showers").value;
    let laundry = document.getElementById("laundry").value;

    fetch("/water-usage",{
        method:"POST",
        headers:{
            "Content-Type":"application/json"
        },
        body:JSON.stringify({
            people:people,
            showers:showers,
            laundry:laundry
        })
    })
    .then(r=>r.json())
    .then(data=>{

        document.getElementById("waterResult").innerText =
        "Daily usage: " + data.daily_usage_liters +
        " L | Monthly: " + data.monthly_usage_liters + " L";

    });

}
const final_parse = JSON.parse(localStorage.getItem("end-parse"));
console.log(final_parse);
let current = 0;
let backwards = document.getElementById("back");
let forwards = document.getElementById("start");
backwards.style.display = 'none'
let length = final_parse.length;

document.getElementById("between").innerHTML = "ASTEROIDS NEAR EARTH 🌎<br>BETWEEN " + final_parse[0]["close_approach"]["approach_date"] + " TO " + final_parse[length-1]["close_approach"]["approach_date"];



function print_everthing(){
    document.getElementById("aster-name").textContent = "Asteroid Name ☄️: " + final_parse[current]["name"];
    document.getElementById("aster-di").textContent = "Diamater 📏: " + final_parse[current]["diameter_km"]["estimated_diameter_min"] + "km to " + final_parse[current]["diameter_km"]["estimated_diameter_max"] + "km";
    document.getElementById("aster-time").textContent = "When 🗓️: " + final_parse[current]["close_approach"]["approach_date"] + " at " + final_parse[current]["close_approach"]["approach_time"];
    document.getElementById("aster-close").textContent = "Closest Approach 🤏: " + final_parse[current]["close_approach"]["approach_distance_au"] + " AU";
    document.getElementById("aster-vel").textContent = "Asteroid Velocity 🏎️: " + final_parse[current]["close_approach"]["approach_velocity_kmps"] + " km/s";
    if (final_parse[current]["hazard"]){
        document.getElementById("aster-hazard").textContent = "Potentinally Hazardous ⚠️: Yes";
    }
    else{
        document.getElementById("aster-hazard").textContent = "Potentially Hazardous ⚠️: No";
    };
}

print_everthing();


document.getElementById("start").addEventListener("click", function(){
    current++;
    if (current > 0){
        backwards.style.display = 'block';
    }
    if (current > length-2){
        forwards.style.display = 'none';
    }
    print_everthing();
    });


document.getElementById("back").addEventListener("click", function(){
    current = current - 1;
    if (current < 1){
        backwards.style.display = 'none';
    }
    if (current < length-1){
        forwards.style.display = 'block';
    }
    print_everthing();
    });

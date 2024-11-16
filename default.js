let START_DATE = "2015-09-01";
let END_DATE = "2015-09-04";

// API key and URL to allow for data fetching
const key = "hVbFkv9OANU05lWkidNnWRXLGKeV5i9JEzAVFnvu";
const apiURL = "https://api.nasa.gov/neo/rest/v1/feed?start_date="+START_DATE+"&end_date="+END_DATE+"&api_key="+key;

// Function that grabs and returns the necessary asteroid data.
async function get_data(url){
    // Fetch statement grabs data from the NASA API
    let data = fetch(url)
        // If the response is invalid for whatever reason
        .then(response => {
            if (!response.ok) {
                throw new Error('Network response was not skibidi.');
            }
            return response.json();
        })
        // Once its confirmed that the response is valid
        .then(data => {
            return data;
        })
        // If any error occurs
        .catch(error => {
            console.error('Error:', error);
    });
    // Sends back the unedited data provided by the API
    return data;
};

// Function that organizes and discards irrelevant data from the dataset provided by the API
function parse_data(data){
    try {
        let sorted_data = sort_data(data);
        
        let important_data = [];
        for (let i of sorted_data){
            let asteroid = {};
            
            asteroid["name"] = i["name"];
            
            asteroid["diameter_km"] = i["estimated_diameter"]["kilometers"];
            
            for (let j in asteroid["diameter_km"]){
                asteroid["diameter_km"][j] = Math.round(asteroid["diameter_km"][j]*1000)/1000;
            }
            
            let cad = i["close_approach_data"];
            
            let date = cad[0]["close_approach_date"];
            let time_uncondensed = cad[0]["close_approach_date_full"];
            let distance = Math.round(cad[0]["miss_distance"]["astronomical"]*100)/100;
            let velocity = Math.round(cad[0]["relative_velocity"]["kilometers_per_second"]*100)/100;
            
            asteroid["close_approach"] = {
                "approach_date":date,
                "approach_time":time_uncondensed.slice(time_uncondensed.indexOf(" ")+1),
                "approach_distance_au":distance,
                "approach_velocity_kmps":velocity
            }
            
            asteroid["hazard"] = i["is_potentially_hazardous_asteroid"];
            
            important_data.push(asteroid);
        }
        
        return important_data;
    } catch (TypeError){
        alert("That data appears to be invalid.");
        return 0;
    }
};

// Organizes the data by date and time
function sort_data(data){
    let num_objects = data["element_count"];
    let objects = data["near_earth_objects"];
    
    let dates = Object.keys(objects).sort();

    let result = [];
    for (let i of dates){
        result.push(objects[i].sort(date_sorting_algorithm));
    }
    
    let final = [];
    for (let i of result){
        for (let j of i){
            final.push(j);
        }
    }
    
    return final;
};

// Algorithm that takes two times and compares them
function date_sorting_algorithm(a,b){
    let d1 = a["close_approach_data"][0]["close_approach_date_full"];
    let d2 = b["close_approach_data"][0]["close_approach_date_full"];
    
    let t1 = d1.slice(d1.indexOf(" ")+1);
    let t2 = d2.slice(d2.indexOf(" ")+1);
    
    let h1 = +t1.slice(0,2);
    let h2 = +t2.slice(0,2);
    let m1 = +t1.slice(3,5);
    let m2 = +t2.slice(3,5);
    
    if (h1>h2){
        return 1;
    } else if (h1==h2){
        if (m1>=m2){
            return 1;
        } else {
            return -1;
        }
    } else {
        return -1;
    }
};

let raw_data = await get_data(apiURL);
let parsed_data = parse_data(raw_data);

console.log(parsed_data);
// API key and URL to allow for data fetching

const key = "hVbFkv9OANU05lWkidNnWRXLGKeV5i9JEzAVFnvu";

// Function that grabs and returns the necessary asteroid data.
async function get_data(url) {
    try {
        // Fetch statement grabs data from the NASA API
        const response = await fetch(url);
        
        // If the response is invalid for whatever reason
        if (!response.ok) {
            throw new Error('Network response was not okay.');
        }
        
        // Once it's confirmed that the response is valid
        const data = await response.json();
        // Sends back the unedited data provided by the API
        return data;
    } catch (error) {
        // If any error occurs
        console.error('Error:', error);
        return null;
    }
};

// Function that organizes and discards irrelevant data from the dataset provided by the API
function parse_data(data) {
    try {
        const sorted_data = sort_data(data);
        
        const important_data = sorted_data.map(i => {
            const asteroid = {
                name: i.name,
                diameter_km: Object.fromEntries(
                    Object.entries(i.estimated_diameter.kilometers).map(([key, value]) => [key, Math.round(value * 1000) / 1000])
                ),
                close_approach: {
                    approach_date: i.close_approach_data[0].close_approach_date,
                    approach_time: i.close_approach_data[0].close_approach_date_full.split(' ')[1],
                    approach_distance_au: Math.round(i.close_approach_data[0].miss_distance.astronomical * 100) / 100,
                    approach_velocity_kmps: Math.round(i.close_approach_data[0].relative_velocity.kilometers_per_second * 100) / 100
                },
                hazard: i.is_potentially_hazardous_asteroid
            };
            return asteroid;
        });
        
        return important_data;
    } catch (TypeError) {
        alert("That data appears to be invalid.");
        return null;
    }
};

// Organizes the data by date and time
function sort_data(data) {
    const dates = Object.keys(data.near_earth_objects).sort();
    const sorted_objects = dates.flatMap(date => data.near_earth_objects[date].sort(date_sorting_algorithm));
    return sorted_objects;
};

// Algorithm that takes two times and compares them
function date_sorting_algorithm(a, b) {
    const [d1, d2] = [a.close_approach_data[0].close_approach_date_full, b.close_approach_data[0].close_approach_date_full];
    const [t1, t2] = [d1.split(' ')[1], d2.split(' ')[1]];
    const [h1, h2] = [parseInt(t1.slice(0, 2)), parseInt(t2.slice(0, 2))];
    const [m1, m2] = [parseInt(t1.slice(3, 5)), parseInt(t2.slice(3, 5))];

    if (h1 > h2) return 1;
    if (h1 === h2) return m1 >= m2 ? 1 : -1;
    return -1;
};


 async function submitForm(){
    let START_DATE = document.getElementById('start').value;
    let END_DATE = document.getElementById('end').value;
    const apiURL = `https://api.nasa.gov/neo/rest/v1/feed?start_date=${START_DATE}&end_date=${END_DATE}&api_key=${key}`;
    
    const raw_data = await get_data(apiURL);
    if (raw_data) {
        const parsed_data = parse_data(raw_data);
        console.log(parsed_data);
        if (parsed_data.length<1){
            alert("Data was not valid. Try different dates.");
            throw new Error("Invalid data.");
        }
        localStorage.setItem("end-parse", JSON.stringify(parsed_data));
        window.location.href="second.html";
    } else {
        console.log('Failed to retrieve data.');
        alert("Cannot get data.");
    }
};

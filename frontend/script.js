let personalizedMenu = document.querySelectorAll(".personalizedMenu");
for (let i = 0; i < personalizedMenu.length; i++) {
  personalizedMenu[i].style.display = "none";
}
function showMenu(selected) {
  document.getElementById("mainMenu").style.display = "none";
  let personalizedMenu = document.querySelectorAll(".personalizedMenu");
  for (let i = 0; i < personalizedMenu.length; i++) {
    personalizedMenu[i].style.display = "none";
  }
  if (selected == 1)
    document.getElementById("calculator").style.display = "block";
  else if (selected == 2)
    document.getElementById("temperature").style.display = "block";
  else if (selected == 3)
    document.getElementById("2point").style.display = "block";
  else if (selected == 4)
    document.getElementById("BMI").style.display = "block";
  else if (selected == 5)
    document.getElementById("Age").style.display = "block";
  else document.getElementById("Home").style.display = "block";
}
function showMainMenu() {
  document.getElementById("mainMenu").style.display = "grid";
  let personalizedMenu = document.querySelectorAll(".personalizedMenu");
  for (let i = 0; i < personalizedMenu.length; i++) {
    personalizedMenu[i].style.display = "none";
  }
}
function collectData(menuId) {
  let baseUrl =
    "https://mxhue7rs3e5jqc7ttbbv3qvmaq0gszle.lambda-url.us-east-1.on.aws/?category=";
  let endpoint = "";
  let parameters = "";

  if (menuId === 1) {
    endpoint = "calculator";
    parameters = `operation=${
      document.getElementById("operationc").value
    }&number1=${document.getElementById("num1").value}&number2=${
      document.getElementById("num2").value
    }`;
  } else if (menuId === 2) {
    endpoint = "temp_conv";
    parameters = `operation=${
      document.getElementById("temperatureUnit").value
    }&temperature=${document.getElementById("temp").value}`;
  } else if (menuId === 3) {
    endpoint = "2_points";
    parameters = `x1=${document.getElementById("x1").value}&y1=${
      document.getElementById("y1").value
    }&x2=${document.getElementById("x2").value}&y2=${
      document.getElementById("y2").value
    }`;
  } else if (menuId === 4) {
    endpoint = "bmi";
    parameters = `age=${document.getElementById("age").value}&weight=${
      document.getElementById("weight").value
    }&height=${document.getElementById("height").value}`;
  } else if (menuId === 5) {
    endpoint = "age_calculator";
    parameters = `birthdate=${document.getElementById("dob").value}`;
  } else if (menuId === 6) {
    endpoint = "home_price_predictor";
    parameters = `location=${
      document.getElementById("location").value
    }&square_feet=${document.getElementById("sqft").value}&bedrooms=${
      document.getElementById("bedr").value
    }&bathrooms=${document.getElementById("bath").value}`;
  }

  let apiUrl = baseUrl + endpoint + "&" + parameters;
  console.log(`API URL: ${apiUrl}`);

  fetch(apiUrl)
    .then((response) => {
      // Check if the request was successful
      if (response.ok) {
        // Parse the JSON response
        return response.json();
      }
      throw new Error("Network response was not ok.");
    })
    .then((data) => {
      // Handle the JSON data
      console.log("Data from API:", data);
    })
    .catch((error) => {
      // Handle errors
      console.error("Error fetching data:", error);
    });
}

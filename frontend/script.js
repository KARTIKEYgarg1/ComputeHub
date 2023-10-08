
let personalizedMenu=document.querySelectorAll(".personalizedMenu");
for(let i=0;i<personalizedMenu.length;i++){
    personalizedMenu[i].style.display="none"; 
}
function showMenu(selected) {
    document.getElementById("mainMenu").style.display="none";
    let personalizedMenu=document.querySelectorAll(".personalizedMenu");
    for(let i=0;i<personalizedMenu.length;i++){
        personalizedMenu[i].style.display="none"; 
    }
    if(selected==1)document.getElementById("calculator").style.display="block";
    else if(selected==2)document.getElementById("temperature").style.display="block";
    else if(selected==3)document.getElementById("2point").style.display="block";
    else if(selected==4)document.getElementById("BMI").style.display="block";
    else if(selected==5)document.getElementById("Age").style.display="block";
    else document.getElementById("Home").style.display="block";
}
function showMainMenu() {
    document.getElementById("mainMenu").style.display="grid";
    let personalizedMenu=document.querySelectorAll(".personalizedMenu");
    for(let i=0;i<personalizedMenu.length;i++){
        personalizedMenu[i].style.display="none"; 
    } 
}

function collectData(menuId) {
    let num1, num2, result;

    if (menuId === 1) {
        num1 = document.getElementById('num1').value;
        num2 = document.getElementById('num2').value;
        result = document.getElementById('result').value;
    } else if (menuId === 2) {
        temp = document.getElementById('temp').value;
        temperatureUnit = document.getElementById('temperature').value;
        result = document.getElementById('result').value;
    } else if (menuId === 3) {
        x1 = document.getElementById('x1').value;
        y1 = document.getElementById('y1').value;
        x2 = document.getElementById('x2').value;
        y2 = document.getElementById('y2').value;
        result = document.getElementById('result').value;
    } else if (menuId === 4) {
        age = document.getElementById('age').value;
        height = document.getElementById('height').value;
        weight = document.getElementById('weight').value;
        result = document.getElementById('result').value;
    } else if (menuId === 5) {
        dob = document.getElementById('dob').value;
        result = document.getElementById('result').value;
    } else if (menuId === 6) {
        location = document.getElementById('Location').value;
        sqft = document.getElementById('sqft').value;
        bedr = document.getElementById('bedr').value;
        bath = document.getElementById('bath').value;
        result = document.getElementById('result').value;
    }

    console.log(`Menu ID: ${menuId}`);
}


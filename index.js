let naveName =  prompt("Digite uma palavra")
let newNaveName = ""

for(let i = naveName.length -1; i >= 0; i-- ){
        newNaveName += naveName[i]
}

alert("Nome original: "+ naveName + "\nNome invertido: " + newNaveName)
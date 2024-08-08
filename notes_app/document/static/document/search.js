const data = '{{qs_json}}'
console.log(data)

const rdata = JSON.parse(data.replace(/&quote;/g, '"'))
console.log(rdata)

const input = document.getElementById('search_here')
console.log(input)

const box = document.getElementById('box')

let filteredArr = []

input.addEventListener('keyup', (e)=>{
    box.innerHTML = ''
    filteredArr = rdata.filter(note=> note['name'].includes(e.target.value))
    console.log(filteredArr)
    if (filteredArr.length > 0){
         filteredArr.map(item=>{
            box.innerHTML += `<b>${item['name']}</b><br>`
         })
    }
})
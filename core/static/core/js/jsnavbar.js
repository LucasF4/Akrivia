const url = location.href
console.log(url)
const hrefMod = location.href.split('http://192.168.0.19/api/v1/survivor/')[1].split('/')[0]
console.log(hrefMod)
document.getElementById(`${hrefMod}`).classList.add('active')

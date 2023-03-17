const hrefMod = location.href.split('http://localhost:8000/api/v1/survivor/')[1].split('/')[0]

document.getElementById(`${hrefMod}`).classList.add('active')

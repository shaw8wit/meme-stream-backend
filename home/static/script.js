const url = document.getElementById('url');
const form = document.querySelector('form');
const output = document.getElementById('output');
const username = document.getElementById('name');
const caption = document.getElementById('caption');

const getMemeHolder = (name, caption, url) => {
    return `<div class="column is-4-desktop is-6-tablet">
                <div class="card">
                    <div class="card-header">
                        <h3 class="card-header-title is-size-5">${name}</h3>
                    </div>
                    <div class="card-content">
                        <div class="content">
                            <h1 class="subtitle is-size-5-tablet is-size-6-mobile m-0 has-text-weight-normal">${caption}</h1>
                        </div>
                    </div>
                    <div class="card-image">
                        <figure class="image is-5by4">
                            <img src="${url}" alt="${name}:${caption}">
                        </figure>
                    </div>
                </div>
            </div>`;
}

const checkImage = (url) => {
    var image = new Image();
    image.onload = function () {
        if (this.width > 0) {
            console.log("image exists");
        }
    }
    image.onerror = function () {
        console.log("image doesn't exist");
    }
    image.src = url;
}

const getMemes = () => {
    let result = '';
    fetch('/memes')
        .then(response => response.json())
        .then(data => {
            data.forEach(e => result = result.concat(getMemeHolder(e.name, e.caption, e.url)));
            output.innerHTML = result;
        });
};


const saveMeme = () => {

    fetch('/memes', {
            method: 'POST',
            headers: {
                'Accept': 'application/json',
                'Content-Type': 'application/json',
            },
            body: JSON.stringify({
                name: username.value,
                caption: caption.value,
                url: url.value,
            })
        })
        .then(response => response.json())
        .then(data => {
            console.log(data);
            getMemes();
        });

    form.reset();
    return false;
}


document.addEventListener("DOMContentLoaded", getMemes);
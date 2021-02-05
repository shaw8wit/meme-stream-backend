const url = document.getElementById('url');
const form = document.querySelector('form');
const output = document.getElementById('output');
const username = document.getElementById('name');
const caption = document.getElementById('caption');

const getMemeHolder = (name, caption, url) => {
    return `<div class="column is-4-desktop is-6-tablet">
                <div class="card">
                    <div class="card-image">
                        <figure class="image is-5by4">
                            <img src="${url}" alt="${name}:${caption}">
                        </figure>
                    </div>
                    <div class="card-content">
                        <div class="content">
                            <h1 class="title is-size-4-tablet is-size-5-mobile m-0 has-text-weight-normal">${caption}</h1>
                        </div>
                    </div>
                    <div class="card-footer">
                        <div class="card-footer-item has-text-right">
                            <h3 class="subtitle">By: <strong>${name}</strong></h3>
                        </div>
                    </div>
                </div>
            </div>`;
}

const saveMeme = () => {

    output.innerHTML = output.innerHTML.concat(getMemeHolder(username.value, caption.value, url.value));

    form.reset();
    return false;
}


document.addEventListener("DOMContentLoaded", () => {
    let result = '';

    fetch('/memes')
        .then(response => response.json())
        .then(data => {
            data.forEach(e => result = result.concat(getMemeHolder(e.name, e.caption, e.url)));
            output.innerHTML = result;
        });
});
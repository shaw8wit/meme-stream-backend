const form = document.querySelector('form');
const username = document.getElementById('name');
const caption = document.getElementById('caption');
const url = document.getElementById('url');

function saveMeme() {
    console.log(username.value, caption.value, url.value, "sdjskldjkl");
    form.reset();
    return false;
}
function saveMeme() {
    const username = document.getElementById('username').value;
    const caption = document.getElementById('caption').value;
    const url = document.getElementById('url').value;
    document.querySelector('form').reset();
    console.log(username, caption, url);
    return false;
}
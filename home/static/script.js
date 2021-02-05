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
    [{
        'name': "test one name",
        'caption': "test one caption",
        'url': "https://3c534w2w7sa3ma8ved14ax12-wpengine.netdna-ssl.com/wp-content/uploads/2020/07/Copy-of-Untitled-2020-07-08T105340.290-1080x630.png"
    }, {
        'name': "test two name",
        'caption': "test two caption",
        'url': "https://images.hindustantimes.com/rf/image_size_630x354/HT/p2/2020/10/26/Pictures/_1b8238d2-1749-11eb-8018-0bdbc3b69c17.jpg"
    }, {
        'name': "test three name",
        'caption': "test three caption",
        'url': "https://i.pinimg.com/736x/a2/3d/27/a23d2700baae88a347dbc6de49192eae.jpg"
    }, {
        'name': "test four name",
        'caption': "test four captijfklsdjklfjklsdjfklsdjkfljsdklfjklsdjklfjsdklfjklsdjfklsdjklfjsdklfjklsdjfljlon",
        'url': "https://cdn.vox-cdn.com/thumbor/cV8X8BZ-aGs8pv3D-sCMr5fQZyI=/1400x1400/filters:format(png)/cdn.vox-cdn.com/uploads/chorus_asset/file/19933026/image.png"
    }, {
        'name': "test five name",
        'caption': "test five caption",
        'url': "https://cms.qz.com/wp-content/uploads/2018/07/meme-featured.jpg"
    }].forEach(e => result = result.concat(getMemeHolder(e.name, e.caption, e.url)));

    output.innerHTML = result;
});
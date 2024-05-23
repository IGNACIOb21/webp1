

window.onload = function() {
    var modal = document.getElementById("modal");
    var closeButton = document.getElementById("close-button");

    modal.style.display = "block";

    closeButton.onclick = function() {
        modal.style.display = "none";
    };

    window.onclick = function(event) {
        if (event.target == modal) {
            modal.style.display = "none";
        }
    };

    var buttonPrev = document.getElementById("button-prev");
    var buttonNext = document.getElementById("button-next");

    buttonPrev.onclick = function(event) {
        processingButton(event);
    };

    buttonNext.onclick = function(event) {
        processingButton(event);
    };
};


function processingButton(event) {
    const btn = event.currentTarget;
    const carruselList = btn.parentNode;
    const track = carruselList.querySelector('#track');
    const carrusels = track.querySelectorAll('.carrusel');

    const carruselWidth = carrusels[0].offsetWidth;
    const trackWidth = track.scrollWidth;
    const listWidth = carruselList.offsetWidth;

    let leftPosition = track.style.left ? parseFloat(track.style.left.slice(0, -2)) * -1 : 0;

    if (btn.dataset.button == "button-prev") {
        prevAction(leftPosition, carruselWidth, track);
    } else {
        nextAction(leftPosition, trackWidth, listWidth, carruselWidth, track);
    }
}

function prevAction(leftPosition, carruselWidth, track) {
    if (leftPosition > 0) {
        track.style.left = `${-1 * (leftPosition - carruselWidth)}px`;
    }
}

function nextAction(leftPosition, trackWidth, listWidth, carruselWidth, track) {
    if (leftPosition < (trackWidth - listWidth)) {
        track.style.left = `${-1 * (leftPosition + carruselWidth)}px`;
    }
}
